from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from dotenv import load_dotenv
import os

# ✅ Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "notes_db"
COLLECTION_NAME = "notes"

# ✅ Initialize FastAPI
app = FastAPI()

# ✅ Enable CORS (Fixing the CORS Issue)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # ✅ Change to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # ✅ Allow all headers
)

# ✅ Connect to MongoDB
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# ✅ Pydantic model for Notes
class NoteModel(BaseModel):
    title: str
    content: str

# ✅ Create a new note
@app.post("/notes/", status_code=201)
async def create_note(note: NoteModel):
    note_dict = note.dict()
    result = await collection.insert_one(note_dict)
    return {"id": str(result.inserted_id), **note_dict}

# ✅ Get all notes
@app.get("/notes/", status_code=200)
async def get_notes():
    notes = await collection.find().to_list(100)
    return [{"id": str(note["_id"]), "title": note["title"], "content": note["content"]} for note in notes]

# ✅ Get a single note by ID
@app.get("/notes/{note_id}")
async def get_note(note_id: str):
    note = await collection.find_one({"_id": ObjectId(note_id)})
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"id": str(note["_id"]), "title": note["title"], "content": note["content"]}

# ✅ Update a note
@app.put("/notes/{note_id}", status_code=200)
async def update_note(note_id: str, note: NoteModel):
    result = await collection.update_one({"_id": ObjectId(note_id)}, {"$set": note.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"id": note_id, **note.dict()}

# ✅ Delete a note
@app.delete("/notes/{note_id}", status_code=200)
async def delete_note(note_id: str):
    result = await collection.delete_one({"_id": ObjectId(note_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}
