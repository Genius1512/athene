from fastapi import FastAPI
import json


app = FastAPI()
data = json.load(open(r"C:\Users\silva\Projects\athene\athene\data\data\data.json", "r"))


@app.get("/data/{identifier}")
def get_profile(identifier: str):
    try:
        return data[
            "teachers" if 3 <= len(identifier) <= 4 else "students"
        ][identifier]
    except KeyError:
        return {"Error": "Invalid identifier"}
