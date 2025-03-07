#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

import logging
from json import load
# Importing models and REST client class from Professional Edition version
from tb_rest_client.rest_client_pe import *
from tb_rest_client.rest import ApiException


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


# ThingsBoard REST API URL
url = "http://localhost:8080"

# Default Tenant Administrator credentials
username = "tenant@thingsboard.org"
password = "tenant"


# Creating the REST client object with context manager to get auto token refresh
def main():
    with RestClientPE(base_url=url) as rest_client:
        try:
            # Auth with credentials
            rest_client.login(username=username, password=password)

            # Getting current user
            current_user = rest_client.get_user()

            # Creating Dashboard Group on the Tenant Level
            shared_dashboards_group = EntityGroup(name="Shared Dashboards", type="DASHBOARD")
            shared_dashboards_group = rest_client.save_entity_group(shared_dashboards_group)

            # Loading Dashboard from file
            dashboard_json = None
            with open("watermeters.json", "r") as dashboard_file:
                dashboard_json = load(dashboard_file)
            dashboard = Dashboard(title=dashboard_json["title"], configuration=dashboard_json["configuration"])
            dashboard = rest_client.save_dashboard(dashboard)

            # Adding Dashboard to the Shared Dashboards Group
            rest_client.add_entities_to_entity_group([dashboard.id.id], shared_dashboards_group.id)

            # Creating Customer 1
            customer1 = Customer(title="Customer 1")
            customer1 = rest_client.save_customer(customer1)

            # Creating Device
            device = Device(name="WaterMeter1", type="waterMeter")
            device = rest_client.save_device(device)

            # Fetching automatically created "Customer Administrators" Group.
            customer1_administrators = rest_client.get_entity_group_by_owner_and_name_and_type(customer1.id.entity_type, customer1.id.id, "USER", "Customer Administrators")

            # Creating Read-Only Role
            read_only_role = Role(name="Read-Only", permissions=['READ', 'READ_ATTRIBUTES', 'READ_TELEMETRY', 'READ_CREDENTIALS'], type="GROUP")
            read_only_role = rest_client.save_role(read_only_role)

            # Assigning Shared Dashboards to the Customer 1 Administrators
            tenant_id = current_user.tenant_id
            group_permission = GroupPermission(role_id=read_only_role.id,
                                               name="Read Only Permission",
                                               is_public=False,
                                               user_group_id=customer1_administrators.id,
                                               tenant_id=tenant_id,
                                               entity_group_id=shared_dashboards_group.id,
                                               entity_group_type=shared_dashboards_group.type)
            group_permission = rest_client.save_group_permission(group_permission)

            # Creating User for Customer 1 with default dashboard from Tenant "Shared Dashboards" group.
            user_email = "user@thingsboard.org"
            user_password = "secret"
            additional_info = {
                "defaultDashboardId": dashboard.id.id,
                "defaultDashboardFullscreen": False
            }
            user = User(authority="CUSTOMER_USER",
                        customer_id=customer1.id,
                        email=user_email,
                        additional_info=additional_info)
            user = rest_client.save_user(user, send_activation_mail=False)
            rest_client.activate_user(user.id, user_password)

            rest_client.add_entities_to_entity_group([user.id.id], customer1_administrators.id)

        except ApiException as e:
            logging.exception(e)

if __name__ == '__main__':
    main()