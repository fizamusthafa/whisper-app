
import streamlit as st
import whisper
import tempfile
import os

st.title("Multi-lingual Transcription using Whisper")

audio_file = st.file_uploader("Upload your audio", type=["wav", "mp3", "m4a"])
model = whisper.load_model("base")

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing...")
        with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
            temp_audio.write(audio_file.read())

        # Get the absolute path of the temporary audio file
        audio_file_path = os.path.abspath(temp_audio.name)

        transcription = model.transcribe(audio_file_path)
        st.sidebar.success("Transcription complete")
        st.markdown(transcription["text"])

        # Clean up the temporary file after processing
        os.remove(audio_file_path)
    else:
        st.sidebar.error("Please upload an audio file.")