# Multi-lingual Transcription using Whisper

This is a simple web application that allows users to transcribe audio files into text using the [Whisper Automatic Speech Recognition (ASR) model](https://github.com/openai/whisper). The application is built using Streamlit and leverages OpenAI's Whisper to perform transcriptions.

## How to Use

* **Upload Audio**: Click on the button and select (or drag and drop) an audio file in WAV, MP3, or M4A format that you want to transcribe.
  ![alt text](https://github.com/fizamusthafa/whisper-app/blob/master/overview.png "Drag or Upload")
* **Transcribe Audio**: Once the audio file is uploaded, click on the "Transcribe Audio" button in the sidebar. The application will start transcribing the audio using the Whisper model.
* **Supported Languages**: The Whisper model supports multiple languages. The application will automatically detect the language of the uploaded audio and provide accurate transcriptions for a wide range of languages. This includes *Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.*
* **Clean-up**: After the transcription is complete, the temporary audio file will be removed to ensure your data privacy.

## Requirements

To run this application locally, you need to have Python installed along with the following packages:

* Streamlit
* Whisper

You can install the required packages using the following commands:
```
pip install streamlit
pip install whisper
```

## How to Run

* Clone this repository to your local machine.
* Open a terminal or command prompt and navigate to the repository's directory.
* Run the Streamlit application: `streamlit run whisper-app.py`
* The application will open in your web browser, and you can start transcribing audio files right away.

