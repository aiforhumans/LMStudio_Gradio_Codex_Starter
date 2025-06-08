import httpx

LM_STUDIO_API_URL = "http://localhost:1234/v1/chat/completions"


def chat_with_model(prompt: str) -> str:
    payload = {
        "model": "local-model",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 512
    }
    try:
        response = httpx.post(LM_STUDIO_API_URL, json=payload, timeout=30.0)
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"
