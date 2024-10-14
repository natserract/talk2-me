# Talk2-Me
Talk to me?

## **Mechanism Overview:**

**Pre-requisites:**
- Use a webcam to capture video stream.
- Provide WebRTC (e.g., Livekit) to stream the video in real-time.

**Input Processing:**
- Capture the image from the video stream.
- Use speech-to-text technology (Deepgram) to convert the user's voice input into text.
- Pass the captured image and text input as context to the LLM (OpenAI GPT-4).

**Response Generation:**
- LLM (OpenAI GPT-4) processes the input context and generates a text response.
- Convert the text response back to speech using a text-to-speech

![Screen Shot 2024-06-25 at 17 32 03](https://github.com/natserract/talk2-me/assets/31182611/7f8a7554-c6f3-40d7-b668-6c35c33c3cca)

## Running

```sh
rye pin 3.11.9

# Install packages
rye sync

# Download livekit plugins
rye run talk2-me download-files

# Running
rye run talk2-me start
```

## Playground
Go to https://agents-playground.livekit.io/

## WIP
- [x] Voice talks
- [ ] Video track & capturing

**Related Issue:**

```sh
LOG: [W NNPACK.cpp:64] Could not initialize NNPACK! Reason: Unsupported hardware.
```
> Still looking how to solve this issue. Currently only able to voice talks.
