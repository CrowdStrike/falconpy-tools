"""Generic API interface."""
try:
    from falconpy import OAuth2
except ImportError as no_falconpy:
    raise SystemExit(
        "CrowdStrike FalconPy must be installed in order to use this application.\n"
        "Please execute `python3 -m pip install crowdstrike-falconpy` and try again."
        ) from no_falconpy


class ToolboxAPI():
    """Base class to represent the Falcon API."""

    def __init__(self, auth_object: object = None, **kwargs):
        """Initialize an instance of the base class, creating the authorization object.

        :str    key         - API client ID to use for authentication.
        :str    secret      - API client secret to use for authentication.
        :str    base        - Base URL to use for API requests.
        :bool   use_ssl     - Enable / disable SSL verification. Defaults to enabled.
        :float  timeout     - Total time in seconds for API requests before timeout.
        :tuple  timeout     - Connect / Read time in seconds for API requests before timeout.
        :dict   proxy       - List of proxies to use for requests made to the API.
        :object auth_object - Pre-initialized FalconPy OAuth2 authentication object.
        """
        if auth_object:
            self.auth = auth_object
        else:
            self.auth = OAuth2(
                client_id=kwargs.get("key", None),
                client_secret=kwargs.get("secret", None),
                base_url=kwargs.get("base", "us1"),
                ssl_verify=kwargs.get("use_ssl", True),
                timeout=kwargs.get("timeout", None),
                proxy=kwargs.get("proxy", None)
                )

    def authenticated(self):
        """Return the authentication status from the auth object."""
        return self.auth.authenticated()

    def deauthenticate(self):
        """Deauthenticate from the API."""
        self.auth.revoke(self.auth.token_value)
