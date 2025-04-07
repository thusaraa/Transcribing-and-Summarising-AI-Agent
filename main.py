import os
from transcriber import extract_audio, transcribe_audio
from summarizer import summarize_text
from utils import chunked_summary

def video_to_summary(
        video_path: str,
        model_size: str = "base",
        summarize_model: str = "facebook/bart-large-cnn",
        use_chunking: bool = False
) -> str:
    
    #1 Extract audio from video
    audio_path = "temp_audio.wav"
    extract_audio(video_path, audio_path)

    #2 Transcribe audio to text
    transcript = transcribe_audio(audio_path, model_size=model_size)

    # Summarising the transcript
    if use_chunking:
        final_summary = chunked_summary(transcript, summarize_func= lambda txt: summarize_text(
                txt, model_name=summarize_model), chunk_size=2000, overlap=200)
    else:
        final_summary = summarize_text(transcript, model_name=summarize_model)

    # Clean up temporary audio file
    if os.path.exists(audio_path):
        os.remove(audio_path)

    return final_summary

if __name__ == "__main__":
    video_file = "example.mp4"
    summary_output = video_to_summary(
        video_file,
        model_size='base',
        summarize_model='facebook/bart-large-cnn',
        use_chunking=True)
    print("Summary:", summary_output)
    # print("Summary:", summary)
