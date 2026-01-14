ISSUER = "https://auth.example.com"


def discovery_document() -> dict:
    return {"issuer": ISSUER, "jwks_uri": f"{ISSUER}/.well-known/jwks.json"}

