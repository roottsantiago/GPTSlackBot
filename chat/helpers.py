from chat.settings import SYSTEM_PROMPT


def chat_post_message(app, channel, thread_ts,
                      text=f"Hubo un error, no te puedo dar una respuesta."):
    """
    Method Post Message
    """
    app.client.chat_postMessage(
        channel=channel,
        thread_ts=thread_ts,
        text=text
    )

def get_conversation(app, channel, thread_ts):
    """
    Method get conversation
    """
    replies = app.client.conversations_replies(
        channel=channel,
        ts=thread_ts,
        inclusive=True
    )
    return replies


def create_conversation(conversation, bot_user_id):
    """
    Method process conversation
    """
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for message in conversation['messages'][:-1]:
        role = "assistant" if message['user'] == bot_user_id else "user"
        message_text = process_message(message, bot_user_id)
        if message_text:
            messages.append({"role": role, "content": message_text})
    return messages


def clean_message(message_text, role, bot_user_id):
    """
    Method clean message text
    """
    if (f"<@{bot_user_id}>" in message_text) or (role == "assistant"):
        message_text = message_text.replace(f"<@{bot_user_id}>", "").strip()
        return message_text
    return None


def process_message(message, bot_user_id):
    """
    Method process message
    """
    message_text = message['text']
    role = "assistant" if message['user'] == bot_user_id else "user"
    message_text = clean_message(message_text, role, bot_user_id)
    return message_text


def update_chat(app, channel, messagets, text):
    """
    Method Update Chat
    """
    app.client.chat_update(
        channel=channel,
        ts=messagets,
        text=text
    )


