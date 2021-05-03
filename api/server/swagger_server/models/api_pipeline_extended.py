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
from swagger_server.models.api_parameter import ApiParameter  # noqa: F401,E501
from swagger_server.models.api_pipeline import ApiPipeline  # noqa: F401,E501
from swagger_server.models.api_pipeline_extension import ApiPipelineExtension  # noqa: F401,E501
from swagger_server import util


class ApiPipelineExtended(ApiPipeline, ApiPipelineExtension):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, created_at: datetime=None, name: str=None, description: str=None, parameters: List[ApiParameter]=None, status: str=None, default_version_id: str=None, annotations: Dict[str, str]=None, featured: bool=None, publish_approved: bool=None):  # noqa: E501
        """ApiPipelineExtended - a model defined in Swagger

        :param id: The id of this ApiPipelineExtended.  # noqa: E501
        :type id: str
        :param created_at: The created_at of this ApiPipelineExtended.  # noqa: E501
        :type created_at: datetime
        :param name: The name of this ApiPipelineExtended.  # noqa: E501
        :type name: str
        :param description: The description of this ApiPipelineExtended.  # noqa: E501
        :type description: str
        :param parameters: The parameters of this ApiPipelineExtended.  # noqa: E501
        :type parameters: List[ApiParameter]
        :param status: The status of this ApiPipelineExtended.  # noqa: E501
        :type status: str
        :param default_version_id: The default_version_id of this ApiPipelineExtended.  # noqa: E501
        :type default_version_id: str
        :param annotations: The annotations of this ApiPipelineExtended.  # noqa: E501
        :type annotations: Dict[str, str]
        :param featured: The featured of this ApiPipelineExtended.  # noqa: E501
        :type featured: bool
        :param publish_approved: The publish_approved of this ApiPipelineExtended.  # noqa: E501
        :type publish_approved: bool
        """
        self.swagger_types = {
            'id': str,
            'created_at': datetime,
            'name': str,
            'description': str,
            'parameters': List[ApiParameter],
            'status': str,
            'default_version_id': str,
            'annotations': Dict[str, str],
            'featured': bool,
            'publish_approved': bool
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'name': 'name',
            'description': 'description',
            'parameters': 'parameters',
            'status': 'status',
            'default_version_id': 'default_version_id',
            'annotations': 'annotations',
            'featured': 'featured',
            'publish_approved': 'publish_approved'
        }

        self._id = id
        self._created_at = created_at
        self._name = name
        self._description = description
        self._parameters = parameters
        self._status = status
        self._default_version_id = default_version_id
        self._annotations = annotations
        self._featured = featured
        self._publish_approved = publish_approved

    @classmethod
    def from_dict(cls, dikt) -> 'ApiPipelineExtended':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apiPipelineExtended of this ApiPipelineExtended.  # noqa: E501
        :rtype: ApiPipelineExtended
        """
        return util.deserialize_model(dikt, cls)

    # @property
    # def id(self) -> str:
    #     """Gets the id of this ApiPipelineExtended.
    #
    #
    #     :return: The id of this ApiPipelineExtended.
    #     :rtype: str
    #     """
    #     return self._id
    #
    # @id.setter
    # def id(self, id: str):
    #     """Sets the id of this ApiPipelineExtended.
    #
    #
    #     :param id: The id of this ApiPipelineExtended.
    #     :type id: str
    #     """
    #
    #     self._id = id
    #
    # @property
    # def created_at(self) -> datetime:
    #     """Gets the created_at of this ApiPipelineExtended.
    #
    #
    #     :return: The created_at of this ApiPipelineExtended.
    #     :rtype: datetime
    #     """
    #     return self._created_at
    #
    # @created_at.setter
    # def created_at(self, created_at: datetime):
    #     """Sets the created_at of this ApiPipelineExtended.
    #
    #
    #     :param created_at: The created_at of this ApiPipelineExtended.
    #     :type created_at: datetime
    #     """
    #
    #     self._created_at = created_at
    #
    # @property
    # def name(self) -> str:
    #     """Gets the name of this ApiPipelineExtended.
    #
    #
    #     :return: The name of this ApiPipelineExtended.
    #     :rtype: str
    #     """
    #     return self._name
    #
    # @name.setter
    # def name(self, name: str):
    #     """Sets the name of this ApiPipelineExtended.
    #
    #
    #     :param name: The name of this ApiPipelineExtended.
    #     :type name: str
    #     """
    #
    #     self._name = name
    #
    # @property
    # def description(self) -> str:
    #     """Gets the description of this ApiPipelineExtended.
    #
    #
    #     :return: The description of this ApiPipelineExtended.
    #     :rtype: str
    #     """
    #     return self._description
    #
    # @description.setter
    # def description(self, description: str):
    #     """Sets the description of this ApiPipelineExtended.
    #
    #
    #     :param description: The description of this ApiPipelineExtended.
    #     :type description: str
    #     """
    #
    #     self._description = description
    #
    # @property
    # def parameters(self) -> List[ApiParameter]:
    #     """Gets the parameters of this ApiPipelineExtended.
    #
    #
    #     :return: The parameters of this ApiPipelineExtended.
    #     :rtype: List[ApiParameter]
    #     """
    #     return self._parameters
    #
    # @parameters.setter
    # def parameters(self, parameters: List[ApiParameter]):
    #     """Sets the parameters of this ApiPipelineExtended.
    #
    #
    #     :param parameters: The parameters of this ApiPipelineExtended.
    #     :type parameters: List[ApiParameter]
    #     """
    #
    #     self._parameters = parameters
    #
    # @property
    # def status(self) -> str:
    #     """Gets the status of this ApiPipelineExtended.
    #
    #     In case any error happens retrieving a pipeline field, only pipeline ID and the error message is returned. Client has the flexibility of choosing how to handle error. This is especially useful during listing call.  # noqa: E501
    #
    #     :return: The status of this ApiPipelineExtended.
    #     :rtype: str
    #     """
    #     return self._status
    #
    # @status.setter
    # def status(self, status: str):
    #     """Sets the status of this ApiPipelineExtended.
    #
    #     In case any error happens retrieving a pipeline field, only pipeline ID and the error message is returned. Client has the flexibility of choosing how to handle error. This is especially useful during listing call.  # noqa: E501
    #
    #     :param status: The status of this ApiPipelineExtended.
    #     :type status: str
    #     """
    #
    #     self._status = status
    #
    # @property
    # def default_version_id(self) -> str:
    #     """Gets the default_version_id of this ApiPipelineExtended.
    #
    #     The default version of the pipeline. As of now, the latest version is used as default. (In the future, if desired by customers, we can allow them to set default version.)  # noqa: E501
    #
    #     :return: The default_version_id of this ApiPipelineExtended.
    #     :rtype: str
    #     """
    #     return self._default_version_id
    #
    # @default_version_id.setter
    # def default_version_id(self, default_version_id: str):
    #     """Sets the default_version_id of this ApiPipelineExtended.
    #
    #     The default version of the pipeline. As of now, the latest version is used as default. (In the future, if desired by customers, we can allow them to set default version.)  # noqa: E501
    #
    #     :param default_version_id: The default_version_id of this ApiPipelineExtended.
    #     :type default_version_id: str
    #     """
    #
    #     self._default_version_id = default_version_id
    #
    # @property
    # def annotations(self) -> Dict[str, str]:
    #     """Gets the annotations of this ApiPipelineExtended.
    #
    #
    #     :return: The annotations of this ApiPipelineExtended.
    #     :rtype: Dict[str, str]
    #     """
    #     return self._annotations
    #
    # @annotations.setter
    # def annotations(self, annotations: Dict[str, str]):
    #     """Sets the annotations of this ApiPipelineExtended.
    #
    #
    #     :param annotations: The annotations of this ApiPipelineExtended.
    #     :type annotations: Dict[str, str]
    #     """
    #
    #     self._annotations = annotations
    #
    # @property
    # def featured(self) -> bool:
    #     """Gets the featured of this ApiPipelineExtended.
    #
    #
    #     :return: The featured of this ApiPipelineExtended.
    #     :rtype: bool
    #     """
    #     return self._featured
    #
    # @featured.setter
    # def featured(self, featured: bool):
    #     """Sets the featured of this ApiPipelineExtended.
    #
    #
    #     :param featured: The featured of this ApiPipelineExtended.
    #     :type featured: bool
    #     """
    #
    #     self._featured = featured
    #
    # @property
    # def publish_approved(self) -> bool:
    #     """Gets the publish_approved of this ApiPipelineExtended.
    #
    #
    #     :return: The publish_approved of this ApiPipelineExtended.
    #     :rtype: bool
    #     """
    #     return self._publish_approved
    #
    # @publish_approved.setter
    # def publish_approved(self, publish_approved: bool):
    #     """Sets the publish_approved of this ApiPipelineExtended.
    #
    #
    #     :param publish_approved: The publish_approved of this ApiPipelineExtended.
    #     :type publish_approved: bool
    #     """
    #
    #     self._publish_approved = publish_approved