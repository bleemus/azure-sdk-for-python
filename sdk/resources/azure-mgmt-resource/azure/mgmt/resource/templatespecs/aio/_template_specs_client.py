# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import TemplateSpecsClientConfiguration

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class TemplateSpecsClient(MultiApiClientMixin, _SDKClient):
    """The APIs listed in this specification can be used to manage Template Spec resources through the Azure Resource Manager.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Subscription Id which forms part of the URI for every service call.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2019-06-01-preview'
    _PROFILE_TAG = "azure.mgmt.resource.TemplateSpecsClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "AsyncTokenCredential"
        subscription_id,  # type: str
        api_version=None,
        base_url=None,
        profile=KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = TemplateSpecsClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(TemplateSpecsClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2019-06-01-preview: :mod:`v2019_06_01_preview.models<azure.mgmt.resource.v2019_06_01_preview.models>`
        """
        if api_version == '2019-06-01-preview':
            from ..v2019_06_01_preview import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def template_spec_versions(self):
        """Instance depends on the API version:

           * 2019-06-01-preview: :class:`TemplateSpecVersionsOperations<azure.mgmt.resource.v2019_06_01_preview.aio.operations.TemplateSpecVersionsOperations>`
        """
        api_version = self._get_api_version('template_spec_versions')
        if api_version == '2019-06-01-preview':
            from ..v2019_06_01_preview.aio.operations import TemplateSpecVersionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'template_spec_versions'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def template_specs(self):
        """Instance depends on the API version:

           * 2019-06-01-preview: :class:`TemplateSpecsOperations<azure.mgmt.resource.v2019_06_01_preview.aio.operations.TemplateSpecsOperations>`
        """
        api_version = self._get_api_version('template_specs')
        if api_version == '2019-06-01-preview':
            from ..v2019_06_01_preview.aio.operations import TemplateSpecsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'template_specs'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
