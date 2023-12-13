# ChatGPT for Slack Bot

This is a simple chatbot that uses the  package to respond to messages in Slack. It is designed to be used with the Slack Events API, and it listens for app_mention events, which are triggered when a user mentions the bot in a Slack channel.

Dependencies
============
See ```requirements.txt```

Installation
============
1. Clone this repository.
  ```
  git clone https://github.com/thomgonzalez/GPTSlackBot.git
  ```
2. Install the required packages.
  ```
   pip install -r requirements.txt
  ```
3. Edit the .app.env file in the root directory of the project and add your Slack and OpenAI API keys.
  ```
  export SLACK_BOT_TOKEN=slack_bot_token
  export SLACK_APP_TOKEN=slack_app_token
  export OPENAI_API_KEY=you_openai_api_key
  ```
Alternatively, you can use the containerized version by setting the environment variables in the variables.env file and then run:
  ```
  docker-compose up -d
  ```

Usage
=====
Once the bot is running, you can mention it in a Slack channel to send it a message. For example
1. Start the bot:
```python
# run with virtual environment
python app.py
# run with docker
docker-compose up -d
```
2. Invite the bot to your desired Slack channel.
3. Mention the bot in a message and ask a question.

## License
This project is released under the terms of the GNU GPL 3.0 license. For more information, see the [LICENSE](LICENSE) file included in the repository.
