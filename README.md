# OpenAI API Connection Project

This project demonstrates how to connect to the OpenAI API using Python. It allows you to send prompts to OpenAI models and receive responses.

## Setup Instructions

### 1. Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### 2. Set Up API Key

1. Create a `.env` file in the project root directory
2. Copy the contents from `.env.example` to your new `.env` file
3. Replace `your_api_key_here` with your actual OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)

### 3. Run the Application

Execute the main script:

```bash
python main.py
```

## Usage

When you run the application:

1. You'll be prompted to enter your question or prompt
2. The application will send your prompt to the OpenAI API
3. The response will be displayed in the console

## Features

- Secure API key storage using environment variables
- Error handling for API requests
- Configurable model selection (default: gpt-4o)
- Simple command-line interface

## Customization

You can modify the `generate_completion` function in `main.py` to adjust parameters like:

- Model selection
- Temperature
- Max tokens
- System prompt
- Other OpenAI API parameters