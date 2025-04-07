import subprocess
import whisper
import os

def extract_audio(video_path: str, audio_path: str = "temp_audio.wav") -> str:
    """
    Extracts audio from a video file using ffmpeg.

    Args:
        video_path (str): Path to the input video file.
        audio_path (str): Path to save the extracted audio file.
    """
    if os.path.exists(audio_path):
        os.remove(audio_path)
        
    command = [
        'ffmpeg',
        '-i', video_path,
        '-q:a', '0',  # Best audio quality
        '-map', 'a',  # Select audio stream
        # '-vn',  # No video
        # '-acodec', 'copy',  # Copy audio codec
        audio_path,
        '-y'  # Overwrite output file if it exists
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return audio_path


def transcribe_audio(audio_path: str, model_size = "base") -> str:
    """
    Transcribes audio to text using Whisper model.

    Args:
        audio_path (str): Path to the audio file.
        model_name (str): Name of the Whisper model to use.

    Returns:
        str: Transcribed text.
    """
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path)
    transcript = result['text']
    return transcript
