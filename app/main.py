from fastapi import FastAPI

app = FastAPI(title="auth-service")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}

