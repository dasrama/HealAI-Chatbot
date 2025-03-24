from config.config import r
import uuid


def get_user_session(user_id):
    session_key = f"user_session:{user_id}"
    session_id = r.get(session_key)

    if session_id is None:
        session_id = str(uuid.uuid4())
        r.setex(f"session:{session_id}", 3600, "Active") 

    return session_id

def store_chat(session_id, user_input, bot_response):
    r.rpush(f"chat:{session_id}", f"User: {user_input}")
    r.rpush(f"chat:{session_id}", f"Bot: {bot_response}")

def get_chat_history(session_id):
    return r.lrange(f"chat:{session_id}", 0, -1)

