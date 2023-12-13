# ChatGPT for Slack Bot

This is a simple chatbot that uses the  package to respond to messages in Slack. It is designed to be used with the Slack Events API, and it listens for app_mention events, which are triggered when a user mentions the bot in a Slack channel.

## Installation
The next step is to install the necessary dependencies such as slack-bolt, slack and openai. The Slack-Bolt package is a set of tools and libraries that allow developers to quickly and easily create Slack applications. It provides an easy-to-use API for building bots, custom integrations, and Slack app features. You can install these dependencies by running the following command in your terminal.

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

## Register an app with Slack and obtain tokens
The first step in integrating ChatGPT with Slack is to register an app with Slack and obtain the Slack Bot Token and Slack App Token. To do this, follow these steps:

1. Log in to your Slack workspace.
2. Go to the Slack API website.
3. Click on “Create an app” and select “From scratch”
4. Give your app a name, select your Slack workspace
5. In Basic information > Add features and functionality. Click on “Permissions” and in Scopes add in Bot Token Scopes: app_mentions:read ; channels:history ; channels:read ; chat:write
6. In settings, click on “Socket Mode”, enable it and give the token a name. Copy the Slack Bot App Token (starts with xapp)
7. In Basic information > Add features and functionality. Click on “Event Subscriptions” and enable it. Furthermore in “Subscribe to bot events” select “app_mention”. Save changes.
8. Go to the “OAuth & Permissions” section and install your app to your workspace
9. Copy the Slack Bot Token (starts with xoxb)

## Obtain the OpenAI API key
The next step is to obtain the OpenAI API key. Why? Will need to connect to OpenAI’s API in order to use their GPT-3 API. If you are new to this, no problem, you’ll get 18$ for free without having to provide a credit card. To generate an API key, follow these steps:

1. Go to the OpenAI API website
2. Log in or sign up for an OpenAI account
3. Go to the API Key section and create a new API key
4. Copy the API key

## Usage
Fill in the 3 tokens that you created above in the script below and run the application. The app will listen to events in which he is tagged, once that happens a message is shown to the user that the bot is working on an answer. Next, the question is sent to a GPT-3 model and finally returned to the user.

1. Start the bot:
```python
# run with virtual environment or 
python app.py
# run with docker
docker-compose up -d
```
2. Invite the bot to your desired Slack channel.
3. Mention the bot in a message and ask a question.

## License
This project is released under the terms of the GNU GPL 3.0 license. For more information, see the [LICENSE](LICENSE) file included in the repository.
