# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8

"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1.25-related-assets
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.api_parameter import ApiParameter  # noqa: F401,E501


class ApiSettingsSection(object):
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
        'name': 'str',
        'description': 'str',
        'settings': 'list[ApiParameter]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'settings': 'settings'
    }

    def __init__(self, name=None, description=None, settings=None):  # noqa: E501
        """ApiSettingsSection - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._settings = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if settings is not None:
            self.settings = settings

    @property
    def name(self):
        """Gets the name of this ApiSettingsSection.  # noqa: E501

        Display name of the configuration category.  # noqa: E501

        :return: The name of this ApiSettingsSection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiSettingsSection.

        Display name of the configuration category.  # noqa: E501

        :param name: The name of this ApiSettingsSection.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApiSettingsSection.  # noqa: E501

        Display text of the configuration category.  # noqa: E501

        :return: The description of this ApiSettingsSection.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiSettingsSection.

        Display text of the configuration category.  # noqa: E501

        :param description: The description of this ApiSettingsSection.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def settings(self):
        """Gets the settings of this ApiSettingsSection.  # noqa: E501

        List of settings.  # noqa: E501

        :return: The settings of this ApiSettingsSection.  # noqa: E501
        :rtype: list[ApiParameter]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this ApiSettingsSection.

        List of settings.  # noqa: E501

        :param settings: The settings of this ApiSettingsSection.  # noqa: E501
        :type: list[ApiParameter]
        """

        self._settings = settings

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
        if issubclass(ApiSettingsSection, dict):
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
        if not isinstance(other, ApiSettingsSection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other