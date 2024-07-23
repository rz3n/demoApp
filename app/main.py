from typing import Union
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
#def read_root():
#  raise HTTPException(status_code=500, detail="bug")
  return [
    { "message": "Hello!" },
    { "version": "1.0" }
  ]


@app.get("/healthcheck")
async def healthcheck():
  return { "code": "200" }


@app.get("/error")
async def erro():
  raise HTTPException(status_code=500, detail="error")


@app.get("/denied")
async def denied():
  raise HTTPException(status_code=404, detail="denied")
