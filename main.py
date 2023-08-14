import requests

# Replace with your actual API key
api_key = "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"

# ChatGPT API endpoint
api_endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

def generate_instructions(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "prompt": prompt,
        "max_tokens": 500  # Adjust as needed
    }

    response = requests.post(api_endpoint, json=data, headers=headers)

    try:
        response_data = response.json()
        if 'choices' in response_data and response_data['choices']:
            return response_data['choices'][0]['text']
        else:
            return "No instructions generated."
    except Exception as e:
        return f"Error processing API response: {e}"

def main():
    prompt = "tell me briefly the ingredients and directions to make"
    instructions = generate_instructions(prompt)
    
    print("Generated Instructions:")
    print(instructions)

if __name__ == "__main__":
    main()
