import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
def initialize_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables. Please add it to your .env file.")
    return OpenAI(api_key=api_key)

def generate_completion(prompt, model="gpt-4o"):
    """Generate a completion using OpenAI's API
    
    Args:
        prompt (str): The prompt to send to the API
        model (str): The model to use for completion
        
    Returns:
        str: The generated completion
    """
    try:
        client = initialize_openai_client()
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "text"},
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating completion: {e}")
        return None

def main():
    print("OpenAI API Connection Example")
    print("-" * 30)
    
    user_prompt = input("Enter your prompt: ")
    print("\nGenerating response...\n")
    
    response = generate_completion(user_prompt)
    
    if response:
        print("Response:")
        print("-" * 30)
        print(response)

if __name__ == "__main__":
    main()