import jwt
from app.core.config import conf


def create_jwt_token(user_id: int) -> str:
    to_payload = {"id": user_id}
    token = jwt.encode(to_payload, conf.JWT_SECRET, algorithm="HS256")
    return token


def decode_jwt_token(token: str) -> int:
    payload = jwt.decode(token, conf.JWT_SECRET, algorithms=["HS256"])
    return payload["id"]
