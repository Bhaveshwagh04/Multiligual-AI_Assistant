from setuptools import find_packages, setup

setup(
    name="Multilingual Assistance",
    version="0.0.1",
    author="Bhavesh Wagh",
    author_email="bhaveshwaghbw.49@gmail.com",
    packages=find_packages(),
    install_requires=[
        "SpeechRecognition",
        "pipwin",
        "pyaudio",
        "gTTS",
        "google-generativeai",
        "python-dotenv",
        "streamlit",
    ],
)
