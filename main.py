from openai import OpenAI
import os

client = OpenAI()

def testConnection():
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role":"user","content":"Say hello briefly."}
        ]
    )

    print(response.choices[0].message.content)

#if __name__ == "__main__":
    #testConnection()

def transcribe_audio(filename):
    with open(filename,"rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model = "whisper-1",
            file=audio_file
                
        )
    return transcript.text

def ask_llm(question):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {"role":"system","content":"You are a helpful NBA statistics assistant."},
            {"role":"user","content":question}
        ]
    )
    return response.choices[0].message.content



if __name__ == "__main__":
    question_text = transcribe_audio("Voice1.m4a")
    print("Transcription:",question_text)
    
    answer = ask_llm(question_text)
    print("\nGPT-4 Response:")
    print(answer)

