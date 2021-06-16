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

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class AttestationOperations:
    """AttestationOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.security.attestation._generated.models
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

    async def attest_open_enclave(
        self,
        request: "_models.AttestOpenEnclaveRequest",
        **kwargs
    ) -> "_models.AttestationResponse":
        """Attest to an SGX enclave.

        Processes an OpenEnclave report , producing an artifact. The type of artifact produced is
        dependent upon attestation policy.

        :param request: Request object containing the quote.
        :type request: ~azure.security.attestation._generated.models.AttestOpenEnclaveRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationResponse, or the result of cls(response)
        :rtype: ~azure.security.attestation._generated.models.AttestationResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AttestationResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-10-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.attest_open_enclave.metadata['url']  # type: ignore
        path_format_arguments = {
            'instanceUrl': self._serialize.url("self._config.instance_url", self._config.instance_url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(request, 'AttestOpenEnclaveRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('AttestationResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    attest_open_enclave.metadata = {'url': '/attest/OpenEnclave'}  # type: ignore

    async def attest_sgx_enclave(
        self,
        request: "_models.AttestSgxEnclaveRequest",
        **kwargs
    ) -> "_models.AttestationResponse":
        """Attest to an SGX enclave.

        Processes an SGX enclave quote, producing an artifact. The type of artifact produced is
        dependent upon attestation policy.

        :param request: Request object containing the quote.
        :type request: ~azure.security.attestation._generated.models.AttestSgxEnclaveRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationResponse, or the result of cls(response)
        :rtype: ~azure.security.attestation._generated.models.AttestationResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AttestationResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-10-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.attest_sgx_enclave.metadata['url']  # type: ignore
        path_format_arguments = {
            'instanceUrl': self._serialize.url("self._config.instance_url", self._config.instance_url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(request, 'AttestSgxEnclaveRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('AttestationResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    attest_sgx_enclave.metadata = {'url': '/attest/SgxEnclave'}  # type: ignore

    async def attest_tpm(
        self,
        data: Optional[bytes] = None,
        **kwargs
    ) -> "_models.TpmAttestationResponse":
        """Attest a Virtualization-based Security (VBS) enclave.

        Processes attestation evidence from a VBS enclave, producing an attestation result. The
        attestation result produced is dependent upon the attestation policy.

        :param data: Protocol data containing artifacts for attestation.
        :type data: bytes
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TpmAttestationResponse, or the result of cls(response)
        :rtype: ~azure.security.attestation._generated.models.TpmAttestationResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TpmAttestationResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        _request = _models.TpmAttestationRequest(data=data)
        api_version = "2020-10-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.attest_tpm.metadata['url']  # type: ignore
        path_format_arguments = {
            'instanceUrl': self._serialize.url("self._config.instance_url", self._config.instance_url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_request, 'TpmAttestationRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('TpmAttestationResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    attest_tpm.metadata = {'url': '/attest/Tpm'}  # type: ignore
