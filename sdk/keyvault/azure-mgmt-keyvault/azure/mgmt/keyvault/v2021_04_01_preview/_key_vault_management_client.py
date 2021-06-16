# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

from ._configuration import KeyVaultManagementClientConfiguration
from .operations import VaultsOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from .operations import ManagedHsmsOperations
from .operations import MHSMPrivateEndpointConnectionsOperations
from .operations import MHSMPrivateLinkResourcesOperations
from .operations import Operations
from .operations import SecretsOperations
from . import models


class KeyVaultManagementClient(object):
    """The Azure management API provides a RESTful set of web services that interact with Azure Key Vault.

    :ivar vaults: VaultsOperations operations
    :vartype vaults: azure.mgmt.keyvault.v2021_04_01_preview.operations.VaultsOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure.mgmt.keyvault.v2021_04_01_preview.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.keyvault.v2021_04_01_preview.operations.PrivateLinkResourcesOperations
    :ivar managed_hsms: ManagedHsmsOperations operations
    :vartype managed_hsms: azure.mgmt.keyvault.v2021_04_01_preview.operations.ManagedHsmsOperations
    :ivar mhsm_private_endpoint_connections: MHSMPrivateEndpointConnectionsOperations operations
    :vartype mhsm_private_endpoint_connections: azure.mgmt.keyvault.v2021_04_01_preview.operations.MHSMPrivateEndpointConnectionsOperations
    :ivar mhsm_private_link_resources: MHSMPrivateLinkResourcesOperations operations
    :vartype mhsm_private_link_resources: azure.mgmt.keyvault.v2021_04_01_preview.operations.MHSMPrivateLinkResourcesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.keyvault.v2021_04_01_preview.operations.Operations
    :ivar secrets: SecretsOperations operations
    :vartype secrets: azure.mgmt.keyvault.v2021_04_01_preview.operations.SecretsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = KeyVaultManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.vaults = VaultsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.managed_hsms = ManagedHsmsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.mhsm_private_endpoint_connections = MHSMPrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.mhsm_private_link_resources = MHSMPrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.secrets = SecretsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.HttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> KeyVaultManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
