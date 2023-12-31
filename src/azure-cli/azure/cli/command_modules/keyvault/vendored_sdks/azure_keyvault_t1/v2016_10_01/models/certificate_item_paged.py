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
from msrest.paging import Paged


class CertificateItemPaged(Paged):
    """
    A paging container for iterating over a list of :class:`CertificateItem <azure.keyvault.v2016_10_01.models.CertificateItem>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CertificateItem]'}
    }

    def __init__(self, *args, **kwargs):

        super(CertificateItemPaged, self).__init__(*args, **kwargs)
