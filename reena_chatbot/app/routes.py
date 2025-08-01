from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from app.chatbot import get_response
import os

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    # Serve the UI/index.html file
    ui_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'UI')
    return send_from_directory(ui_path, 'index.html')

@app.route("/test", methods=["GET"])
def test():
    """Test endpoint to check if backend is working"""
    return jsonify({
        "status": "success",
        "message": "🟢 Reena chatbot backend is running!",
        "api_ready": os.getenv("GROQ_API_KEY") is not None
    })

@app.route("/chat", methods=["POST"])
def chat():
    print("✅ Received POST request at /chat")

    if not request.is_json:
        print("❌ Request does not contain JSON")
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    print("📦 Request data:", data)

    user_input = data.get("message", "").strip()
    if not user_input:
        print("⚠️ No message provided")
        return jsonify({"error": "No message provided"}), 400

    # Check if API key is configured
    if not os.getenv("GROQ_API_KEY"):
        return jsonify({"error": "GROQ_API_KEY not configured. Please set your Groq API key in environment variables."}), 500

    try:
        response = get_response(user_input)
        print("🤖 Response from chatbot:", response)
        return jsonify({"response": response})
    except Exception as e:
        print("🔥 Error during chatbot response:", e)
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# Serve static files from UI directory
@app.route('/<path:filename>')
def serve_static(filename):
    ui_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'UI')
    return send_from_directory(ui_path, filename)

