# coding: utf-8

"""
    Service Fabric Reliable Collection Backup Explorer OpenApi

    OpenApi spec of [service-fabric-backup-explorer](http://github.com/Microsoft/service-fabric-backup-explorer).  # noqa: E501

    OpenAPI spec version: 0.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AddTransactionResponse(object):
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
        'collection': 'str',
        'operation': 'str',
        'partition_id': 'str',
        'key': 'object',
        'status': 'str',
        'description': 'str'
    }

    attribute_map = {
        'collection': 'Collection',
        'operation': 'Operation',
        'partition_id': 'PartitionId',
        'key': 'Key',
        'status': 'Status',
        'description': 'Description'
    }

    def __init__(self, collection=None, operation=None, partition_id=None, key=None, status=None, description=None):  # noqa: E501
        """AddTransactionResponse - a model defined in Swagger"""  # noqa: E501
        self._collection = None
        self._operation = None
        self._partition_id = None
        self._key = None
        self._status = None
        self._description = None
        self.discriminator = None
        if collection is not None:
            self.collection = collection
        if operation is not None:
            self.operation = operation
        if partition_id is not None:
            self.partition_id = partition_id
        if key is not None:
            self.key = key
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description

    @property
    def collection(self):
        """Gets the collection of this AddTransactionResponse.  # noqa: E501

        Changed dictionary name  # noqa: E501

        :return: The collection of this AddTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this AddTransactionResponse.

        Changed dictionary name  # noqa: E501

        :param collection: The collection of this AddTransactionResponse.  # noqa: E501
        :type: str
        """

        self._collection = collection

    @property
    def operation(self):
        """Gets the operation of this AddTransactionResponse.  # noqa: E501


        :return: The operation of this AddTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this AddTransactionResponse.


        :param operation: The operation of this AddTransactionResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Add", "Update", "Delete"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def partition_id(self):
        """Gets the partition_id of this AddTransactionResponse.  # noqa: E501

        Partition id   # noqa: E501

        :return: The partition_id of this AddTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        """Sets the partition_id of this AddTransactionResponse.

        Partition id   # noqa: E501

        :param partition_id: The partition_id of this AddTransactionResponse.  # noqa: E501
        :type: str
        """

        self._partition_id = partition_id

    @property
    def key(self):
        """Gets the key of this AddTransactionResponse.  # noqa: E501

        Key of the dictionary  # noqa: E501

        :return: The key of this AddTransactionResponse.  # noqa: E501
        :rtype: object
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AddTransactionResponse.

        Key of the dictionary  # noqa: E501

        :param key: The key of this AddTransactionResponse.  # noqa: E501
        :type: object
        """

        self._key = key

    @property
    def status(self):
        """Gets the status of this AddTransactionResponse.  # noqa: E501

        200 for successfull update  # noqa: E501

        :return: The status of this AddTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AddTransactionResponse.

        200 for successfull update  # noqa: E501

        :param status: The status of this AddTransactionResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def description(self):
        """Gets the description of this AddTransactionResponse.  # noqa: E501

        Details of the request  # noqa: E501

        :return: The description of this AddTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddTransactionResponse.

        Details of the request  # noqa: E501

        :param description: The description of this AddTransactionResponse.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(AddTransactionResponse, dict):
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
        if not isinstance(other, AddTransactionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other