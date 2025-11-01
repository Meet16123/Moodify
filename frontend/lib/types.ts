// Authentication types
export interface AuthStatus {
    isAuthenticated: boolean
    user?: {
      id: string
      name: string
      email: string
      image?: string
    }
  }
  
  // Emotion Analysis types
  export interface EmotionAnalysis {
    sentiment: 'positive' | 'negative' | 'neutral'
    keywords: string[]
    mood: string
  }
  
  // Music types
  export interface Track {
    id: string
    name: string
    artist: string
    album: string
    image?: string
    preview_url?: string
    duration_ms: number
  }
  
  export interface PlaybackStatus {
    isPlaying: boolean
    currentTrack?: Track
    progress: number
    volume: number
  }