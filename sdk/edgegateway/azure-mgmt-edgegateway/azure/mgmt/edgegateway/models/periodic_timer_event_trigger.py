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

from .trigger import Trigger


class PeriodicTimerEventTrigger(Trigger):
    """Trigger details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The path ID that uniquely identifies the object.
    :vartype id: str
    :ivar name: The object name.
    :vartype name: str
    :ivar type: The hierarchical type of the object.
    :vartype type: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param source_info: Required. Periodic timer details.
    :type source_info: ~azure.mgmt.edgegateway.models.PeriodicTimerSourceInfo
    :param sink_info: Required. Role Sink information.
    :type sink_info: ~azure.mgmt.edgegateway.models.RoleSinkInfo
    :param custom_context_tag: A custom context tag typically used to
     correlate the trigger against its usage. For example, if a periodic timer
     trigger is intended for certain specific IoT modules in the device, the
     tag can be the name or the image URL of the module.
    :type custom_context_tag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'required': True},
        'source_info': {'required': True},
        'sink_info': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'source_info': {'key': 'properties.sourceInfo', 'type': 'PeriodicTimerSourceInfo'},
        'sink_info': {'key': 'properties.sinkInfo', 'type': 'RoleSinkInfo'},
        'custom_context_tag': {'key': 'properties.customContextTag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PeriodicTimerEventTrigger, self).__init__(**kwargs)
        self.source_info = kwargs.get('source_info', None)
        self.sink_info = kwargs.get('sink_info', None)
        self.custom_context_tag = kwargs.get('custom_context_tag', None)
        self.kind = 'PeriodicTimerEvent'
