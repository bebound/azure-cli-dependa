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
# pylint: skip-file
# flake8: noqa
from msrest.serialization import Model


class StorageBundle(Model):
    """A Storage account bundle consists of key vault storage account details plus
    its attributes.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The storage account id.
    :vartype id: str
    :ivar resource_id: The storage account resource id.
    :vartype resource_id: str
    :ivar active_key_name: The current active storage account key name.
    :vartype active_key_name: str
    :ivar auto_regenerate_key: whether keyvault should manage the storage
     account for the user.
    :vartype auto_regenerate_key: bool
    :ivar regeneration_period: The key regeneration time duration specified in
     ISO-8601 format.
    :vartype regeneration_period: str
    :ivar attributes: The storage account attributes.
    :vartype attributes: ~azure.keyvault.v7_0.models.StorageAccountAttributes
    :ivar tags: Application specific metadata in the form of key-value pairs
    :vartype tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'resource_id': {'readonly': True},
        'active_key_name': {'readonly': True},
        'auto_regenerate_key': {'readonly': True},
        'regeneration_period': {'readonly': True},
        'attributes': {'readonly': True},
        'tags': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'active_key_name': {'key': 'activeKeyName', 'type': 'str'},
        'auto_regenerate_key': {'key': 'autoRegenerateKey', 'type': 'bool'},
        'regeneration_period': {'key': 'regenerationPeriod', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'StorageAccountAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(StorageBundle, self).__init__(**kwargs)
        self.id = None
        self.resource_id = None
        self.active_key_name = None
        self.auto_regenerate_key = None
        self.regeneration_period = None
        self.attributes = None
        self.tags = None
