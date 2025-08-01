#!/usr/bin/env python3
"""
Startup script for Reena Insurance Chatbot
This script will install dependencies and start the Flask server
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required Python packages"""
    print("📦 Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False
    return True

def start_server():
    """Start the Flask server"""
    print("🚀 Starting Reena Insurance Chatbot...")
    print("🌐 Server will be available at: http://localhost:5000")
    print("📱 Open your browser and navigate to the URL above")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "run.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

def main():
    print("🤖 Welcome to Reena Insurance Chatbot!")
    print("=" * 50)
    
    # Install dependencies
    if not install_requirements():
        print("❌ Failed to install dependencies. Please check your Python environment.")
        return
    
    # Start server
    start_server()

if __name__ == "__main__":
    main() 