import { useEffect, useState } from "react";
import axios from "axios";

const API_URL = "http://localhost:8000/notes/";

export default function App() {
  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [error, setError] = useState("");

  // ✅ Fetch notes from backend
  useEffect(() => {
    fetchNotes();
  }, []);

  const fetchNotes = async () => {
    try {
      const response = await axios.get(API_URL);
      setNotes(response.data);
    } catch (error) {
      setError("Error fetching notes");
      console.error("Fetch error:", error);
    }
  };

  // ✅ Add a new note
  const addNote = async () => {
    if (!title || !content) {
      setError("Title and content cannot be empty");
      return;
    }
    try {
      const response = await axios.post(API_URL, { title, content });
      setNotes([...notes, response.data]);
      setTitle("");
      setContent("");
      setError("");
    } catch (error) {
      setError("Error adding note");
      console.error("Add error:", error);
    }
  };

  // ✅ Delete a note
  const deleteNote = async (id) => {
    try {
      await axios.delete(`${API_URL}${id}`);
      setNotes(notes.filter((note) => note.id !== id));
    } catch (error) {
      setError("Error deleting note");
      console.error("Delete error:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-xl mx-auto bg-white p-4 shadow-lg rounded-lg">
        <h2 className="text-xl font-bold mb-4">Notes</h2>

        {error && <p className="text-red-500">{error}</p>}

        <input
          className="w-full p-2 border mb-2"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          className="w-full p-2 border mb-2"
          placeholder="Content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        ></textarea>
        <button className="bg-blue-500 text-white p-2 w-full" onClick={addNote}>
          Add Note
        </button>

        <ul className="mt-4">
          {notes.map((note) => (
            <li key={note.id} className="flex justify-between p-2 border-b">
              <div>
                <h3 className="font-bold">{note.title}</h3>
                <p>{note.content}</p>
              </div>
              <button
                className="text-red-500"
                onClick={() => deleteNote(note.id)}
              >
                Delete
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
