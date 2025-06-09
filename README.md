# LM Studio + Gradio Chatbot Starter

## How to run:

1️⃣ Install Python 3.11+  
2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Start app:

```bash
python app.py
```

Gradio will open → Chat with your local LM Studio AI model.

### Using the OpenAI client

LM Studio exposes an OpenAI-compatible API. Point the OpenAI SDK at your
local server and reuse the normal methods:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
    model="model-identifier",
    messages=[{"role": "user", "content": "Hello"}]
)
``` 

See `api_client.py` for a complete example.

---

## Structure:

- `app.py` → main app entry point
- `api_client.py` → calls LM Studio API (http://localhost:1234)
- `ui.py` → Gradio UI
- `tests/` → tests folder (optional)
- `AGENTS.md` → guide for Codex agent

---

Happy coding 🚀
