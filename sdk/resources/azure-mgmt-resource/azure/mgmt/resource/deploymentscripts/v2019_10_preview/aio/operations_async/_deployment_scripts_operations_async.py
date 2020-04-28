# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncNoPolling, AsyncPollingMethod, async_poller
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DeploymentScriptsOperations:
    """DeploymentScriptsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def _create_initial(
        self,
        resource_group_name: str,
        script_name: str,
        deployment_script: "models.DeploymentScript",
        **kwargs
    ) -> "models.DeploymentScript":
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DeploymentScript"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'scriptName': self._serialize.url("script_name", script_name, 'str', max_length=90, min_length=1),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(deployment_script, 'DeploymentScript')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DeploymentScriptsError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DeploymentScript', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('DeploymentScript', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}'}  # type: ignore

    async def create(
        self,
        resource_group_name: str,
        script_name: str,
        deployment_script: "models.DeploymentScript",
        **kwargs
    ) -> "models.DeploymentScript":
        """Creates a deployment script.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param script_name: Name of the deployment script.
        :type script_name: str
        :param deployment_script: Deployment script supplied to the operation.
        :type deployment_script: ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.DeploymentScript
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: DeploymentScript
        :rtype: ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.DeploymentScript
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DeploymentScript"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = await self._create_initial(
            resource_group_name=resource_group_name,
            script_name=script_name,
            deployment_script=deployment_script,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('DeploymentScript', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}'}  # type: ignore

    async def update(
        self,
        resource_group_name: str,
        script_name: str,
        deployment_script: Optional["models.DeploymentScriptUpdateParameter"] = None,
        **kwargs
    ) -> "models.DeploymentScript":
        """Updates deployment script tags with specified values.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param script_name: Name of the deployment script.
        :type script_name: str
        :param deployment_script: Deployment script resource with the tags to be updated.
        :type deployment_script: ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.DeploymentScriptUpdateParameter
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DeploymentScript or the result of cls(response)
        :rtype: ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.DeploymentScript
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DeploymentScript"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'scriptName': self._serialize.url("script_name", script_name, 'str', max_length=90, min_length=1),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        if deployment_script is not None:
            body_content = self._serialize.body(deployment_script, 'DeploymentScriptUpdateParameter')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DeploymentScriptsError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DeploymentScript', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}'}  # type: ignore

    async def get(
        self,
        resource_group_name: str,
        script_name: str,
        **kwargs
    ) -> "models.DeploymentScript":
        """Gets a deployment script with a given name.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param script_name: Name of the deployment script.
        :type script_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DeploymentScript or the result of cls(response)
        :rtype: ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.DeploymentScript
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DeploymentScript"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01-preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'scriptName': self._serialize.url("script_name", script_name, 'str', max_length=90, min_length=1),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DeploymentScriptsError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DeploymentScript', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}'}  # type: ignore

    async def delete(
        self,
        resource_group_name: str,
        script_name: str,
        **kwargs
    ) -> None:
        """Deletes a deployment script. When operation completes, status code 200 returned without content.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param script_name: Name of the deployment script.
        :type script_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01-preview"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'scriptName': self._serialize.url("script_name", script_name, 'str', max_length=90, min_length=1),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DeploymentScriptsError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}'}  # type: ignore

    def list_by_subscription(
        self,
        **kwargs
    ) -> AsyncIterable["models.DeploymentScriptListResult"]:
        """Lists all deployment scripts for a given subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of DeploymentScriptListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.DeploymentScriptListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DeploymentScriptListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_subscription.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('DeploymentScriptListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.DeploymentScriptsError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Resources/deploymentScripts'}  # type: ignore

    async def get_logs(
        self,
        resource_group_name: str,
        script_name: str,
        **kwargs
    ) -> "models.ScriptLogsList":
        """Gets deployment script logs for a given deployment script name.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param script_name: Name of the deployment script.
        :type script_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ScriptLogsList or the result of cls(response)
        :rtype: ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptLogsList
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ScriptLogsList"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01-preview"

        # Construct URL
        url = self.get_logs.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'scriptName': self._serialize.url("script_name", script_name, 'str', max_length=90, min_length=1),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DeploymentScriptsError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ScriptLogsList', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_logs.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}/logs'}  # type: ignore

    async def get_logs_default(
        self,
        resource_group_name: str,
        script_name: str,
        tail: Optional[int] = None,
        **kwargs
    ) -> "models.ScriptLog":
        """Gets deployment script logs for a given deployment script name.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param script_name: Name of the deployment script.
        :type script_name: str
        :param tail: The number of lines to show from the tail of the deployment script log. Valid
         value is a positive number up to 1000. If 'tail' is not provided, all available logs are shown
         up to container instance log capacity of 4mb.
        :type tail: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ScriptLog or the result of cls(response)
        :rtype: ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptLog
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ScriptLog"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01-preview"

        # Construct URL
        url = self.get_logs_default.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'scriptName': self._serialize.url("script_name", script_name, 'str', max_length=90, min_length=1),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if tail is not None:
            query_parameters['tail'] = self._serialize.query("tail", tail, 'int')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DeploymentScriptsError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ScriptLog', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_logs_default.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}/logs/default'}  # type: ignore

    def list_by_resource_group(
        self,
        resource_group_name: str,
        **kwargs
    ) -> AsyncIterable["models.DeploymentScriptListResult"]:
        """Lists deployments scripts.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of DeploymentScriptListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.DeploymentScriptListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DeploymentScriptListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-10-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('DeploymentScriptListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.DeploymentScriptsError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts'}  # type: ignore