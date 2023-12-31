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


class AdministratorDetails(Model):
    """Details of the organization administrator of the certificate issuer.

    :param first_name: First name.
    :type first_name: str
    :param last_name: Last name.
    :type last_name: str
    :param email_address: Email addresss.
    :type email_address: str
    :param phone: Phone number.
    :type phone: str
    """

    _attribute_map = {
        'first_name': {'key': 'first_name', 'type': 'str'},
        'last_name': {'key': 'last_name', 'type': 'str'},
        'email_address': {'key': 'email', 'type': 'str'},
        'phone': {'key': 'phone', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AdministratorDetails, self).__init__(**kwargs)
        self.first_name = kwargs.get('first_name', None)
        self.last_name = kwargs.get('last_name', None)
        self.email_address = kwargs.get('email_address', None)
        self.phone = kwargs.get('phone', None)
