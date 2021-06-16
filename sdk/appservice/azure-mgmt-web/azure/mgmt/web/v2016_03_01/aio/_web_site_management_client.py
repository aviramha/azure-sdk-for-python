# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import WebSiteManagementClientConfiguration
from .operations import CertificatesOperations
from .operations import DeletedWebAppsOperations
from .operations import DiagnosticsOperations
from .operations import ProviderOperations
from .operations import RecommendationsOperations
from .operations import ResourceHealthMetadataOperations
from .operations import WebSiteManagementClientOperationsMixin
from .operations import BillingMetersOperations
from .. import models


class WebSiteManagementClient(WebSiteManagementClientOperationsMixin):
    """WebSite Management Client.

    :ivar certificates: CertificatesOperations operations
    :vartype certificates: azure.mgmt.web.v2016_03_01.aio.operations.CertificatesOperations
    :ivar deleted_web_apps: DeletedWebAppsOperations operations
    :vartype deleted_web_apps: azure.mgmt.web.v2016_03_01.aio.operations.DeletedWebAppsOperations
    :ivar diagnostics: DiagnosticsOperations operations
    :vartype diagnostics: azure.mgmt.web.v2016_03_01.aio.operations.DiagnosticsOperations
    :ivar provider: ProviderOperations operations
    :vartype provider: azure.mgmt.web.v2016_03_01.aio.operations.ProviderOperations
    :ivar recommendations: RecommendationsOperations operations
    :vartype recommendations: azure.mgmt.web.v2016_03_01.aio.operations.RecommendationsOperations
    :ivar resource_health_metadata: ResourceHealthMetadataOperations operations
    :vartype resource_health_metadata: azure.mgmt.web.v2016_03_01.aio.operations.ResourceHealthMetadataOperations
    :ivar billing_meters: BillingMetersOperations operations
    :vartype billing_meters: azure.mgmt.web.v2016_03_01.aio.operations.BillingMetersOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = WebSiteManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.certificates = CertificatesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.deleted_web_apps = DeletedWebAppsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.diagnostics = DiagnosticsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.provider = ProviderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.recommendations = RecommendationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.resource_health_metadata = ResourceHealthMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_meters = BillingMetersOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "WebSiteManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
