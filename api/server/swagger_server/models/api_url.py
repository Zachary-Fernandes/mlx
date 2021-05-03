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


class ApiUrl(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, pipeline_url: str=None):  # noqa: E501
        """ApiUrl - a model defined in Swagger

        :param pipeline_url: The pipeline_url of this ApiUrl.  # noqa: E501
        :type pipeline_url: str
        """
        self.swagger_types = {
            'pipeline_url': str
        }

        self.attribute_map = {
            'pipeline_url': 'pipeline_url'
        }

        self._pipeline_url = pipeline_url

    @classmethod
    def from_dict(cls, dikt) -> 'ApiUrl':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apiUrl of this ApiUrl.  # noqa: E501
        :rtype: ApiUrl
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pipeline_url(self) -> str:
        """Gets the pipeline_url of this ApiUrl.


        :return: The pipeline_url of this ApiUrl.
        :rtype: str
        """
        return self._pipeline_url

    @pipeline_url.setter
    def pipeline_url(self, pipeline_url: str):
        """Sets the pipeline_url of this ApiUrl.


        :param pipeline_url: The pipeline_url of this ApiUrl.
        :type pipeline_url: str
        """

        self._pipeline_url = pipeline_url