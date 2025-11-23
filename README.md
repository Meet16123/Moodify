**Moodify – Emotion-Based Music Recommendation System**
COSC-3117 – Artificial Intelligence Final Project

**Group Members**

Meet Mangroliya – 5145432

Sukhraj Mahal – 5144420

Nandnee Patel – 5143156

🎧 Overview

Moodify is an intelligent, emotion-driven music recommendation system designed to create a personalized playlist that adapts to the user’s real-time mood and context.

Instead of relying on static playlists or past listening history, Moodify uses AI-powered text analysis, real-time facial emotion recognition, and learning-based behavior tracking to play music that matches how the user feels right now.

Core Features

📝 Text-Based Mood Analysis
Users can type how they feel; the system extracts sentiment & keywords using AI.

🎥 Real-Time Facial Emotion Detection
Uses webcam input to continuously monitor user emotions (happy, sad, angry, etc.).

🎵 Automatic Music Recommendation & Playback
Mood-matched tracks are played via the Spotify API.

📈 Learning Preference System
The system scores songs based on how the user emotionally reacts and adapts over time.

🔊 Smart Volume Adjustment
Volume automatically adjusts depending on user's distance from screen.

🏗️ System Architecture & Tech Stack

Moodify is a full-stack AI-powered application built with modern frameworks and cloud services.

1. Frontend — Next.js 14 + React + Tailwind CSS

Handles:

UI dashboard

Music player

Webcam streaming

Real-time mood updates via Server-Sent Events (SSE)

API communication

2. Backend — Flask (Python)

Acts as the logic layer for:

Text emotion processing

Facial recognition pipeline

Spotify authentication + playback control

Emotion scoring system

Threading processes for constant webcam monitoring

API endpoints for frontend

3. AI & External Services
🔹 Spotify Web API

OAuth login

Searching tracks

Controlling playback

🔹 Google Gemini AI

NLP processing for user text

Extracts sentiment + keywords

🔹 DeepFace & OpenCV

Real-time webcam frame capture

Facial emotion recognition

Distance measurement for smart volume

🔹 MongoDB

Stores:

Songs with emotion-specific scores

Total reaction scores

User preference data

🤖 Use of AI

Moodify uses AI in two powerful ways:

1. Natural Language Processing (Gemini)

Users type natural sentences such as:

“Feeling tired from studying”
Gemini extracts:

Sentiment: tired

Context keyword: studying
These drive Spotify mood-based search queries.

2. Computer Vision (DeepFace + OpenCV)

Continuously analyzes facial expressions

Detects emotion every few seconds

Updates emotional scores for currently playing tracks

Allows Moodify to "learn" what music the user genuinely likes based on reactions

These AI tools make Moodify a truly intelligent, adaptive system rather than a static recommender.

⚠️ Challenges Faced
1. Real-Time Synchronization

Balancing:

Continuous webcam processing

Database updates

Spotify track changes

Smooth frontend experience

…without lag or interruptions required careful multithreading & optimization.

2. State Management

Keeping frontend UI in sync with backend events required:

Server-Sent Events

React state management

MongoDB → frontend data propagation

3. External API Reliability

Spotify & Gemini have:

Rate limits

Occasional latency

Error handling requirements

Robust fallback logic was needed to avoid crashes.

4. Concurrency & Threading

Backend handled:

API requests

Webcam thread

Emotion scoring thread

Database operations

Thread-safety and race-condition prevention were critical.

📚 Key Learnings
Team Growth

Sukhraj: Built his first full-stack application, mastering Flask + Next.js integration.

Meet: Learned Python backend + AI model integration for the first time.

Nandnee: Gained confidence navigating complex codebases through AI assisted learning despite non-programming background.

Technical Skills Learned

Full-stack development

Real-time systems

AI integration

Spotify API + OAuth

DeepFace computer vision

MongoDB schema design

SSE-based communication

The project strengthened our ability to rapidly learn new tools and design an end-to-end AI-powered system.

✅ Conclusion

Moodify demonstrates the power of combining AI, real-time data processing, and modern web technologies to create emotionally intelligent applications.
