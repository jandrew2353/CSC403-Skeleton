from fastapi import FastAPI

#create fast api for webserver
app = FastAPI(title="CSC 4033 Project Skeleton")

# Create a GET endpoint for the root URL ("/")
# This runs when someone visits http://localhost:8000/
# The summary describes what this endpoint does
@app.get("/", summary="Check that the service is running")
# Define the function that runs when the root endpoint is accessed
# dict[str, str] means the function returns a dictionary
# containing string keys and string values
def root() -> dict[str, str]:
    return {"service": "CSC 4033 Project Skeleton", "status": "running"}


# to run server open terminal:
    # python -m uvicorn main:app --reload

# to run docker build docker build -t fastapi-skeleton .

# to end server crtl + c