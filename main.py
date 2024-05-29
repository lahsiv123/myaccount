from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "GMAC Career Compass is on the horizon"}