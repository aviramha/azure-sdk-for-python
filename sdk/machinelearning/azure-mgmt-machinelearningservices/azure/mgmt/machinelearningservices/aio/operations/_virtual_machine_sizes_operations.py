# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class VirtualMachineSizesOperations:
    """VirtualMachineSizesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.machinelearningservices.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def list(
        self,
        location: str,
        compute_type: Optional[str] = None,
        recommended: Optional[bool] = None,
        **kwargs
    ) -> "_models.VirtualMachineSizeListResult":
        """Returns supported VM Sizes in a location.

        :param location: The location upon which virtual-machine-sizes is queried.
        :type location: str
        :param compute_type: Type of compute to filter by.
        :type compute_type: str
        :param recommended: Specifies whether to return recommended vm sizes or all vm sizes.
        :type recommended: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualMachineSizeListResult, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.VirtualMachineSizeListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VirtualMachineSizeListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-08-01"
        accept = "application/json"

        # Construct URL
        url = self.list.metadata['url']  # type: ignore
        path_format_arguments = {
            'location': self._serialize.url("location", location, 'str', pattern=r'^[-\w\._]+$'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if compute_type is not None:
            query_parameters['compute-type'] = self._serialize.query("compute_type", compute_type, 'str')
        if recommended is not None:
            query_parameters['recommended'] = self._serialize.query("recommended", recommended, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('VirtualMachineSizeListResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/locations/{location}/vmSizes'}  # type: ignore
