"""
App GPT Slack Bot
"""
import os
import logging
import openai
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack import WebClient


SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", None)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN", None)

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
        # Create prompt for ChatGPT
        prompt = str(body["event"]["text"]).split(">")[1]
        logging.info(prompt)

        # Let thre user know that we are busy with the request
        response = client.chat_postMessage(
            channel=channel,
            thread_ts=thread_ts,
            text=("Recibí tu solicitud :robot_face: \n"
                "Espere por favor.")
        )

        # Check ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        ).choices[0].text

        # Reply to thread
        response = client.chat_postMessage(
            channel=channel,
            thread_ts=thread_ts,
            text=f"Aquí tienes: \n{response}"
        )

    except Exception as exc:
        logging.info(f"Error: {exc}")
        app.client.chat_postMessage(
            channel=channel,
            thread_ts=thread_ts,
            text=f"Hubo un error, no puedo dar una respuesta."
        )


if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
