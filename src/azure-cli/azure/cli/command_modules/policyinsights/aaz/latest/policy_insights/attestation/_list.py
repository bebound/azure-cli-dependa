# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *

class List(AAZCommand):
    """List all attestations for a resource.

    :example: List all policy attestations at subscription scope
        az policy attestation list

    :example: List the top two policy attestations at resource group scope
        az policy attestation list -g myRg --top 2

    :example: List all attestations that has the policy assignment id of myPolicyAssignment
        az policy attestation list --filter "PolicyAssignmentId eq '/subscriptions/35ee058e-5fa0-414c-8145-3ebb8d09b6e2/providers/microsoft.authorization/policyassignments/b101830944f246d8a14088c5'"
    """

    _aaz_info = {
        "version": "2022-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.policyinsights/attestations", "2022-09-01"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.policyinsights/attestations", "2022-09-01"],
            ["mgmt-plane", "/{resourceid}/providers/microsoft.policyinsights/attestations", "2022-09-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        _args_schema.resource_id = AAZStrArg(
            options=["--resource-id"],
            help="Resource ID.",
        )
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="OData filter expression.",
        )
        _args_schema.top = AAZIntArg(
            options=["--top"],
            help="Maximum number of records to return.",
            fmt=AAZIntArgFormat(
                minimum=0,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_id)
        condition_1 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_2 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.AttestationsListForResource(ctx=self.ctx)()
        if condition_1:
            self.AttestationsListForResourceGroup(ctx=self.ctx)()
        if condition_2:
            self.AttestationsListForSubscription(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class AttestationsListForResource(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/{resourceId}/providers/Microsoft.PolicyInsights/attestations",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceId", self.ctx.args.resource_id,
                    skip_quote=True,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "$top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "api-version", "2022-09-01",
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.assessment_date = AAZStrType(
                serialized_name="assessmentDate",
            )
            properties.comments = AAZStrType()
            properties.compliance_state = AAZStrType(
                serialized_name="complianceState",
            )
            properties.evidence = AAZListType()
            properties.expires_on = AAZStrType(
                serialized_name="expiresOn",
            )
            properties.last_compliance_state_change_at = AAZStrType(
                serialized_name="lastComplianceStateChangeAt",
                flags={"read_only": True},
            )
            properties.metadata = AAZDictType()
            properties.owner = AAZStrType()
            properties.policy_assignment_id = AAZStrType(
                serialized_name="policyAssignmentId",
                flags={"required": True},
            )
            properties.policy_definition_reference_id = AAZStrType(
                serialized_name="policyDefinitionReferenceId",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            evidence = cls._schema_on_200.value.Element.properties.evidence
            evidence.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.evidence.Element
            _element.description = AAZStrType()
            _element.source_uri = AAZStrType(
                serialized_name="sourceUri",
            )

            metadata = cls._schema_on_200.value.Element.properties.metadata
            metadata.Element = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200

    class AttestationsListForResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/attestations",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

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
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "$top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "api-version", "2022-09-01",
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.assessment_date = AAZStrType(
                serialized_name="assessmentDate",
            )
            properties.comments = AAZStrType()
            properties.compliance_state = AAZStrType(
                serialized_name="complianceState",
            )
            properties.evidence = AAZListType()
            properties.expires_on = AAZStrType(
                serialized_name="expiresOn",
            )
            properties.last_compliance_state_change_at = AAZStrType(
                serialized_name="lastComplianceStateChangeAt",
                flags={"read_only": True},
            )
            properties.metadata = AAZDictType()
            properties.owner = AAZStrType()
            properties.policy_assignment_id = AAZStrType(
                serialized_name="policyAssignmentId",
                flags={"required": True},
            )
            properties.policy_definition_reference_id = AAZStrType(
                serialized_name="policyDefinitionReferenceId",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            evidence = cls._schema_on_200.value.Element.properties.evidence
            evidence.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.evidence.Element
            _element.description = AAZStrType()
            _element.source_uri = AAZStrType(
                serialized_name="sourceUri",
            )

            metadata = cls._schema_on_200.value.Element.properties.metadata
            metadata.Element = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200

    class AttestationsListForSubscription(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/attestations",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "$top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "api-version", "2022-09-01",
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.assessment_date = AAZStrType(
                serialized_name="assessmentDate",
            )
            properties.comments = AAZStrType()
            properties.compliance_state = AAZStrType(
                serialized_name="complianceState",
            )
            properties.evidence = AAZListType()
            properties.expires_on = AAZStrType(
                serialized_name="expiresOn",
            )
            properties.last_compliance_state_change_at = AAZStrType(
                serialized_name="lastComplianceStateChangeAt",
                flags={"read_only": True},
            )
            properties.metadata = AAZDictType()
            properties.owner = AAZStrType()
            properties.policy_assignment_id = AAZStrType(
                serialized_name="policyAssignmentId",
                flags={"required": True},
            )
            properties.policy_definition_reference_id = AAZStrType(
                serialized_name="policyDefinitionReferenceId",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            evidence = cls._schema_on_200.value.Element.properties.evidence
            evidence.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.evidence.Element
            _element.description = AAZStrType()
            _element.source_uri = AAZStrType(
                serialized_name="sourceUri",
            )

            metadata = cls._schema_on_200.value.Element.properties.metadata
            metadata.Element = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
