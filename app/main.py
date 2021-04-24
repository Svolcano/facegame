# app entrypoint
import uvicorn
from fastapi import FastAPI
from routers import facegame, root

app = FastAPI()
app.include_router(facegame.router)
app.include_router(root.router)


if __name__ == '__main__':
    uvicorn.run(app='main.app', host='0.0.0.0', port=8001)


