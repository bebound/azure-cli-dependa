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
    "network watcher packet-capture create",
)
class Create(AAZCommand):
    """Create and start a packet capture session.

    :example: Create a packet capture session on a VM.
        az network watcher packet-capture create -g MyResourceGroup -n MyPacketCaptureName --vm MyVm --storage-account MyStorageAccount

    :example: Create a packet capture session on a VM with optional filters for protocols, local IP address and remote IP address ranges and ports.
        az network watcher packet-capture create -g MyResourceGroup -n MyPacketCaptureName --vm MyVm --storage-account MyStorageAccount --filters '[{"protocol":"TCP", "remoteIPAddress":"1.1.1.1-255.255.255", "localIPAddress":"10.0.0.3", "remotePort":"20"}, {"protocol":"TCP", "remoteIPAddress":"1.1.1.1-255.255.255", "localIPAddress":"10.0.0.3", "remotePort":"80"}, {"protocol":"TCP", "remoteIPAddress":"1.1.1.1-255.255.255", "localIPAddress":"10.0.0.3", "remotePort":"443"}, {"protocol":"UDP"}]'

    :example: Create a packet capture session on a VMSS.
        az network watcher packet-capture create -g MyResourceGroup -n MyPacketCaptureName --vm MyVmVMSS --storage-account MyStorageAccount --target-type "AzureVMSS"

    :example: Create a packet capture session on a VMSS with including particular instances.
        az network watcher packet-capture create -g MyResourceGroup -n MyPacketCaptureName --target MyVmVMSS --storage-account MyStorageAccount --target-type "AzureVMSS" --include "0" "1"

    :example: Create a packet capture session on a VMSS with excluding particular instances.
        az network watcher packet-capture create -g MyResourceGroup -n MyPacketCaptureName --vm MyVmVMSS --storage-account MyStorageAccount --target-type "AzureVMSS" --exclude "0" "1"
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkwatchers/{}/packetcaptures/{}", "2022-01-01"],
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
        _args_schema.watcher_name = AAZStrArg(
            options=["--watcher-name"],
            help="Name of the network watcher.",
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the packet capture session.",
            required=True,
        )
        _args_schema.watcher_rg = AAZResourceGroupNameArg(
            options=["--watcher-rg"],
            help="Name of the resource group the watcher is in.",
            required=True,
        )
        _args_schema.capture_size = AAZIntArg(
            options=["--capture-size"],
            help="Number of bytes captured per packet. Excess bytes are truncated.",
            default=0,
            fmt=AAZIntArgFormat(
                maximum=4294967295,
                minimum=0,
            ),
        )
        _args_schema.filters = AAZListArg(
            options=["--filters"],
            help="JSON encoded list of packet filters. Use `@{path}` to load from file.",
        )
        _args_schema.target = AAZStrArg(
            options=["--target"],
            help="Name or ID of the target resource. If `--target-type` is AzureVMSS, then `--target` is mandatory.",
            required=True,
        )
        _args_schema.target_type = AAZStrArg(
            options=["--target-type"],
            help="Resource type of target.",
            default="AzureVM",
            enum={"AzureVM": "AzureVM", "AzureVMSS": "AzureVMSS"},
        )
        _args_schema.time_limit = AAZIntArg(
            options=["--time-limit"],
            help="Maximum duration of the capture session in seconds.",
            default=18000,
            fmt=AAZIntArgFormat(
                maximum=18000,
                minimum=0,
            ),
        )
        _args_schema.capture_limit = AAZIntArg(
            options=["--capture-limit"],
            help="Maximum size in bytes of the capture output.",
            default=1073741824,
            fmt=AAZIntArgFormat(
                maximum=4294967295,
                minimum=0,
            ),
        )

        filters = cls._args_schema.filters
        filters.Element = AAZObjectArg()

        _element = cls._args_schema.filters.Element
        _element.local_ip_address = AAZStrArg(
            options=["local-ip-address"],
            help="Local IP Address to be filtered on. Notation: \"127.0.0.1\" for single address entry. \"127.0.0.1-127.0.0.255\" for range. \"127.0.0.1;127.0.0.5\"? for multiple entries. Multiple ranges not currently supported. Mixing ranges with multiple entries not currently supported. Default = null.",
        )
        _element.local_port = AAZStrArg(
            options=["local-port"],
            help="Local port to be filtered on. Notation: \"80\" for single port entry.\"80-85\" for range. \"80;443;\" for multiple entries. Multiple ranges not currently supported. Mixing ranges with multiple entries not currently supported. Default = null.",
        )
        _element.protocol = AAZStrArg(
            options=["protocol"],
            help="Protocol to be filtered on.",
            default="Any",
            enum={"Any": "Any", "TCP": "TCP", "UDP": "UDP"},
        )
        _element.remote_ip_address = AAZStrArg(
            options=["remote-ip-address"],
            help="Local IP Address to be filtered on. Notation: \"127.0.0.1\" for single address entry. \"127.0.0.1-127.0.0.255\" for range. \"127.0.0.1;127.0.0.5;\" for multiple entries. Multiple ranges not currently supported. Mixing ranges with multiple entries not currently supported. Default = null.",
        )
        _element.remote_port = AAZStrArg(
            options=["remote-port"],
            help="Remote port to be filtered on. Notation: \"80\" for single port entry.\"80-85\" for range. \"80;443;\" for multiple entries. Multiple ranges not currently supported. Mixing ranges with multiple entries not currently supported. Default = null.",
        )

        # define Arg Group "Scope"

        _args_schema = cls._args_schema
        _args_schema.exclude = AAZListArg(
            options=["--exclude"],
            arg_group="Scope",
            help="Space-separated list of VMSS instances to exclude in packet capture.",
        )
        _args_schema.include = AAZListArg(
            options=["--include"],
            arg_group="Scope",
            help="Space-separated list of VMSS instances to include in packet capture like 0 1 2.",
        )

        exclude = cls._args_schema.exclude
        exclude.Element = AAZStrArg()

        include = cls._args_schema.include
        include.Element = AAZStrArg()

        # define Arg Group "Storage"

        _args_schema = cls._args_schema
        _args_schema.file_path = AAZStrArg(
            options=["--file-path"],
            arg_group="Storage",
            help="Local path on the targeted VM at which to save the packet capture. For Linux VMs, the path must start with `/var/captures`.",
        )
        _args_schema.storage_account = AAZStrArg(
            options=["--storage-account"],
            arg_group="Storage",
            help="Name or ID of a storage account to save the packet capture to.",
        )
        _args_schema.storage_path = AAZStrArg(
            options=["--storage-path"],
            arg_group="Storage",
            help="Fully qualified URI of an existing storage container in which to store the capture file. If not specified, the container `network-watcher-logs` will be created if it does not exist and the capture file will be stored there.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.PacketCapturesCreate(ctx=self.ctx)()
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

    class PacketCapturesCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkWatcherName", self.ctx.args.watcher_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "packetCaptureName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.watcher_rg,
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
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("bytesToCapturePerPacket", AAZIntType, ".capture_size")
                properties.set_prop("filters", AAZListType, ".filters")
                properties.set_prop("scope", AAZObjectType)
                properties.set_prop("storageLocation", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("target", AAZStrType, ".target", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("targetType", AAZStrType, ".target_type")
                properties.set_prop("timeLimitInSeconds", AAZIntType, ".time_limit")
                properties.set_prop("totalBytesPerSession", AAZIntType, ".capture_limit")

            filters = _builder.get(".properties.filters")
            if filters is not None:
                filters.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.filters[]")
            if _elements is not None:
                _elements.set_prop("localIPAddress", AAZStrType, ".local_ip_address")
                _elements.set_prop("localPort", AAZStrType, ".local_port")
                _elements.set_prop("protocol", AAZStrType, ".protocol")
                _elements.set_prop("remoteIPAddress", AAZStrType, ".remote_ip_address")
                _elements.set_prop("remotePort", AAZStrType, ".remote_port")

            scope = _builder.get(".properties.scope")
            if scope is not None:
                scope.set_prop("exclude", AAZListType, ".exclude")
                scope.set_prop("include", AAZListType, ".include")

            exclude = _builder.get(".properties.scope.exclude")
            if exclude is not None:
                exclude.set_elements(AAZStrType, ".")

            include = _builder.get(".properties.scope.include")
            if include is not None:
                include.set_elements(AAZStrType, ".")

            storage_location = _builder.get(".properties.storageLocation")
            if storage_location is not None:
                storage_location.set_prop("filePath", AAZStrType, ".file_path")
                storage_location.set_prop("storageId", AAZStrType, ".storage_account")
                storage_location.set_prop("storagePath", AAZStrType, ".storage_path")

            return self.serialize_content(_content_value)

        def on_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_201
            )

        _schema_on_201 = None

        @classmethod
        def _build_schema_on_201(cls):
            if cls._schema_on_201 is not None:
                return cls._schema_on_201

            cls._schema_on_201 = AAZObjectType()

            _schema_on_201 = cls._schema_on_201
            _schema_on_201.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_201.properties
            properties.bytes_to_capture_per_packet = AAZIntType(
                serialized_name="bytesToCapturePerPacket",
            )
            properties.filters = AAZListType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.scope = AAZObjectType()
            properties.storage_location = AAZObjectType(
                serialized_name="storageLocation",
                flags={"required": True},
            )
            properties.target = AAZStrType(
                flags={"required": True},
            )
            properties.target_type = AAZStrType(
                serialized_name="targetType",
            )
            properties.time_limit_in_seconds = AAZIntType(
                serialized_name="timeLimitInSeconds",
            )
            properties.total_bytes_per_session = AAZIntType(
                serialized_name="totalBytesPerSession",
            )

            filters = cls._schema_on_201.properties.filters
            filters.Element = AAZObjectType()

            _element = cls._schema_on_201.properties.filters.Element
            _element.local_ip_address = AAZStrType(
                serialized_name="localIPAddress",
            )
            _element.local_port = AAZStrType(
                serialized_name="localPort",
            )
            _element.protocol = AAZStrType()
            _element.remote_ip_address = AAZStrType(
                serialized_name="remoteIPAddress",
            )
            _element.remote_port = AAZStrType(
                serialized_name="remotePort",
            )

            scope = cls._schema_on_201.properties.scope
            scope.exclude = AAZListType()
            scope.include = AAZListType()

            exclude = cls._schema_on_201.properties.scope.exclude
            exclude.Element = AAZStrType()

            include = cls._schema_on_201.properties.scope.include
            include.Element = AAZStrType()

            storage_location = cls._schema_on_201.properties.storage_location
            storage_location.file_path = AAZStrType(
                serialized_name="filePath",
            )
            storage_location.storage_id = AAZStrType(
                serialized_name="storageId",
            )
            storage_location.storage_path = AAZStrType(
                serialized_name="storagePath",
            )

            return cls._schema_on_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
