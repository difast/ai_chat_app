from fastapi import WebSocket, WebSocketDisconnect
from app.services.redis import RedisService
from app.services.ai_moderation import AIModerator

class ConnectionManager:
    def __init__(self):
        self.active_connections = []
        self.redis = RedisService()
        self.moderator = AIModerator()

    async def broadcast(self, message: str):
        if self.moderator.check_toxicity(message):
            await self.redis.log_toxic_message(message)
        else:
            for connection in self.active_connections:
                await connection.send_text(message)