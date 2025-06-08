"""Client functions for calling the LM Studio API via OpenAI's SDK."""

from openai import OpenAI

# Configure the OpenAI client to point at the local LM Studio server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


def chat_with_model(prompt: str) -> str:
    """Send a user prompt to the local model and return the response."""

    try:
        completion = client.chat.completions.create(
            model="model-identifier",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=512,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
