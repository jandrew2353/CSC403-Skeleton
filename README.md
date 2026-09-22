# CSC 4033 Project Skeleton

Step one uses FastAPI to return a JSON response at `/`.

## Run locally

From this folder in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

Open http://127.0.0.1:8000/ in a browser. The response is:

```json
{"service":"CSC 4033 Project Skeleton","status":"running"}
```

## Public deployment

Step one is complete only once this service is deployed and its public URL
returns the response above. A cloud account and public deployment have not
been configured in this project.

Configure your Python host to install `requirements.txt` and start the service
with this command, replacing `8000` if your host requires a different port:

```text
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

After deployment, open the host's public HTTPS URL and confirm the JSON response.
