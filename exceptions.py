class HoneygainCredentialsError(Exception):
    """Raised when the authentication token
    provided to authenticate to Honeygain
    fails."""
    pass


class HoneygainError(Exception):
    """Raised when Honeygain throws around random
    response codes (common phenomenon)"""
    pass
