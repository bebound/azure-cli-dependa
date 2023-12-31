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


class KeyBundle(Model):
    """A KeyBundle consisting of a WebKey plus its attributes.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param key: The Json web key.
    :type key: ~azure.keyvault.v2016_10_01.models.JsonWebKey
    :param attributes: The key management attributes.
    :type attributes: ~azure.keyvault.v2016_10_01.models.KeyAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    :ivar managed: True if the key's lifetime is managed by key vault. If this
     is a key backing a certificate, then managed will be true.
    :vartype managed: bool
    """

    _validation = {
        'managed': {'readonly': True},
    }

    _attribute_map = {
        'key': {'key': 'key', 'type': 'JsonWebKey'},
        'attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed': {'key': 'managed', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(KeyBundle, self).__init__(**kwargs)
        self.key = kwargs.get('key', None)
        self.attributes = kwargs.get('attributes', None)
        self.tags = kwargs.get('tags', None)
        self.managed = None
