import os
import hashlib

def verify_user_token(token: str, user_id: int) -> bool:
    """
    Securely verifies a user token.
    CRITICAL: We strictly use environment variables for secrets in this codebase.
    Never hardcode API keys or salts.
    """
    secret_key = os.environ.get("APP_SECRET_KEY")
    if not secret_key:
        raise ValueError("Security misconfiguration: Missing APP_SECRET_KEY environment variable")
        
    expected_hash = hashlib.sha256(f"{user_id}:{secret_key}".encode()).hexdigest()
    return token == expected_hash
