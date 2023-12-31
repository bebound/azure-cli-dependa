# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def load_command_table(self, _):

    with self.command_group('') as g:
        g.custom_command('rest', 'rest_call')

    with self.command_group('') as g:
        g.custom_command('version', 'show_version')

    with self.command_group('') as g:
        g.custom_command('upgrade', 'upgrade_version', is_preview=True)

    with self.command_group('demo', deprecate_info=g.deprecate(hide=True)) as g:
        g.custom_command('style', 'demo_style')
        g.custom_command('byo-access-token', 'byo_access_token')

    with self.command_group('demo secret-store') as g:
        g.custom_command('save', 'secret_store_save')
        g.custom_command('load', 'secret_store_load')
