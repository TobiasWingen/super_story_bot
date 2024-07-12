

# Audio Story Generator

This project enables the generation of audio stories for children, adaptable to various themes. The example code focuses on German superhero tales. It utilizes OpenAI's GPT models for crafting stories which are then converted into audio format. Stories have a length from 5 - 15 minutes and contain 5 chapters

## Cost and Risk Disclaimer

Use of this script involves making API calls that incur costs from OpenAI. Users are responsible for these costs and must ensure they have a valid OpenAI API subscription or pay-per-use arrangement. The author(s) of this script do not assume responsibility for any costs, claims, or damages related to the use of this script. Use at your own risk and expense. This is a private project by me and not related to my employer.

## Project Overview

The script offers a flexible framework for generating stories by adjusting initial prompts for a wide range of narratives. It automates the process from text generation to audio file production, exemplified by a superhero story to illustrate its capabilities.

## Features

- **Flexible Story Generation**: Create stories on a wide range of themes by adjusting the initial prompts to fit the desired narrative.
- **Longer stories**: Due to requesting five chapters, stories become longer than the typical response.
- **Automated Text Cleaning**: Prepares generated text for text-to-speech conversion by removing or replacing problematic characters.
- **Text-to-Speech Conversion**: Converts the story text into spoken audio, managing character limits by segmenting the story as needed.
- **Audio File Merging**: Merges segmented audio files into a single MP3 file for each story, making it convenient for playback.

## Installation

To get started with generating your own audio stories, follow these steps:

1. Clone this repository: https://github.com/TobiasWingen/super_story_bot.git

2. Install the required Python libraries:



### Additional Requirements

- **ffmpeg**: Required by `pydub` for audio conversion. Ensure `ffmpeg` is installed and in your system's PATH. I found this guide helpful: https://phoenixnap.com/kb/ffmpeg-windows
- **OpenAI API Key**: Necessary for accessing the GPT models. Securely store your API key in a `.env` file as `OPENAI_API_KEY=<your_api_key_here>`.

## Usage

Adjust the initial prompts within the script for your desired theme and run:


## Customizing Story Themes

Modify the prompts in the script to reflect your desired narrative theme.

## Legal Disclaimer

This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software.

Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.

## Acknowledgements

OpenAI's GPT models are utilized for story generation and text-to-speech conversion.
