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


class SasDefinitionItem(Model):
    """The SAS definition item containing storage SAS definition metadata.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The storage SAS identifier.
    :vartype id: str
    :ivar secret_id: The storage account SAS definition secret id.
    :vartype secret_id: str
    :ivar attributes: The SAS definition management attributes.
    :vartype attributes: ~azure.keyvault.v7_0.models.SasDefinitionAttributes
    :ivar tags: Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'secret_id': {'readonly': True},
        'attributes': {'readonly': True},
        'tags': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'secret_id': {'key': 'sid', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'SasDefinitionAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(SasDefinitionItem, self).__init__(**kwargs)
        self.id = None
        self.secret_id = None
        self.attributes = None
        self.tags = None
