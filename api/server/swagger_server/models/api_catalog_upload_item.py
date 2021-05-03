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

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ApiCatalogUploadItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, url: str=None):  # noqa: E501
        """ApiCatalogUploadItem - a model defined in Swagger

        :param name: The name of this ApiCatalogUploadItem.  # noqa: E501
        :type name: str
        :param url: The url of this ApiCatalogUploadItem.  # noqa: E501
        :type url: str
        """
        self.swagger_types = {
            'name': str,
            'url': str
        }

        self.attribute_map = {
            'name': 'name',
            'url': 'url'
        }

        self._name = name
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'ApiCatalogUploadItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apiCatalogUploadItem of this ApiCatalogUploadItem.  # noqa: E501
        :rtype: ApiCatalogUploadItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this ApiCatalogUploadItem.


        :return: The name of this ApiCatalogUploadItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ApiCatalogUploadItem.


        :param name: The name of this ApiCatalogUploadItem.
        :type name: str
        """

        self._name = name

    @property
    def url(self) -> str:
        """Gets the url of this ApiCatalogUploadItem.

        The URL to the YAML metadata file, i.e. on GitHub.com  # noqa: E501

        :return: The url of this ApiCatalogUploadItem.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this ApiCatalogUploadItem.

        The URL to the YAML metadata file, i.e. on GitHub.com  # noqa: E501

        :param url: The url of this ApiCatalogUploadItem.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url