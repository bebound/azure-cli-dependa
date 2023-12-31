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
    "network profile",
)
class __CMDGroup(AAZCommandGroup):
    """Manage network profiles.

    To create a network profile, see the create command for the relevant resource. Currently, only Azure Container Instances are supported.
    """
    pass


__all__ = ["__CMDGroup"]
