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


class CertificateItem(Model):
    """The certificate item containing certificate metadata.

    :param id: Certificate identifier.
    :type id: str
    :param attributes: The certificate management attributes.
    :type attributes: ~azure.keyvault.v2016_10_01.models.CertificateAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    :param x509_thumbprint: Thumbprint of the certificate.
    :type x509_thumbprint: bytes
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'CertificateAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'x509_thumbprint': {'key': 'x5t', 'type': 'base64'},
    }

    def __init__(self, **kwargs):
        super(CertificateItem, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.attributes = kwargs.get('attributes', None)
        self.tags = kwargs.get('tags', None)
        self.x509_thumbprint = kwargs.get('x509_thumbprint', None)
