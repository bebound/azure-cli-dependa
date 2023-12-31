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


class CertificateRestoreParameters(Model):
    """The certificate restore parameters.

    All required parameters must be populated in order to send to Azure.

    :param certificate_bundle_backup: Required. The backup blob associated
     with a certificate bundle.
    :type certificate_bundle_backup: bytes
    """

    _validation = {
        'certificate_bundle_backup': {'required': True},
    }

    _attribute_map = {
        'certificate_bundle_backup': {'key': 'value', 'type': 'base64'},
    }

    def __init__(self, **kwargs):
        super(CertificateRestoreParameters, self).__init__(**kwargs)
        self.certificate_bundle_backup = kwargs.get('certificate_bundle_backup', None)
