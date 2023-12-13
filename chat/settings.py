import os

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", None)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN", None)

CHUNK_SIZE = 200

MODEL = "gpt-3.5-turbo"

SYSTEM_PROMPT = '''
Eres un asistente de IA.
Responderás la pregunta con la mayor sinceridad posible.
Si no está seguro de la respuesta, diga lo siento, no lo sé la respuesta.
'''
