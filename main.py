"""Minimal HTTP service for project skeleton step one."""

from fastapi import FastAPI

app = FastAPI(title="CSC 4033 Project Skeleton")


@app.get("/", summary="Check that the service is running")
def root() -> dict[str, str]:
    return {"service": "CSC 4033 Project Skeleton", "status": "running"}


# to run server open terminal:
    # python -m uvicorn main:app --reaload 

# to end server crtl + c