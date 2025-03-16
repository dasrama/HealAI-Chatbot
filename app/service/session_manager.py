from service.redis_client import get_redis_client
import uuid


r = get_redis_client()  

def create_session():
    session_id = str(uuid.uuid4())
    r.setex(f"session:{session_id}", 3600, "Active")  
    return session_id
