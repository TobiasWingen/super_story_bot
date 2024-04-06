#IMPORTANT TO NOTE: RUNNING THIS CODE WILL COST YOU MONEY####


# import libraries
import os
from dotenv import load_dotenv
from openai import OpenAI
import re
from pathlib import Path
# note AudioSegment requires ffmpeg 
from pydub import AudioSegment

# Load environment variables from .env file
# Make sure this .env file exists/can be accessed 
load_dotenv()

# Retrieve API key
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client with API key
client = OpenAI(api_key=api_key)

# Functions to clean and handle text
# to remove the " sign which may cause problems for the text-to-speech software
def clean_text(text):
    text = re.sub(r"ChatCompletionMessage\(content='", '', text)
    text = re.sub(r"', role='assistant', function_call=None, tool_calls=None\)", '', text)
    text = text.replace('\\n', ' ')
    text = text.replace('"', '')
    return text

#to split the text in manageble chunks respecting the TTS character limit
def split_text(text, chunk_size=4096):
    words = text.split()
    chunks = []
    current_chunk = words[0]
    for word in words[1:]:
        if len(current_chunk) + len(word) + 1 <= chunk_size:
            current_chunk += ' ' + word
        else:
            chunks.append(current_chunk)
            current_chunk = word
    chunks.append(current_chunk)  # Add the last chunk
    return chunks

#to ensure file names can be used 
def clean_text_for_filename(text):
    # Remove any invalid characters for filenames
    text = re.sub(r'[<>:"/\\|?*]', '', text)  # Removes characters not allowed in Windows filenames
    text = re.sub(r'\s+', '_', text)  # Replace spaces with underscores
    text = text[:100]  # Limit the length to avoid too long filenames
    return text


# Function to convert text to speech and save as MP3
# model and voice are set here

def text_to_speech(text_chunks, story_number):
    mp3_paths = []
    for i, chunk in enumerate(text_chunks):
        speech_file_path = Path(f"story_{story_number}_part_{i}.mp3")
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=chunk
        )
        response.stream_to_file(speech_file_path)
        mp3_paths.append(speech_file_path)
    return mp3_paths

# Function to merge MP3 files
def merge_mp3s(mp3_paths, story_number):
    combined = AudioSegment.empty()
    for mp3_path in mp3_paths:
        combined += AudioSegment.from_mp3(mp3_path)
    combined.export(f"story_{cleaned_title}_combined.mp3", format="mp3")





# The outer for loop sets the number of stores 
# Generate 6 different stories
number_stories = 6


for story_number in range(1, number_stories):
    # Request an outline and a title for a superhero children's book story in German with 5 chapters
    outline_response = client.chat.completions.create(
      model="gpt-4",
      messages=[
        #the general content of the stories
        {"role": "system", "content": "You're crafting superhero tales for young children. The adventures center on the siblings Emma (6) and Leo (4), along with their cousin Mia (4). These kids possess unique superpowers that enable them to tackle challenges and assist others in their community. In each episode, they face a new, imaginative predicament that requires their special skills for resolution. From saving a local park from environmental threats to helping lost animals find their way home, Emma, Leo, and Mia demonstrate teamwork, compassion, and quick thinking, embodying the spirit of young heroes making a difference in their world."},
        #tell it to outline 5 chapters and a title
        {"role": "user", "content": "Please create a draft for a superhero story with 5 chapters and give it a suitable title for preschool children."}
      ]
    )

    # Extract the title and the outline from the first response
    title_and_outline = outline_response.choices[0].message.content
    title = title_and_outline.split('\n')[0]  # The title is the first line
    outline = '\n'.join(title_and_outline.split('\n')[1:])  # The rest is the outline

    # Then include the outline in each chapter request
    chapters = []
    for i in range(1, 6):
        chapter_response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": outline},  # Include the outline here
                #ask it to now create the actual story
                {"role": "user", "content": f"Please write chapter {i} of the superhero tale"}
            ]
        )
        chapters.append(chapter_response.choices[0].message.content)


    # Combine chapters into a full story
    full_story = "\n".join(chapters)
    cleaned_story = clean_text(full_story)
    cleaned_title = clean_text_for_filename(title)  # You may need to clean or process this further

    # Split, convert to speech, and merge
    text_chunks = split_text(cleaned_story)
    mp3_paths = text_to_speech(text_chunks, story_number)
    merge_mp3s(mp3_paths, story_number)

    # Ensure title is cleaned or processed if needed for file naming or printing
    # This might include removing or replacing characters not allowed in filenames
    print(f"Story {story_number} titled '{cleaned_title}' has been saved as MP3.")


print("All stories have been created and saved.")

