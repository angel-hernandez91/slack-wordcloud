# Slack Wordcloud
This package is intended to take the history of a given Slack Channel, and run it through a Python Wordcloud API, and generate a wordcloud image.

This package uses the `channels.history` Slack endpoint and will require a valid Slack API Token.

## Installation
1. `pip install slack_wordcloud`
2. `docopt` and `wordcloud` are also required. Can be installed via `pip`

## Classes
1. `SlackHistory(token, channel)`
2. `GenerateWordCloud(options, *args, **kwargs)`

## Command Line Usage
1. `slack-wordclound [-f] --channel <CHANNEL_NAME> [--token=SLACK_TOKEN]`
	* `-f` will create a png file in your current directory of the output
	* `--channel` is required. Any valid slack channel.
	* `--token` option argument. It will check your environment first, and fail if not present.