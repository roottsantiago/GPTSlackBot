"""
App GPT Slack Bot
"""
import logging
import openai
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack import WebClient
from chat.settings import (
    SLACK_APP_TOKEN,
    SLACK_BOT_TOKEN,
    OPENAI_API_KEY,
    MODEL,
    CHUNK_SIZE
)
from chat.helpers import (
    update_chat, 
    chat_post_message,
    get_conversation,
    create_conversation
)

# Event API & Web API
app = App(token=SLACK_BOT_TOKEN)
client = WebClient(SLACK_BOT_TOKEN)
openai.api_key = OPENAI_API_KEY


# This gets activated when the bot is tagged in a channel
@app.event("app_mention")
def handle_message_events(body, context):
    """
    Message events
    """
    try:
        # Log message
        channel = body["event"]["channel"]
        thread_ts = body["event"].get("thread_ts", body["event"]["ts"])
        bot_user_id = context["bot_user_id"]
        # Let thre user know that we are busy with the request
        slack_response = app.client.chat_postMessage(
            channel=channel,
            thread_ts=thread_ts,
            text="Recibí tu solicitud :robot_face: \n Espere por favor..."
        )
        message_ts = slack_response["message"]["ts"]
        conversation = get_conversation(app, channel, thread_ts)
        messages = create_conversation(conversation, bot_user_id)
        # Check ChatGPT
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=messages,
            stream=True
        )
        # Reply to thread
        response_text = ""
        count = 0
        for chunk in response:
            if chunk.choices[0].delta.get("content"):
                count += count
                response_text += chunk.choices[0].delta.content
                if count > CHUNK_SIZE:
                    update_chat(app, channel, message_ts, response_text)
                    count = 0
            elif chunk.choices[0].finish_reason == "stop":
                update_chat(app, channel, message_ts, response_text)

    except Exception as exc:
        logging.info(f"Error: {exc}")
        chat_post_message(app, channel, thread_ts)


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
