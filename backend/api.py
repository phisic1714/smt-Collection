from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess


class RunBody(BaseModel):
    emulator: str | None = None
    rom: str | None = None


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/run-game")
def run_games(req_body: RunBody):

    emulator = req_body.emulator
    rom = req_body.rom

    subprocess.Popen(f'start "" "{emulator}" "{rom}"', shell=True)
    return {"Hello": "World"}
