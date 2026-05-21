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
    try:
        if not emulator or not rom:
            return {"error": "emulator and rom must be provided"}
        # both emulator and rom are guaranteed to be str here
        subprocess.Popen([emulator, rom])
        return {"success": True}
    except Exception as e:
        print(e)
        return {"error": str(e)}
