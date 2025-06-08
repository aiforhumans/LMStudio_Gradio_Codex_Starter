import gradio as gr
from api_client import chat_with_model


def respond(user_input):
    return chat_with_model(user_input)


def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# 🧠 Local AI Chatbot (LM Studio + Gradio)")
        chatbot = gr.Chatbot()
        msg = gr.Textbox(label="Type your message:")
        clear = gr.Button("Clear Chat")

        def user_submit(user_message, chat_history):
            bot_message = respond(user_message)
            chat_history = chat_history + [[user_message, bot_message]]
            return "", chat_history

        msg.submit(user_submit, [msg, chatbot], [msg, chatbot])
        clear.click(lambda: None, None, chatbot, queue=False)

    return demo
