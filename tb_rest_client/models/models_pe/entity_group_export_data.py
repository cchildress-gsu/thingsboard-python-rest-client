# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0PE-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from tb_rest_client.models.models_pe import EntityExportDataobject  # noqa: F401,E501

class EntityGroupExportData(EntityExportDataobject):
    """

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
        'attributes': 'dict(str, list[AttributeExportData])',
        'entity': 'EntityGroup',
        'entity_type': 'str',
        'group_entities': 'bool',
        'permissions': 'list[GroupPermission]',
        'relations': 'list[EntityRelation]'
    }
    if hasattr(EntityExportDataobject, "swagger_types"):
        swagger_types.update(EntityExportDataobject.swagger_types)

    attribute_map = {
        'attributes': 'attributes',
        'entity': 'entity',
        'entity_type': 'entityType',
        'group_entities': 'groupEntities',
        'permissions': 'permissions',
        'relations': 'relations'
    }
    if hasattr(EntityExportDataobject, "attribute_map"):
        attribute_map.update(EntityExportDataobject.attribute_map)

    def __init__(self, attributes=None, entity=None, entity_type=None, group_entities=None, permissions=None, relations=None, *args, **kwargs):  # noqa: E501
        """EntityGroupExportData - a model defined in Swagger"""  # noqa: E501
        self._attributes = None
        self._entity = None
        self._entity_type = None
        self._group_entities = None
        self._permissions = None
        self._relations = None
        self.discriminator = None
        if attributes is not None:
            self.attributes = attributes
        if entity is not None:
            self.entity = entity
        if entity_type is not None:
            self.entity_type = entity_type
        if group_entities is not None:
            self.group_entities = group_entities
        if permissions is not None:
            self.permissions = permissions
        if relations is not None:
            self.relations = relations
        EntityExportDataobject.__init__(self, *args, **kwargs)

    @property
    def attributes(self):
        """Gets the attributes of this EntityGroupExportData.  # noqa: E501


        :return: The attributes of this EntityGroupExportData.  # noqa: E501
        :rtype: dict(str, list[AttributeExportData])
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this EntityGroupExportData.


        :param attributes: The attributes of this EntityGroupExportData.  # noqa: E501
        :type: dict(str, list[AttributeExportData])
        """

        self._attributes = attributes

    @property
    def entity(self):
        """Gets the entity of this EntityGroupExportData.  # noqa: E501


        :return: The entity of this EntityGroupExportData.  # noqa: E501
        :rtype: EntityGroup
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this EntityGroupExportData.


        :param entity: The entity of this EntityGroupExportData.  # noqa: E501
        :type: EntityGroup
        """

        self._entity = entity

    @property
    def entity_type(self):
        """Gets the entity_type of this EntityGroupExportData.  # noqa: E501


        :return: The entity_type of this EntityGroupExportData.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this EntityGroupExportData.


        :param entity_type: The entity_type of this EntityGroupExportData.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "API_USAGE_STATE", "ASSET", "BLOB_ENTITY", "CONVERTER", "CUSTOMER", "DASHBOARD", "DEVICE", "DEVICE_PROFILE", "EDGE", "ENTITY_GROUP", "ENTITY_VIEW", "GROUP_PERMISSION", "INTEGRATION", "OTA_PACKAGE", "QUEUE", "ROLE", "RPC", "RULE_CHAIN", "RULE_NODE", "SCHEDULER_EVENT", "TB_RESOURCE", "TENANT", "TENANT_PROFILE", "USER", "WIDGETS_BUNDLE", "WIDGET_TYPE"]  # noqa: E501
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def group_entities(self):
        """Gets the group_entities of this EntityGroupExportData.  # noqa: E501


        :return: The group_entities of this EntityGroupExportData.  # noqa: E501
        :rtype: bool
        """
        return self._group_entities

    @group_entities.setter
    def group_entities(self, group_entities):
        """Sets the group_entities of this EntityGroupExportData.


        :param group_entities: The group_entities of this EntityGroupExportData.  # noqa: E501
        :type: bool
        """

        self._group_entities = group_entities

    @property
    def permissions(self):
        """Gets the permissions of this EntityGroupExportData.  # noqa: E501


        :return: The permissions of this EntityGroupExportData.  # noqa: E501
        :rtype: list[GroupPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this EntityGroupExportData.


        :param permissions: The permissions of this EntityGroupExportData.  # noqa: E501
        :type: list[GroupPermission]
        """

        self._permissions = permissions

    @property
    def relations(self):
        """Gets the relations of this EntityGroupExportData.  # noqa: E501


        :return: The relations of this EntityGroupExportData.  # noqa: E501
        :rtype: list[EntityRelation]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this EntityGroupExportData.


        :param relations: The relations of this EntityGroupExportData.  # noqa: E501
        :type: list[EntityRelation]
        """

        self._relations = relations

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
        if issubclass(EntityGroupExportData, dict):
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
        if not isinstance(other, EntityGroupExportData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other