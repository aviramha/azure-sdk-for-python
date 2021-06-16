# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import TextAnalyticsClientConfiguration
from .operations import TextAnalyticsClientOperationsMixin
from .. import models


class TextAnalyticsClient(TextAnalyticsClientOperationsMixin):
    """The Text Analytics API is a suite of natural language processing (NLP)  services built with best-in-class Microsoft machine learning algorithms.  The API can be used to analyze unstructured text for tasks such as sentiment analysis, key phrase extraction and language detection. Functionality for analysis of text specific to the healthcare domain and personal information are also available in the API. Further documentation can be found in :code:`<a href="https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview">https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview</a>`.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param endpoint: Supported Cognitive Services endpoints (protocol and hostname, for example: https://westus.api.cognitive.microsoft.com).
    :type endpoint: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        endpoint: str,
        **kwargs: Any
    ) -> None:
        base_url = '{Endpoint}/text/analytics/v3.1-preview.5'
        self._config = TextAnalyticsClientConfiguration(credential, endpoint, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)


    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "TextAnalyticsClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
