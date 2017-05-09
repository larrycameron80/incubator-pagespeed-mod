# gyp file for grpc, originally based on binding.gyp from the git repo.
{
  'target_defaults': {
    'include_dirs': [
      'src',
      'src/include',
    ],
    # Clients need to inherit the grpc includes.
    'all_dependent_settings': {
      'include_dirs': [ 'src/include', ],
    },
  },
  'targets': [
    {
      'target_name': 'grpc_cpp',
      'type': 'static_library',
      'dependencies': [
        ':grpc_core',
        ':gpr',
        '<(DEPTH)/third_party/protobuf/protobuf.gyp:protobuf_lite',
      ],
      'cflags_cc': [
        '-Wall',
        '-pthread',
        '-zdefs',
        '-Wno-error=deprecated-declarations'
      ],
      'sources': [
        'src/src/cpp/client/insecure_credentials.cc',
        'src/src/cpp/client/secure_credentials.cc',
        'src/src/cpp/common/auth_property_iterator.cc',
        'src/src/cpp/common/secure_auth_context.cc',
        'src/src/cpp/common/secure_channel_arguments.cc',
        'src/src/cpp/common/secure_create_auth_context.cc',
        'src/src/cpp/server/insecure_server_credentials.cc',
        'src/src/cpp/server/secure_server_credentials.cc',
        'src/src/cpp/client/channel_cc.cc',
        'src/src/cpp/client/client_context.cc',
        'src/src/cpp/client/create_channel.cc',
        'src/src/cpp/client/create_channel_internal.cc',
        'src/src/cpp/client/create_channel_posix.cc',
        'src/src/cpp/client/credentials_cc.cc',
        'src/src/cpp/client/generic_stub.cc',
        'src/src/cpp/common/channel_arguments.cc',
        'src/src/cpp/common/channel_filter.cc',
        'src/src/cpp/common/completion_queue_cc.cc',
        'src/src/cpp/common/core_codegen.cc',
        'src/src/cpp/common/resource_quota_cc.cc',
        'src/src/cpp/common/rpc_method.cc',
        'src/src/cpp/common/version_cc.cc',
        'src/src/cpp/server/async_generic_service.cc',
        'src/src/cpp/server/create_default_thread_pool.cc',
        'src/src/cpp/server/dynamic_thread_pool.cc',
        'src/src/cpp/server/health/default_health_check_service.cc',
        'src/src/cpp/server/health/health.pb.c',
        'src/src/cpp/server/health/health_check_service.cc',
        'src/src/cpp/server/health/health_check_service_server_builder_option.cc',
        'src/src/cpp/server/server_builder.cc',
        'src/src/cpp/server/server_cc.cc',
        'src/src/cpp/server/server_context.cc',
        'src/src/cpp/server/server_credentials.cc',
        'src/src/cpp/server/server_posix.cc',
        'src/src/cpp/thread_manager/thread_manager.cc',
        'src/src/cpp/util/byte_buffer_cc.cc',
        'src/src/cpp/util/slice_cc.cc',
        'src/src/cpp/util/status.cc',
        'src/src/cpp/util/string_ref.cc',
        'src/src/cpp/util/time_cc.cc',
        'src/src/cpp/codegen/codegen_init.cc',
      ],
    },
    {
      'target_name': 'grpc_core',
      'type': 'static_library',
      'dependencies': [
        ':gpr',
        '<(DEPTH)/third_party/serf/select_openssl.gyp:select_openssl',
      ],
      'cflags': [
        '-std=c99',
        '-Wall',
      ],
      'ldflags': [
        '-Wl,-wrap,memcpy',
      ],
      'sources': [
        'src/src/core/lib/surface/init.c',
        'src/src/core/lib/channel/channel_args.c',
        'src/src/core/lib/channel/channel_stack.c',
        'src/src/core/lib/channel/channel_stack_builder.c',
        'src/src/core/lib/channel/compress_filter.c',
        'src/src/core/lib/channel/connected_channel.c',
        'src/src/core/lib/channel/deadline_filter.c',
        'src/src/core/lib/channel/handshaker.c',
        'src/src/core/lib/channel/handshaker_factory.c',
        'src/src/core/lib/channel/handshaker_registry.c',
        'src/src/core/lib/channel/http_client_filter.c',
        'src/src/core/lib/channel/http_server_filter.c',
        'src/src/core/lib/channel/message_size_filter.c',
        'src/src/core/lib/compression/compression.c',
        'src/src/core/lib/compression/message_compress.c',
        'src/src/core/lib/debug/trace.c',
        'src/src/core/lib/http/format_request.c',
        'src/src/core/lib/http/httpcli.c',
        'src/src/core/lib/http/parser.c',
        'src/src/core/lib/iomgr/closure.c',
        'src/src/core/lib/iomgr/combiner.c',
        'src/src/core/lib/iomgr/endpoint.c',
        'src/src/core/lib/iomgr/endpoint_pair_posix.c',
        'src/src/core/lib/iomgr/endpoint_pair_uv.c',
        'src/src/core/lib/iomgr/endpoint_pair_windows.c',
        'src/src/core/lib/iomgr/error.c',
        'src/src/core/lib/iomgr/ev_epoll_linux.c',
        'src/src/core/lib/iomgr/ev_poll_posix.c',
        'src/src/core/lib/iomgr/ev_posix.c',
        'src/src/core/lib/iomgr/exec_ctx.c',
        'src/src/core/lib/iomgr/executor.c',
        'src/src/core/lib/iomgr/iocp_windows.c',
        'src/src/core/lib/iomgr/iomgr.c',
        'src/src/core/lib/iomgr/iomgr_posix.c',
        'src/src/core/lib/iomgr/iomgr_uv.c',
        'src/src/core/lib/iomgr/iomgr_windows.c',
        'src/src/core/lib/iomgr/load_file.c',
        'src/src/core/lib/iomgr/network_status_tracker.c',
        'src/src/core/lib/iomgr/polling_entity.c',
        'src/src/core/lib/iomgr/pollset_set_uv.c',
        'src/src/core/lib/iomgr/pollset_set_windows.c',
        'src/src/core/lib/iomgr/pollset_uv.c',
        'src/src/core/lib/iomgr/pollset_windows.c',
        'src/src/core/lib/iomgr/resolve_address_posix.c',
        'src/src/core/lib/iomgr/resolve_address_uv.c',
        'src/src/core/lib/iomgr/resolve_address_windows.c',
        'src/src/core/lib/iomgr/resource_quota.c',
        'src/src/core/lib/iomgr/sockaddr_utils.c',
        'src/src/core/lib/iomgr/socket_mutator.c',
        'src/src/core/lib/iomgr/socket_utils_common_posix.c',
        'src/src/core/lib/iomgr/socket_utils_linux.c',
        'src/src/core/lib/iomgr/socket_utils_posix.c',
        'src/src/core/lib/iomgr/socket_utils_uv.c',
        'src/src/core/lib/iomgr/socket_utils_windows.c',
        'src/src/core/lib/iomgr/socket_windows.c',
        'src/src/core/lib/iomgr/tcp_client_posix.c',
        'src/src/core/lib/iomgr/tcp_client_uv.c',
        'src/src/core/lib/iomgr/tcp_client_windows.c',
        'src/src/core/lib/iomgr/tcp_posix.c',
        'src/src/core/lib/iomgr/tcp_server_posix.c',
        'src/src/core/lib/iomgr/tcp_server_uv.c',
        'src/src/core/lib/iomgr/tcp_server_windows.c',
        'src/src/core/lib/iomgr/tcp_uv.c',
        'src/src/core/lib/iomgr/tcp_windows.c',
        'src/src/core/lib/iomgr/time_averaged_stats.c',
        'src/src/core/lib/iomgr/timer_generic.c',
        'src/src/core/lib/iomgr/timer_heap.c',
        'src/src/core/lib/iomgr/timer_uv.c',
        'src/src/core/lib/iomgr/udp_server.c',
        'src/src/core/lib/iomgr/unix_sockets_posix.c',
        'src/src/core/lib/iomgr/unix_sockets_posix_noop.c',
        'src/src/core/lib/iomgr/wakeup_fd_cv.c',
        'src/src/core/lib/iomgr/wakeup_fd_eventfd.c',
        'src/src/core/lib/iomgr/wakeup_fd_nospecial.c',
        'src/src/core/lib/iomgr/wakeup_fd_pipe.c',
        'src/src/core/lib/iomgr/wakeup_fd_posix.c',
        'src/src/core/lib/iomgr/workqueue_uv.c',
        'src/src/core/lib/iomgr/workqueue_windows.c',
        'src/src/core/lib/json/json.c',
        'src/src/core/lib/json/json_reader.c',
        'src/src/core/lib/json/json_string.c',
        'src/src/core/lib/json/json_writer.c',
        'src/src/core/lib/slice/percent_encoding.c',
        'src/src/core/lib/slice/slice.c',
        'src/src/core/lib/slice/slice_buffer.c',
        'src/src/core/lib/slice/slice_hash_table.c',
        'src/src/core/lib/slice/slice_intern.c',
        'src/src/core/lib/slice/slice_string_helpers.c',
        'src/src/core/lib/surface/alarm.c',
        'src/src/core/lib/surface/api_trace.c',
        'src/src/core/lib/surface/byte_buffer.c',
        'src/src/core/lib/surface/byte_buffer_reader.c',
        'src/src/core/lib/surface/call.c',
        'src/src/core/lib/surface/call_details.c',
        'src/src/core/lib/surface/call_log_batch.c',
        'src/src/core/lib/surface/channel.c',
        'src/src/core/lib/surface/channel_init.c',
        'src/src/core/lib/surface/channel_ping.c',
        'src/src/core/lib/surface/channel_stack_type.c',
        'src/src/core/lib/surface/completion_queue.c',
        'src/src/core/lib/surface/event_string.c',
        'src/src/core/lib/surface/lame_client.c',
        'src/src/core/lib/surface/metadata_array.c',
        'src/src/core/lib/surface/server.c',
        'src/src/core/lib/surface/validate_metadata.c',
        'src/src/core/lib/surface/version.c',
        'src/src/core/lib/transport/bdp_estimator.c',
        'src/src/core/lib/transport/byte_stream.c',
        'src/src/core/lib/transport/connectivity_state.c',
        'src/src/core/lib/transport/error_utils.c',
        'src/src/core/lib/transport/metadata.c',
        'src/src/core/lib/transport/metadata_batch.c',
        'src/src/core/lib/transport/pid_controller.c',
        'src/src/core/lib/transport/service_config.c',
        'src/src/core/lib/transport/static_metadata.c',
        'src/src/core/lib/transport/status_conversion.c',
        'src/src/core/lib/transport/timeout_encoding.c',
        'src/src/core/lib/transport/transport.c',
        'src/src/core/lib/transport/transport_op_string.c',
        'src/src/core/ext/transport/chttp2/server/secure/server_secure_chttp2.c',
        'src/src/core/ext/transport/chttp2/transport/bin_decoder.c',
        'src/src/core/ext/transport/chttp2/transport/bin_encoder.c',
        'src/src/core/ext/transport/chttp2/transport/chttp2_plugin.c',
        'src/src/core/ext/transport/chttp2/transport/chttp2_transport.c',
        'src/src/core/ext/transport/chttp2/transport/frame_data.c',
        'src/src/core/ext/transport/chttp2/transport/frame_goaway.c',
        'src/src/core/ext/transport/chttp2/transport/frame_ping.c',
        'src/src/core/ext/transport/chttp2/transport/frame_rst_stream.c',
        'src/src/core/ext/transport/chttp2/transport/frame_settings.c',
        'src/src/core/ext/transport/chttp2/transport/frame_window_update.c',
        'src/src/core/ext/transport/chttp2/transport/hpack_encoder.c',
        'src/src/core/ext/transport/chttp2/transport/hpack_parser.c',
        'src/src/core/ext/transport/chttp2/transport/hpack_table.c',
        'src/src/core/ext/transport/chttp2/transport/huffsyms.c',
        'src/src/core/ext/transport/chttp2/transport/incoming_metadata.c',
        'src/src/core/ext/transport/chttp2/transport/parsing.c',
        'src/src/core/ext/transport/chttp2/transport/stream_lists.c',
        'src/src/core/ext/transport/chttp2/transport/stream_map.c',
        'src/src/core/ext/transport/chttp2/transport/varint.c',
        'src/src/core/ext/transport/chttp2/transport/writing.c',
        'src/src/core/ext/transport/chttp2/alpn/alpn.c',
        'src/src/core/lib/http/httpcli_security_connector.c',
        'src/src/core/lib/security/context/security_context.c',
        'src/src/core/lib/security/credentials/composite/composite_credentials.c',
        'src/src/core/lib/security/credentials/credentials.c',
        'src/src/core/lib/security/credentials/credentials_metadata.c',
        'src/src/core/lib/security/credentials/fake/fake_credentials.c',
        'src/src/core/lib/security/credentials/google_default/credentials_generic.c',
        'src/src/core/lib/security/credentials/google_default/google_default_credentials.c',
        'src/src/core/lib/security/credentials/iam/iam_credentials.c',
        'src/src/core/lib/security/credentials/jwt/json_token.c',
        'src/src/core/lib/security/credentials/jwt/jwt_credentials.c',
        'src/src/core/lib/security/credentials/jwt/jwt_verifier.c',
        'src/src/core/lib/security/credentials/oauth2/oauth2_credentials.c',
        'src/src/core/lib/security/credentials/plugin/plugin_credentials.c',
        'src/src/core/lib/security/credentials/ssl/ssl_credentials.c',
        'src/src/core/lib/security/transport/client_auth_filter.c',
        'src/src/core/lib/security/transport/lb_targets_info.c',
        'src/src/core/lib/security/transport/secure_endpoint.c',
        'src/src/core/lib/security/transport/security_connector.c',
        'src/src/core/lib/security/transport/security_handshaker.c',
        'src/src/core/lib/security/transport/server_auth_filter.c',
        'src/src/core/lib/security/transport/tsi_error.c',
        'src/src/core/lib/security/util/b64.c',
        'src/src/core/lib/security/util/json_util.c',
        'src/src/core/lib/surface/init_secure.c',
        'src/src/core/lib/tsi/fake_transport_security.c',
        'src/src/core/lib/tsi/ssl_transport_security.c',
        'src/src/core/lib/tsi/transport_security.c',
        'src/src/core/ext/transport/chttp2/server/chttp2_server.c',
        'src/src/core/ext/transport/chttp2/client/secure/secure_channel_create.c',
        'src/src/core/ext/client_channel/channel_connectivity.c',
        'src/src/core/ext/client_channel/client_channel.c',
        'src/src/core/ext/client_channel/client_channel_factory.c',
        'src/src/core/ext/client_channel/client_channel_plugin.c',
        'src/src/core/ext/client_channel/connector.c',
        'src/src/core/ext/client_channel/default_initial_connect_string.c',
        'src/src/core/ext/client_channel/http_connect_handshaker.c',
        'src/src/core/ext/client_channel/http_proxy.c',
        'src/src/core/ext/client_channel/initial_connect_string.c',
        'src/src/core/ext/client_channel/lb_policy.c',
        'src/src/core/ext/client_channel/lb_policy_factory.c',
        'src/src/core/ext/client_channel/lb_policy_registry.c',
        'src/src/core/ext/client_channel/parse_address.c',
        'src/src/core/ext/client_channel/proxy_mapper.c',
        'src/src/core/ext/client_channel/proxy_mapper_registry.c',
        'src/src/core/ext/client_channel/resolver.c',
        'src/src/core/ext/client_channel/resolver_factory.c',
        'src/src/core/ext/client_channel/resolver_registry.c',
        'src/src/core/ext/client_channel/subchannel.c',
        'src/src/core/ext/client_channel/subchannel_index.c',
        'src/src/core/ext/client_channel/uri_parser.c',
        'src/src/core/ext/transport/chttp2/client/chttp2_connector.c',
        'src/src/core/ext/transport/chttp2/server/insecure/server_chttp2.c',
        'src/src/core/ext/transport/chttp2/server/insecure/server_chttp2_posix.c',
        'src/src/core/ext/transport/chttp2/client/insecure/channel_create.c',
        'src/src/core/ext/transport/chttp2/client/insecure/channel_create_posix.c',
        'src/src/core/ext/lb_policy/grpclb/grpclb.c',
        'src/src/core/ext/lb_policy/grpclb/grpclb_channel_secure.c',
        'src/src/core/ext/lb_policy/grpclb/load_balancer_api.c',
        'src/src/core/ext/lb_policy/grpclb/proto/grpc/lb/v1/load_balancer.pb.c',
        'src/third_party/nanopb/pb_common.c',
        'src/third_party/nanopb/pb_decode.c',
        'src/third_party/nanopb/pb_encode.c',
        'src/src/core/ext/lb_policy/pick_first/pick_first.c',
        'src/src/core/ext/lb_policy/round_robin/round_robin.c',
        'src/src/core/ext/resolver/dns/native/dns_resolver.c',
        'src/src/core/ext/resolver/sockaddr/sockaddr_resolver.c',
        'src/src/core/ext/load_reporting/load_reporting.c',
        'src/src/core/ext/load_reporting/load_reporting_filter.c',
        'src/src/core/ext/census/base_resources.c',
        'src/src/core/ext/census/context.c',
        'src/src/core/ext/census/gen/census.pb.c',
        'src/src/core/ext/census/gen/trace_context.pb.c',
        'src/src/core/ext/census/grpc_context.c',
        'src/src/core/ext/census/grpc_filter.c',
        'src/src/core/ext/census/grpc_plugin.c',
        'src/src/core/ext/census/initialize.c',
        'src/src/core/ext/census/mlog.c',
        'src/src/core/ext/census/operation.c',
        'src/src/core/ext/census/placeholders.c',
        'src/src/core/ext/census/resource.c',
        'src/src/core/ext/census/trace_context.c',
        'src/src/core/ext/census/tracing.c',
        'src/src/core/plugin_registry/grpc_plugin_registry.c',
      ],
    },
    {
      'target_name': 'gpr',
      'type': 'static_library',
      'cflags': [
        '-std=c99',
        '-Wall',
      ],
      'sources': [
        'src/src/core/lib/profiling/basic_timers.c',
        'src/src/core/lib/profiling/stap_timers.c',
        'src/src/core/lib/support/alloc.c',
        'src/src/core/lib/support/avl.c',
        'src/src/core/lib/support/backoff.c',
        'src/src/core/lib/support/cmdline.c',
        'src/src/core/lib/support/cpu_iphone.c',
        'src/src/core/lib/support/cpu_linux.c',
        'src/src/core/lib/support/cpu_posix.c',
        'src/src/core/lib/support/cpu_windows.c',
        'src/src/core/lib/support/env_linux.c',
        'src/src/core/lib/support/env_posix.c',
        'src/src/core/lib/support/env_windows.c',
        'src/src/core/lib/support/histogram.c',
        'src/src/core/lib/support/host_port.c',
        'src/src/core/lib/support/log.c',
        'src/src/core/lib/support/log_android.c',
        'src/src/core/lib/support/log_linux.c',
        'src/src/core/lib/support/log_posix.c',
        'src/src/core/lib/support/log_windows.c',
        'src/src/core/lib/support/mpscq.c',
        'src/src/core/lib/support/murmur_hash.c',
        'src/src/core/lib/support/stack_lockfree.c',
        'src/src/core/lib/support/string.c',
        'src/src/core/lib/support/string_posix.c',
        'src/src/core/lib/support/string_util_windows.c',
        'src/src/core/lib/support/string_windows.c',
        'src/src/core/lib/support/subprocess_posix.c',
        'src/src/core/lib/support/subprocess_windows.c',
        'src/src/core/lib/support/sync.c',
        'src/src/core/lib/support/sync_posix.c',
        'src/src/core/lib/support/sync_windows.c',
        'src/src/core/lib/support/thd.c',
        'src/src/core/lib/support/thd_posix.c',
        'src/src/core/lib/support/thd_windows.c',
        'src/src/core/lib/support/time.c',
        'src/src/core/lib/support/time_posix.c',
        'src/src/core/lib/support/time_precise.c',
        'src/src/core/lib/support/time_windows.c',
        'src/src/core/lib/support/tls_pthread.c',
        'src/src/core/lib/support/tmpfile_msys.c',
        'src/src/core/lib/support/tmpfile_posix.c',
        'src/src/core/lib/support/tmpfile_windows.c',
        'src/src/core/lib/support/wrap_memcpy.c',
      ],
    },
    {
      'target_name': 'grpc_cpp_plugin',
      'type': 'executable',
      'toolsets': [ 'host' ],
      'cflags_cc': [
        '-Wall',
        '-pthread',
        '-zdefs',
        '-Wno-error=deprecated-declarations'
      ],
      'sources': [
        'src/src/compiler/cpp_generator.cc',
        'src/src/compiler/cpp_plugin.cc',
      ],
      'dependencies': [
        '<(DEPTH)/third_party/protobuf/protobuf.gyp:protoc_lib',
      ],
    },
  ]
}
