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
from .event_filter import EventFilter  # noqa: F401,E501

class StatisticsEventFilter(EventFilter):
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
        'event_type': 'str',
        'server': 'str',
        'messages_processed': 'int',
        'errors_occurred': 'int'
    }
    if hasattr(EventFilter, "swagger_types"):
        swagger_types.update(EventFilter.swagger_types)

    attribute_map = {
        'event_type': 'eventType',
        'server': 'server',
        'messages_processed': 'messagesProcessed',
        'errors_occurred': 'errorsOccurred'
    }
    if hasattr(EventFilter, "attribute_map"):
        attribute_map.update(EventFilter.attribute_map)

    def __init__(self, event_type=None, server=None, messages_processed=None, errors_occurred=None, *args, **kwargs):  # noqa: E501
        """StatisticsEventFilter - a model defined in Swagger"""  # noqa: E501
        self._event_type = None
        self._server = None
        self._messages_processed = None
        self._errors_occurred = None
        self.discriminator = None
        self.event_type = event_type
        if server is not None:
            self.server = server
        if messages_processed is not None:
            self.messages_processed = messages_processed
        if errors_occurred is not None:
            self.errors_occurred = errors_occurred
        EventFilter.__init__(self, *args, **kwargs)

    @property
    def event_type(self):
        """Gets the event_type of this StatisticsEventFilter.  # noqa: E501

        String value representing the event type  # noqa: E501

        :return: The event_type of this StatisticsEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this StatisticsEventFilter.

        String value representing the event type  # noqa: E501

        :param event_type: The event_type of this StatisticsEventFilter.  # noqa: E501
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DEBUG_RULE_CHAIN", "DEBUG_RULE_NODE", "ERROR", "LC_EVENT", "STATS"]  # noqa: E501
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def server(self):
        """Gets the server of this StatisticsEventFilter.  # noqa: E501

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :return: The server of this StatisticsEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this StatisticsEventFilter.

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :param server: The server of this StatisticsEventFilter.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def messages_processed(self):
        """Gets the messages_processed of this StatisticsEventFilter.  # noqa: E501

        The minimum number of successfully processed messages  # noqa: E501

        :return: The messages_processed of this StatisticsEventFilter.  # noqa: E501
        :rtype: int
        """
        return self._messages_processed

    @messages_processed.setter
    def messages_processed(self, messages_processed):
        """Sets the messages_processed of this StatisticsEventFilter.

        The minimum number of successfully processed messages  # noqa: E501

        :param messages_processed: The messages_processed of this StatisticsEventFilter.  # noqa: E501
        :type: int
        """

        self._messages_processed = messages_processed

    @property
    def errors_occurred(self):
        """Gets the errors_occurred of this StatisticsEventFilter.  # noqa: E501

        The minimum number of errors occurred during messages processing  # noqa: E501

        :return: The errors_occurred of this StatisticsEventFilter.  # noqa: E501
        :rtype: int
        """
        return self._errors_occurred

    @errors_occurred.setter
    def errors_occurred(self, errors_occurred):
        """Sets the errors_occurred of this StatisticsEventFilter.

        The minimum number of errors occurred during messages processing  # noqa: E501

        :param errors_occurred: The errors_occurred of this StatisticsEventFilter.  # noqa: E501
        :type: int
        """

        self._errors_occurred = errors_occurred

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
        if issubclass(StatisticsEventFilter, dict):
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
        if not isinstance(other, StatisticsEventFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
