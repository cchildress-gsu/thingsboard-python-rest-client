# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TenantInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.
from tb_rest_client.api_client import ApiClient
    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'TenantId',
        'created_time': 'int',
        'title': 'str',
        'name': 'str',
        'region': 'str',
        'tenant_profile_id': 'TenantProfileId',
        'country': 'str',
        'state': 'str',
        'city': 'str',
        'address': 'str',
        'address2': 'str',
        'zip': 'str',
        'phone': 'str',
        'email': 'str',
        'additional_info': 'JsonNode',
        'tenant_profile_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'title': 'title',
        'name': 'name',
        'region': 'region',
        'tenant_profile_id': 'tenantProfileId',
        'country': 'country',
        'state': 'state',
        'city': 'city',
        'address': 'address',
        'address2': 'address2',
        'zip': 'zip',
        'phone': 'phone',
        'email': 'email',
        'additional_info': 'additionalInfo',
        'tenant_profile_name': 'tenantProfileName'
    }

    def __init__(self, id=None, created_time=None, title=None, name=None, region=None, tenant_profile_id=None, country=None, state=None, city=None, address=None, address2=None, zip=None, phone=None, email=None, additional_info=None, tenant_profile_name=None):  # noqa: E501
        """TenantInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._title = None
        self._name = None
        self._region = None
        self._tenant_profile_id = None
        self._country = None
        self._state = None
        self._city = None
        self._address = None
        self._address2 = None
        self._zip = None
        self._phone = None
        self._email = None
        self._additional_info = None
        self._tenant_profile_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if title is not None:
            self.title = title
        if name is not None:
            self.name = name
        if region is not None:
            self.region = region
        self.tenant_profile_id = tenant_profile_id
        self.country = country
        self.state = state
        self.city = city
        self.address = address
        self.address2 = address2
        self.zip = zip
        self.phone = phone
        self.email = email
        if additional_info is not None:
            self.additional_info = additional_info
        if tenant_profile_name is not None:
            self.tenant_profile_name = tenant_profile_name

    @property
    def id(self):
        """Gets the id of this TenantInfo.  # noqa: E501


        :return: The id of this TenantInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TenantInfo.


        :param id: The id of this TenantInfo.  # noqa: E501
        :type: TenantId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this TenantInfo.  # noqa: E501

        Timestamp of the tenant creation, in milliseconds  # noqa: E501

        :return: The created_time of this TenantInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this TenantInfo.

        Timestamp of the tenant creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this TenantInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def title(self):
        """Gets the title of this TenantInfo.  # noqa: E501

        Title of the tenant  # noqa: E501

        :return: The title of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TenantInfo.

        Title of the tenant  # noqa: E501

        :param title: The title of this TenantInfo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def name(self):
        """Gets the name of this TenantInfo.  # noqa: E501

        Name of the tenant. Read-only, duplicated from title for backward compatibility  # noqa: E501

        :return: The name of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TenantInfo.

        Name of the tenant. Read-only, duplicated from title for backward compatibility  # noqa: E501

        :param name: The name of this TenantInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def region(self):
        """Gets the region of this TenantInfo.  # noqa: E501

        Geo region of the tenant  # noqa: E501

        :return: The region of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TenantInfo.

        Geo region of the tenant  # noqa: E501

        :param region: The region of this TenantInfo.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def tenant_profile_id(self):
        """Gets the tenant_profile_id of this TenantInfo.  # noqa: E501


        :return: The tenant_profile_id of this TenantInfo.  # noqa: E501
        :rtype: TenantProfileId
        """
        return self._tenant_profile_id

    @tenant_profile_id.setter
    def tenant_profile_id(self, tenant_profile_id):
        """Sets the tenant_profile_id of this TenantInfo.


        :param tenant_profile_id: The tenant_profile_id of this TenantInfo.  # noqa: E501
        :type: TenantProfileId
        """
        if tenant_profile_id is None:
            raise ValueError("Invalid value for `tenant_profile_id`, must not be `None`")  # noqa: E501

        self._tenant_profile_id = tenant_profile_id

    @property
    def country(self):
        """Gets the country of this TenantInfo.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this TenantInfo.

        Country  # noqa: E501

        :param country: The country of this TenantInfo.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def state(self):
        """Gets the state of this TenantInfo.  # noqa: E501

        State  # noqa: E501

        :return: The state of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TenantInfo.

        State  # noqa: E501

        :param state: The state of this TenantInfo.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def city(self):
        """Gets the city of this TenantInfo.  # noqa: E501

        City  # noqa: E501

        :return: The city of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this TenantInfo.

        City  # noqa: E501

        :param city: The city of this TenantInfo.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def address(self):
        """Gets the address of this TenantInfo.  # noqa: E501

        Address Line 1  # noqa: E501

        :return: The address of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this TenantInfo.

        Address Line 1  # noqa: E501

        :param address: The address of this TenantInfo.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this TenantInfo.  # noqa: E501

        Address Line 2  # noqa: E501

        :return: The address2 of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this TenantInfo.

        Address Line 2  # noqa: E501

        :param address2: The address2 of this TenantInfo.  # noqa: E501
        :type: str
        """
        if address2 is None:
            raise ValueError("Invalid value for `address2`, must not be `None`")  # noqa: E501

        self._address2 = address2

    @property
    def zip(self):
        """Gets the zip of this TenantInfo.  # noqa: E501

        Zip code  # noqa: E501

        :return: The zip of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this TenantInfo.

        Zip code  # noqa: E501

        :param zip: The zip of this TenantInfo.  # noqa: E501
        :type: str
        """
        if zip is None:
            raise ValueError("Invalid value for `zip`, must not be `None`")  # noqa: E501

        self._zip = zip

    @property
    def phone(self):
        """Gets the phone of this TenantInfo.  # noqa: E501

        Phone number  # noqa: E501

        :return: The phone of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this TenantInfo.

        Phone number  # noqa: E501

        :param phone: The phone of this TenantInfo.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this TenantInfo.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TenantInfo.

        Email  # noqa: E501

        :param email: The email of this TenantInfo.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def additional_info(self):
        """Gets the additional_info of this TenantInfo.  # noqa: E501


        :return: The additional_info of this TenantInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this TenantInfo.


        :param additional_info: The additional_info of this TenantInfo.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def tenant_profile_name(self):
        """Gets the tenant_profile_name of this TenantInfo.  # noqa: E501

        Tenant Profile name  # noqa: E501

        :return: The tenant_profile_name of this TenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._tenant_profile_name

    @tenant_profile_name.setter
    def tenant_profile_name(self, tenant_profile_name):
        """Sets the tenant_profile_name of this TenantInfo.

        Tenant Profile name  # noqa: E501

        :param tenant_profile_name: The tenant_profile_name of this TenantInfo.  # noqa: E501
        :type: str
        """

        self._tenant_profile_name = tenant_profile_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TenantInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TenantInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
