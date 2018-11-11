# Slack Wordcloud
This package is intended to take the history of a given Slack Channel, and run it through a Python Wordcloud API, and generate a wordcloud image.

This package uses the `channels.history` Slack endpoint and will require a valid Slack API Token.

## Installation
1. *pip-install pending*

## Classes
1. `SlackHistory(token, channel)`
2. `GenerateWordCloud(channel_text)`

## Command Line Usage
1. `slack-wordclound --token <SLACK_API_TOKEN> --channel <CHANNEL_NAME> [OUT_FILE_NAME]`
