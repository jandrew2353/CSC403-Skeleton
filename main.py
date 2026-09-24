from fastapi import FastAPI, HTTPException
import random

app = FastAPI(tittle="Dice Roller yay!")

#end point one. Checks if the server is running
@app.get("/")
def root():
    return {"Service": "Dice Roller, YAY!", "status": "running, YAY!"}

#end point two roll the dice
@app.get("/roll")
def roll(side: int):
    #make sure that the side rolled is valid
    if side < 2 or side > 100:
        raise HTTPException(
            status_code=400,
            detail="Sides must be between 2 and 100"
        )

    result = random.randint(1,side)

    return {"side": side, "result": result}

# python -m uvicorn main:app --reload (used to run in vscode)
# USE make build            (docker build -t dice-roller . (build docker container))
# USE make run              (docker run --rm -p 8000:8000 dice-roller (run docker container))
# ctrl + c to end

# leave root alone for server status
# to roll the dice /roll?side=(desired size)
# for error /roll?side=1
# to see all end points /docs
