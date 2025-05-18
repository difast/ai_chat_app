from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base
from app.db.session import engine
from app.api.endpoints import users, chat
from app.websocket.chat import websocket_router

app = FastAPI(title="AI Chat App")
app.add_middleware(CORSMiddleware, allow_origins=["*"])

app.include_router(users.router)
app.include_router(chat.router)
app.include_router(websocket_router)

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)