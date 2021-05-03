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
import connexion
import json

from datetime import datetime

from swagger_server.data_access.mysql_client import store_data, generate_id, load_data, delete_data, num_rows
from swagger_server.gateways.kubernetes_service import create_secret, get_secret, delete_secret, list_secrets,\
    secret_name_prefix
from swagger_server.models.api_credential import ApiCredential  # noqa: E501
from swagger_server.models.api_list_credentials_response import ApiListCredentialsResponse  # noqa: E501
from swagger_server.models.api_status import ApiStatus  # noqa: E501


def create_credential(body):  # noqa: E501
    """create_credential

    Creates a credential associated with a pipeline. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ApiCredential
    """
    if connexion.request.is_json:
        body = ApiCredential.from_dict(connexion.request.get_json())

    api_credential: ApiCredential = body

    api_credential.id = api_credential.id or f"{secret_name_prefix}-{generate_id(length=16)}".lower()
    api_credential.created_at = datetime.now()

    error = store_data(api_credential)

    if error:
        return error, 400

    # TODO: do we need to generate some token or return something generated by K8s?
    secret = create_secret(api_credential.id,
                           {key: value for key, value in api_credential.to_dict().items()
                            if key not in ["id", "created_at"]})

    # TODO: remove credential if kubernetes secret was not created

    return api_credential, 200  # TODO: return 201


def delete_credential(id):  # noqa: E501
    """delete_credential

    :param id: 
    :type id: str

    :rtype: None
    """
    delete_data(ApiCredential, id)

    delete_secret(id)

    return f"Credential {id} was deleted", 200


def get_credential(id):  # noqa: E501
    """get_credential

    :param id: 
    :type id: str

    :rtype: ApiComponent
    """
    api_credentials: [ApiCredential] = load_data(ApiCredential, filter_dict={"id": id})

    if not api_credentials:
        return "Not found", 404

    api_credential = api_credentials[0]

    secret = get_secret(id)

    return api_credential, 200


def list_credentials(page_token=None, page_size=None, sort_by=None, filter=None):  # noqa: E501
    """list_credentials

    :param page_token:
    :type page_token: str
    :param page_size:
    :type page_size: int
    :param sort_by: Can be format of \&quot;field_name\&quot;, \&quot;field_name asc\&quot; or \&quot;field_name des\&quot; Ascending by default.
    :type sort_by: str
    :param filter: A string-serialized JSON dictionary containing key-value pairs with name of the object property to apply filter on and the value of the respective property.
    :type filter: str

    :rtype: ApiListCredentialsResponse
    """

    if page_size == 0:
        return {}, 200

    # TODO: do not misuse page_token as MySQL result offset
    offset = int(page_token) if page_token and page_token.isdigit() else 0

    filter_dict = json.loads(filter) if filter else None

    api_credentials: [ApiCredential] = load_data(ApiCredential, filter_dict=filter_dict, sort_by=sort_by,
                                                 count=page_size, offset=offset)

    next_page_token = offset + page_size if len(api_credentials) == page_size else None

    total_size = num_rows(ApiCredential)

    if total_size == next_page_token:
        next_page_token = None

    secrets = list_secrets(name_prefix=secret_name_prefix)

    # TODO: consolidate kubernetes secrets with MLX registered credentials (i.e. add status field?)
    comp_list = ApiListCredentialsResponse(credentials=api_credentials, total_size=total_size,
                                           next_page_token=next_page_token)
    return comp_list, 200