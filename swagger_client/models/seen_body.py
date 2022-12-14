# coding: utf-8

"""
    API whatsgate.ru

    Интерфейс для взаимодействия с клиентом Whatsapp  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SeenBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'whatsapp_id': 'str',
        'recipient': 'AnyOfseenBodyRecipient'
    }

    attribute_map = {
        'whatsapp_id': 'WhatsappID',
        'recipient': 'recipient'
    }

    def __init__(self, whatsapp_id=None, recipient=None):  # noqa: E501
        """SeenBody - a model defined in Swagger"""  # noqa: E501
        self._whatsapp_id = None
        self._recipient = None
        self.discriminator = None
        if whatsapp_id is not None:
            self.whatsapp_id = whatsapp_id
        if recipient is not None:
            self.recipient = recipient

    @property
    def whatsapp_id(self):
        """Gets the whatsapp_id of this SeenBody.  # noqa: E501

        Идентификатор Whatsapp ID  # noqa: E501

        :return: The whatsapp_id of this SeenBody.  # noqa: E501
        :rtype: str
        """
        return self._whatsapp_id

    @whatsapp_id.setter
    def whatsapp_id(self, whatsapp_id):
        """Sets the whatsapp_id of this SeenBody.

        Идентификатор Whatsapp ID  # noqa: E501

        :param whatsapp_id: The whatsapp_id of this SeenBody.  # noqa: E501
        :type: str
        """

        self._whatsapp_id = whatsapp_id

    @property
    def recipient(self):
        """Gets the recipient of this SeenBody.  # noqa: E501


        :return: The recipient of this SeenBody.  # noqa: E501
        :rtype: AnyOfseenBodyRecipient
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this SeenBody.


        :param recipient: The recipient of this SeenBody.  # noqa: E501
        :type: AnyOfseenBodyRecipient
        """

        self._recipient = recipient

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
        if issubclass(SeenBody, dict):
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
        if not isinstance(other, SeenBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
