# Authored By Certified Coders — v1.2 (2025-11-14)
from config import MONGO_URI

mongo = None
db = None
users = None

if MONGO_URI and MONGO_URI.strip():
    try:
        from motor.motor_asyncio import AsyncIOMotorClient
        mongo = AsyncIOMotorClient(MONGO_URI)
        db = mongo.sessionbuilder
        users = db.users
    except Exception as e:
        print(f"[DB] Mongo connection failed: {e}")
        mongo = None
        db = None
        users = None
else:
    print("[DB] MONGO_URI not set — database features disabled")
