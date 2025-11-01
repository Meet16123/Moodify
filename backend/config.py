import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Spotify OAuth
    SPOTIFY_CLIENT_ID = os.getenv('CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    SPOTIFY_REDIRECT_URI = os.getenv('REDIRECT_URI', 'http://localhost:5000/callback')
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # MongoDB (for later weeks)
    MONGODB_URI = os.getenv('MONGODB_URI', '')
    
    # Google Gemini API (for Week 2)
    GEM_API_KEY = os.getenv('GEM_API_KEY', '')