# Slack Wordcloud
This package is intended to take the history of a given Slack Channel, and run it through a Python Wordcloud API, and generate a wordcloud image. Compatibile with Python 3.7+.

This package uses the `channels.history` Slack endpoint and will require a valid Slack API Token.

## Installation
1. `pip install slack-wordcloud`
2. `docopt` and `wordcloud` are also required and can be installed via `pip`
	* `pip install docopt wordcloud`

## Classes
1. `SlackHistory(token, channel)`
2. `GenerateWordCloud(options, *args, **kwargs)`

## Command Line Usage
1. `slack-wordclound [-f] --channel <CHANNEL_NAME> [--token=SLACK_TOKEN]`
	* `-f` will create a png file in your current directory of the output
	* `--channel` is required. Any valid slack channel.
	* `--token` optional argument if the token is already in your environment. Otherwise, you will need to pass it in.
