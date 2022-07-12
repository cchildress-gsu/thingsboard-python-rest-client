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
from .entity_filter import EntityFilter  # noqa: F401,E501

class AssetTypeFilter(EntityFilter):
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
        'asset_name_filter': 'str',
        'asset_type': 'str'
    }
    if hasattr(EntityFilter, "swagger_types"):
        swagger_types.update(EntityFilter.swagger_types)

    attribute_map = {
        'asset_name_filter': 'assetNameFilter',
        'asset_type': 'assetType'
    }
    if hasattr(EntityFilter, "attribute_map"):
        attribute_map.update(EntityFilter.attribute_map)

    def __init__(self, asset_name_filter=None, asset_type=None, *args, **kwargs):  # noqa: E501
        """AssetTypeFilter - a model defined in Swagger"""  # noqa: E501
        self._asset_name_filter = None
        self._asset_type = None
        self.discriminator = None
        if asset_name_filter is not None:
            self.asset_name_filter = asset_name_filter
        if asset_type is not None:
            self.asset_type = asset_type
        EntityFilter.__init__(self, *args, **kwargs)

    @property
    def asset_name_filter(self):
        """Gets the asset_name_filter of this AssetTypeFilter.  # noqa: E501


        :return: The asset_name_filter of this AssetTypeFilter.  # noqa: E501
        :rtype: str
        """
        return self._asset_name_filter

    @asset_name_filter.setter
    def asset_name_filter(self, asset_name_filter):
        """Sets the asset_name_filter of this AssetTypeFilter.


        :param asset_name_filter: The asset_name_filter of this AssetTypeFilter.  # noqa: E501
        :type: str
        """

        self._asset_name_filter = asset_name_filter

    @property
    def asset_type(self):
        """Gets the asset_type of this AssetTypeFilter.  # noqa: E501


        :return: The asset_type of this AssetTypeFilter.  # noqa: E501
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this AssetTypeFilter.


        :param asset_type: The asset_type of this AssetTypeFilter.  # noqa: E501
        :type: str
        """

        self._asset_type = asset_type

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
        if issubclass(AssetTypeFilter, dict):
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
        if not isinstance(other, AssetTypeFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
