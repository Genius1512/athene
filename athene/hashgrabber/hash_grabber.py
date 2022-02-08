import sys

from fastapi import FastAPI

sys.path.append("../athene")
from athene.console import console

# create api
app = FastAPI()

# handle get request
@app.get("/{hash}")
def get_hash(hash: str):
    console.print(f"New hash: {hash}", style="success")
    return {"details": "Done"}
