from typing import Optional, Sequence

from mitmproxy import optmanager
from mitmproxy import contentviews
from mitmproxy.net import tls

log_verbosity = [
    "error",
    "warn",
    "info",
    "alert",
    "debug",
]

APP_HOST = "mitm.it"
APP_PORT = 80
CA_DIR = "~/.mitmproxy"
LISTEN_PORT = 8080

# Some help text style guidelines:
#
# - Should be a single paragraph with no linebreaks. Help will be reflowed by
# tools.
# - Avoid adding information about the data type - we can generate that.


class Options(optmanager.OptManager):

    if False:
        # This provides type hints for IDEs (e.g. PyCharm) and mypy.
        # Autogenerated using test/helper_tools/typehints_for_options.py
        add_upstream_certs_to_client_chain = None  # type: bool
        allow_remote = None  # type: bool
        anticache = None  # type: bool
        anticomp = None  # type: bool
        body_size_limit = None  # type: Optional[str]
        cadir = None  # type: str
        certs = None  # type: Sequence[str]
        ciphers_client = None  # type: Optional[str]
        ciphers_server = None  # type: Optional[str]
        client_certs = None  # type: Optional[str]
        client_replay = None  # type: Sequence[str]
        console_focus_follow = None  # type: bool
        console_layout = None  # type: str
        console_layout_headers = None  # type: bool
        console_mouse = None  # type: bool
        console_palette = None  # type: str
        console_palette_transparent = None  # type: bool
        default_contentview = None  # type: str
        flow_detail = None  # type: int
        http2 = None  # type: bool
        http2_priority = None  # type: bool
        ignore_hosts = None  # type: Sequence[str]
        intercept = None  # type: Optional[str]
        intercept_active = None  # type: bool
        keep_host_header = None  # type: bool
        keepserving = None  # type: bool
        listen_host = None  # type: str
        listen_port = None  # type: int
        mode = None  # type: str
        onboarding = None  # type: bool
        onboarding_host = None  # type: str
        onboarding_port = None  # type: int
        proxyauth = None  # type: Optional[str]
        rawtcp = None  # type: bool
        refresh_server_playback = None  # type: bool
        replacements = None  # type: Sequence[str]
        replay_kill_extra = None  # type: bool
        rfile = None  # type: Optional[str]
        save_stream_file = None  # type: Optional[str]
        save_stream_filter = None  # type: Optional[str]
        scripts = None  # type: Sequence[str]
        server = None  # type: bool
        server_replay = None  # type: Sequence[str]
        server_replay_ignore_content = None  # type: bool
        server_replay_ignore_host = None  # type: bool
        server_replay_ignore_params = None  # type: Sequence[str]
        server_replay_ignore_payload_params = None  # type: Sequence[str]
        server_replay_nopop = None  # type: bool
        server_replay_use_headers = None  # type: Sequence[str]
        setheaders = None  # type: Sequence[str]
        showhost = None  # type: bool
        spoof_source_address = None  # type: bool
        ssl_insecure = None  # type: bool
        ssl_verify_upstream_trusted_ca = None  # type: Optional[str]
        ssl_verify_upstream_trusted_cadir = None  # type: Optional[str]
        ssl_version_client = None  # type: str
        ssl_version_server = None  # type: str
        stickyauth = None  # type: Optional[str]
        stickycookie = None  # type: Optional[str]
        stream_large_bodies = None  # type: Optional[str]
        stream_websockets = None  # type: bool
        tcp_hosts = None  # type: Sequence[str]
        upstream_auth = None  # type: Optional[str]
        upstream_bind_address = None  # type: str
        upstream_cert = None  # type: bool
        verbosity = None  # type: str
        view_filter = None  # type: Optional[str]
        view_order = None  # type: str
        view_order_reversed = None  # type: bool
        web_debug = None  # type: bool
        web_iface = None  # type: str
        web_open_browser = None  # type: bool
        web_port = None  # type: int
        websocket = None  # type: bool

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.add_option(
            "onboarding", bool, True,
            "Toggle the mitmproxy onboarding app."
        )
        self.add_option(
            "onboarding_host", str, APP_HOST,
            """
            Onboarding app domain. For transparent mode, use an IP when a DNS
            entry for the app domain is not present.
            """
        )
        self.add_option(
            "onboarding_port", int, APP_PORT,
            "Port to serve the onboarding app from."
        )
        self.add_option(
            "anticache", bool, False,
            """
            Strip out request headers that might cause the server to return
            304-not-modified.
            """
        )
        self.add_option(
            "anticomp", bool, False,
            "Try to convince servers to send us un-compressed data."
        )
        self.add_option(
            "client_replay", Sequence[str], [],
            "Replay client requests from a saved file."
        )
        self.add_option(
            "replay_kill_extra", bool, False,
            "Kill extra requests during replay."
        )
        self.add_option(
            "keepserving", bool, False,
            """
            Continue serving after client playback, server playback or file
            read. This option is ignored by interactive tools, which always keep
            serving.
            """
        )
        self.add_option(
            "server", bool, True,
            "Start a proxy server. Enabled by default."
        )
        self.add_option(
            "server_replay_nopop", bool, False,
            """
            Don't remove flows from server replay state after use. This makes it
            possible to replay same response multiple times.
            """
        )
        self.add_option(
            "refresh_server_playback", bool, True,
            """
            Refresh server replay responses by adjusting date, expires and
            last-modified headers, as well as adjusting cookie expiration.
            """
        )
        self.add_option(
            "rfile", Optional[str], None,
            "Read flows from file."
        )
        self.add_option(
            "scripts", Sequence[str], [],
            """
            Execute a script.
            """
        )
        self.add_option(
            "showhost", bool, False,
            "Use the Host header to construct URLs for display."
        )
        self.add_option(
            "replacements", Sequence[str], [],
            """
            Replacement patterns of the form "/pattern/regex/replacement", where
            the separator can be any character.
            """
        )
        self.add_option(
            "server_replay_use_headers", Sequence[str], [],
            "Request headers to be considered during replay."
        )
        self.add_option(
            "setheaders", Sequence[str], [],
            """
            Header set pattern of the form "/pattern/header/value", where the
            separator can be any character.
            """
        )
        self.add_option(
            "server_replay", Sequence[str], [],
            "Replay server responses from a saved file."
        )
        self.add_option(
            "stickycookie", Optional[str], None,
            "Set sticky cookie filter. Matched against requests."
        )
        self.add_option(
            "stickyauth", Optional[str], None,
            "Set sticky auth filter. Matched against requests."
        )
        self.add_option(
            "stream_large_bodies", Optional[str], None,
            """
            Stream data to the client if response body exceeds the given
            threshold. If streamed, the body will not be stored in any way.
            Understands k/m/g suffixes, i.e. 3m for 3 megabytes.
            """
        )
        self.add_option(
            "stream_websockets", bool, False,
            """
            Stream WebSocket messages between client and server.
            Messages are captured and cannot be modified.
            """
        )
        self.add_option(
            "verbosity", str, 'info',
            "Log verbosity.",
            choices=log_verbosity
        )
        self.add_option(
            "default_contentview", str, "auto",
            "The default content view mode.",
            choices = [i.name.lower() for i in contentviews.views]
        )
        self.add_option(
            "save_stream_file", Optional[str], None,
            "Stream flows to file as they arrive. Prefix path with + to append."
        )
        self.add_option(
            "save_stream_filter", Optional[str], None,
            "Filter which flows are written to file."
        )
        self.add_option(
            "server_replay_ignore_content", bool, False,
            "Ignore request's content while searching for a saved flow to replay."
        )
        self.add_option(
            "server_replay_ignore_params", Sequence[str], [],
            """
            Request's parameters to be ignored while searching for a saved flow
            to replay.
            """
        )
        self.add_option(
            "server_replay_ignore_payload_params", Sequence[str], [],
            """
            Request's payload parameters (application/x-www-form-urlencoded or
            multipart/form-data) to be ignored while searching for a saved flow
            to replay.
            """
        )
        self.add_option(
            "server_replay_ignore_host", bool, False,
            """
            Ignore request's destination host while searching for a saved flow
            to replay.
            """
        )

        # Proxy options
        self.add_option(
            "proxyauth", Optional[str], None,
            """
            Require proxy authentication. Format:
            "username:pass",
            "any" to accept any user/pass combination,
            "@path" to use an Apache htpasswd file,
            or "ldap[s]:url_server_ldap:dn_auth:password:dn_subtree" for LDAP authentication.
            """
        )
        self.add_option(
            "add_upstream_certs_to_client_chain", bool, False,
            """
            Add all certificates of the upstream server to the certificate chain
            that will be served to the proxy client, as extras.
            """
        )
        self.add_option(
            "body_size_limit", Optional[str], None,
            """
            Byte size limit of HTTP request and response bodies. Understands
            k/m/g suffixes, i.e. 3m for 3 megabytes.
            """
        )
        self.add_option(
            "cadir", str, CA_DIR,
            "Location of the default mitmproxy CA files."
        )
        self.add_option(
            "certs", Sequence[str], [],
            """
            SSL certificates of the form "[domain=]path". The domain may include
            a wildcard, and is equal to "*" if not specified. The file at path
            is a certificate in PEM format. If a private key is included in the
            PEM, it is used, else the default key in the conf dir is used. The
            PEM file should contain the full certificate chain, with the leaf
            certificate as the first entry.
            """
        )
        self.add_option(
            "ciphers_client", Optional[str], None,
            "Set supported ciphers for client connections using OpenSSL syntax."
        )
        self.add_option(
            "ciphers_server", Optional[str], None,
            "Set supported ciphers for server connections using OpenSSL syntax."
        )
        self.add_option(
            "client_certs", Optional[str], None,
            "Client certificate file or directory."
        )
        self.add_option(
            "ignore_hosts", Sequence[str], [],
            """
            Ignore host and forward all traffic without processing it. In
            transparent mode, it is recommended to use an IP address (range),
            not the hostname. In regular mode, only SSL traffic is ignored and
            the hostname should be used. The supplied value is interpreted as a
            regular expression and matched on the ip or the hostname.
            """
        )
        self.add_option(
            "listen_host", str, "",
            "Address to bind proxy to."
        )
        self.add_option(
            "listen_port", int, LISTEN_PORT,
            "Proxy service port."
        )
        self.add_option(
            "upstream_bind_address", str, "",
            "Address to bind upstream requests to."
        )
        self.add_option(
            "mode", str, "regular",
            """
            Mode can be "regular", "transparent", "socks5", "reverse:SPEC",
            or "upstream:SPEC". For reverse and upstream proxy modes, SPEC
            is host specification in the form of "http[s]://host[:port]".
            """
        )
        self.add_option(
            "upstream_cert", bool, True,
            "Connect to upstream server to look up certificate details."
        )
        self.add_option(
            "keep_host_header", bool, False,
            """
            Reverse Proxy: Keep the original host header instead of rewriting it
            to the reverse proxy target.
            """
        )

        self.add_option(
            "http2", bool, True,
            "Enable/disable HTTP/2 support. "
            "HTTP/2 support is enabled by default.",
        )
        self.add_option(
            "http2_priority", bool, False,
            """
            PRIORITY forwarding for HTTP/2 connections. Disabled by default to ensure compatibility
            with misbehaving servers.
            """
        )
        self.add_option(
            "websocket", bool, True,
            "Enable/disable WebSocket support. "
            "WebSocket support is enabled by default.",
        )
        self.add_option(
            "rawtcp", bool, False,
            "Enable/disable experimental raw TCP support. TCP connections starting with non-ascii "
            "bytes are treated as if they would match tcp_hosts. The heuristic is very rough, use "
            "with caution. Disabled by default. "
        )

        self.add_option(
            "spoof_source_address", bool, False,
            """
            Use the client's IP for server-side connections. Combine with
            --upstream-bind-address to spoof a fixed source address.
            """
        )
        self.add_option(
            "upstream_auth", Optional[str], None,
            """
            Add HTTP Basic authentication to upstream proxy and reverse proxy
            requests. Format: username:password.
            """
        )
        self.add_option(
            "ssl_version_client", str, "secure",
            """
            Set supported SSL/TLS versions for client connections. SSLv2, SSLv3
            and 'all' are INSECURE. Defaults to secure, which is TLS1.0+.
            """,
            choices=list(tls.VERSION_CHOICES.keys()),
        )
        self.add_option(
            "ssl_version_server", str, "secure",
            """
            Set supported SSL/TLS versions for server connections. SSLv2, SSLv3
            and 'all' are INSECURE. Defaults to secure, which is TLS1.0+.
            """,
            choices=list(tls.VERSION_CHOICES.keys()),
        )
        self.add_option(
            "ssl_insecure", bool, False,
            "Do not verify upstream server SSL/TLS certificates."
        )
        self.add_option(
            "ssl_verify_upstream_trusted_cadir", Optional[str], None,
            """
            Path to a directory of trusted CA certificates for upstream server
            verification prepared using the c_rehash tool.
            """
        )
        self.add_option(
            "ssl_verify_upstream_trusted_ca", Optional[str], None,
            "Path to a PEM formatted trusted CA certificate."
        )
        self.add_option(
            "tcp_hosts", Sequence[str], [],
            """
            Generic TCP SSL proxy mode for all hosts that match the pattern.
            Similar to --ignore, but SSL connections are intercepted. The
            communication contents are printed to the log in verbose mode.
            """
        )

        self.add_option(
            "intercept_active", bool, False,
            "Intercept toggle"
        )

        self.add_option(
            "intercept", Optional[str], None,
            "Intercept filter expression."
        )

        self.add_option(
            "view_filter", Optional[str], None,
            "Limit which flows are displayed."
        )

        # Dump options
        self.add_option(
            "flow_detail", int, 1,
            """
            The display detail level for flows in mitmdump: 0 (almost quiet) to 3 (very verbose).
              0: shortened request URL, response status code, WebSocket and TCP message notifications.
              1: full request URL with response status code
              2: 1 + HTTP headers
              3: 2 + full response content, content of WebSocket and TCP messages.
            """
        )

        self.update(**kwargs)
