from fastapi import FastAPI
import json
import requests as req


app = FastAPI()
data = json.loads(req.get("https://genius1512.github.io/athene/files/data.json").text)


@app.get("/data/{identifier}")
def get_profile(identifier: str):
    try:
        return data[
            "teachers" if 3 <= len(identifier) <= 4 else "students"
        ][identifier]
    except KeyError:
        return {"Error": "Invalid identifier"}
