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

class ProcessingStrategy(object):
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
        'failure_percentage': 'float',
        'max_pause_between_retries': 'int',
        'pause_between_retries': 'int',
        'retries': 'int',
        'type': 'str'
    }

    attribute_map = {
        'failure_percentage': 'failurePercentage',
        'max_pause_between_retries': 'maxPauseBetweenRetries',
        'pause_between_retries': 'pauseBetweenRetries',
        'retries': 'retries',
        'type': 'type'
    }

    def __init__(self, failure_percentage=None, max_pause_between_retries=None, pause_between_retries=None, retries=None, type=None):  # noqa: E501
        """ProcessingStrategy - a model defined in Swagger"""  # noqa: E501
        self._failure_percentage = None
        self._max_pause_between_retries = None
        self._pause_between_retries = None
        self._retries = None
        self._type = None
        self.discriminator = None
        if failure_percentage is not None:
            self.failure_percentage = failure_percentage
        if max_pause_between_retries is not None:
            self.max_pause_between_retries = max_pause_between_retries
        if pause_between_retries is not None:
            self.pause_between_retries = pause_between_retries
        if retries is not None:
            self.retries = retries
        if type is not None:
            self.type = type

    @property
    def failure_percentage(self):
        """Gets the failure_percentage of this ProcessingStrategy.  # noqa: E501


        :return: The failure_percentage of this ProcessingStrategy.  # noqa: E501
        :rtype: float
        """
        return self._failure_percentage

    @failure_percentage.setter
    def failure_percentage(self, failure_percentage):
        """Sets the failure_percentage of this ProcessingStrategy.


        :param failure_percentage: The failure_percentage of this ProcessingStrategy.  # noqa: E501
        :type: float
        """

        self._failure_percentage = failure_percentage

    @property
    def max_pause_between_retries(self):
        """Gets the max_pause_between_retries of this ProcessingStrategy.  # noqa: E501


        :return: The max_pause_between_retries of this ProcessingStrategy.  # noqa: E501
        :rtype: int
        """
        return self._max_pause_between_retries

    @max_pause_between_retries.setter
    def max_pause_between_retries(self, max_pause_between_retries):
        """Sets the max_pause_between_retries of this ProcessingStrategy.


        :param max_pause_between_retries: The max_pause_between_retries of this ProcessingStrategy.  # noqa: E501
        :type: int
        """

        self._max_pause_between_retries = max_pause_between_retries

    @property
    def pause_between_retries(self):
        """Gets the pause_between_retries of this ProcessingStrategy.  # noqa: E501


        :return: The pause_between_retries of this ProcessingStrategy.  # noqa: E501
        :rtype: int
        """
        return self._pause_between_retries

    @pause_between_retries.setter
    def pause_between_retries(self, pause_between_retries):
        """Sets the pause_between_retries of this ProcessingStrategy.


        :param pause_between_retries: The pause_between_retries of this ProcessingStrategy.  # noqa: E501
        :type: int
        """

        self._pause_between_retries = pause_between_retries

    @property
    def retries(self):
        """Gets the retries of this ProcessingStrategy.  # noqa: E501


        :return: The retries of this ProcessingStrategy.  # noqa: E501
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this ProcessingStrategy.


        :param retries: The retries of this ProcessingStrategy.  # noqa: E501
        :type: int
        """

        self._retries = retries

    @property
    def type(self):
        """Gets the type of this ProcessingStrategy.  # noqa: E501


        :return: The type of this ProcessingStrategy.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProcessingStrategy.


        :param type: The type of this ProcessingStrategy.  # noqa: E501
        :type: str
        """
        allowed_values = ["RETRY_ALL", "RETRY_FAILED", "RETRY_FAILED_AND_TIMED_OUT", "RETRY_TIMED_OUT", "SKIP_ALL_FAILURES", "SKIP_ALL_FAILURES_AND_TIMED_OUT"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(ProcessingStrategy, dict):
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
        if not isinstance(other, ProcessingStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
