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
from swagger_server.models.api_pipeline_task import ApiPipelineTask  # noqa: F401,E501
from swagger_server import util


class ApiPipelineDAG(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, tasks: List[ApiPipelineTask]=None):  # noqa: E501
        """ApiPipelineDAG - a model defined in Swagger

        :param tasks: The tasks of this ApiPipelineDAG.  # noqa: E501
        :type tasks: List[ApiPipelineTask]
        """
        self.swagger_types = {
            'tasks': List[ApiPipelineTask]
        }

        self.attribute_map = {
            'tasks': 'tasks'
        }

        self._tasks = tasks

    @classmethod
    def from_dict(cls, dikt) -> 'ApiPipelineDAG':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apiPipelineDAG of this ApiPipelineDAG.  # noqa: E501
        :rtype: ApiPipelineDAG
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tasks(self) -> List[ApiPipelineTask]:
        """Gets the tasks of this ApiPipelineDAG.

        List of pipeline tasks.  # noqa: E501

        :return: The tasks of this ApiPipelineDAG.
        :rtype: List[ApiPipelineTask]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks: List[ApiPipelineTask]):
        """Sets the tasks of this ApiPipelineDAG.

        List of pipeline tasks.  # noqa: E501

        :param tasks: The tasks of this ApiPipelineDAG.
        :type tasks: List[ApiPipelineTask]
        """

        self._tasks = tasks