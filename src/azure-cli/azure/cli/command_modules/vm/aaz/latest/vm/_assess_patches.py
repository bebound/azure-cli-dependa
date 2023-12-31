# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "vm assess-patches",
)
class AssessPatches(AAZCommand):
    """Assess patches on a VM.

    :example: Assess patches on a VM.
        az vm assess-patches -g MyResourceGroup -n MyVm
    """

    _aaz_info = {
        "version": "2022-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/virtualmachines/{}/assesspatches", "2022-11-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.vm_name = AAZStrArg(
            options=["-n", "--name", "--vm-name"],
            help="The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`",
            required=True,
            id_part="name",
            configured_default="vm",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.VirtualMachinesAssessPatches(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class VirtualMachinesAssessPatches(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/assessPatches",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "vmName", self.ctx.args.vm_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.assessment_activity_id = AAZStrType(
                serialized_name="assessmentActivityId",
                flags={"read_only": True},
            )
            _schema_on_200.available_patches = AAZListType(
                serialized_name="availablePatches",
                flags={"read_only": True},
            )
            _schema_on_200.critical_and_security_patch_count = AAZIntType(
                serialized_name="criticalAndSecurityPatchCount",
                flags={"read_only": True},
            )
            _schema_on_200.error = AAZObjectType()
            _AssessPatchesHelper._build_schema_api_error_read(_schema_on_200.error)
            _schema_on_200.other_patch_count = AAZIntType(
                serialized_name="otherPatchCount",
                flags={"read_only": True},
            )
            _schema_on_200.reboot_pending = AAZBoolType(
                serialized_name="rebootPending",
                flags={"read_only": True},
            )
            _schema_on_200.start_date_time = AAZStrType(
                serialized_name="startDateTime",
                flags={"read_only": True},
            )
            _schema_on_200.status = AAZStrType(
                flags={"read_only": True},
            )

            available_patches = cls._schema_on_200.available_patches
            available_patches.Element = AAZObjectType()

            _element = cls._schema_on_200.available_patches.Element
            _element.activity_id = AAZStrType(
                serialized_name="activityId",
                flags={"read_only": True},
            )
            _element.assessment_state = AAZStrType(
                serialized_name="assessmentState",
                flags={"read_only": True},
            )
            _element.classifications = AAZListType(
                flags={"read_only": True},
            )
            _element.kb_id = AAZStrType(
                serialized_name="kbId",
                flags={"read_only": True},
            )
            _element.last_modified_date_time = AAZStrType(
                serialized_name="lastModifiedDateTime",
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.patch_id = AAZStrType(
                serialized_name="patchId",
                flags={"read_only": True},
            )
            _element.published_date = AAZStrType(
                serialized_name="publishedDate",
                flags={"read_only": True},
            )
            _element.reboot_behavior = AAZStrType(
                serialized_name="rebootBehavior",
                flags={"read_only": True},
            )
            _element.version = AAZStrType(
                flags={"read_only": True},
            )

            classifications = cls._schema_on_200.available_patches.Element.classifications
            classifications.Element = AAZStrType()

            return cls._schema_on_200


class _AssessPatchesHelper:
    """Helper class for AssessPatches"""

    _schema_api_error_read = None

    @classmethod
    def _build_schema_api_error_read(cls, _schema):
        if cls._schema_api_error_read is not None:
            _schema.code = cls._schema_api_error_read.code
            _schema.details = cls._schema_api_error_read.details
            _schema.innererror = cls._schema_api_error_read.innererror
            _schema.message = cls._schema_api_error_read.message
            _schema.target = cls._schema_api_error_read.target
            return

        cls._schema_api_error_read = _schema_api_error_read = AAZObjectType()

        api_error_read = _schema_api_error_read
        api_error_read.code = AAZStrType()
        api_error_read.details = AAZListType()
        api_error_read.innererror = AAZObjectType()
        api_error_read.message = AAZStrType()
        api_error_read.target = AAZStrType()

        details = _schema_api_error_read.details
        details.Element = AAZObjectType()

        _element = _schema_api_error_read.details.Element
        _element.code = AAZStrType()
        _element.message = AAZStrType()
        _element.target = AAZStrType()

        innererror = _schema_api_error_read.innererror
        innererror.errordetail = AAZStrType()
        innererror.exceptiontype = AAZStrType()

        _schema.code = cls._schema_api_error_read.code
        _schema.details = cls._schema_api_error_read.details
        _schema.innererror = cls._schema_api_error_read.innererror
        _schema.message = cls._schema_api_error_read.message
        _schema.target = cls._schema_api_error_read.target


__all__ = ["AssessPatches"]
