# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "vm availability-set",
)
class __CMDGroup(AAZCommandGroup):
    """Group resources into availability sets.

    To provide redundancy to an application, it is recommended to group two or more virtual machines in an availability set. This configuration ensures that during either a planned or unplanned maintenance event, at least one virtual machine will be available.
    """
    pass


__all__ = ["__CMDGroup"]
