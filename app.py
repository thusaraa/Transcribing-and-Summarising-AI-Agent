import streamlit as st
import os
from main import video_to_summary

def main():
    st.title("Video to Summary App")

    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])

    if uploaded_file is not None:
        with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_file.read())

        st.write("Transcribing and summarizing the video...")

        summary_result = video_to_summary(
            video_path="temp_video.mp4",
            model_size='base',
            summarize_model='facebook/bart-large-cnn',
            use_chunking=True
        )

        st.subheader("Summary")
        st.write(summary_result)

        if os.path.exists("temp_video.mp4"):
            os.remove("temp_video.mp4")

if __name__ == "__main__":
    main()