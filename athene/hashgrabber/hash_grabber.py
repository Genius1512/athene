from fastapi import FastAPI

# create api
app = FastAPI()

# handle get request
@app.get("/{hash}")
def get_hash(hash: str):
    print(f"New hash: {hash}")
    return {"details": "Done"}