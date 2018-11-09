import os
import requests
import json 

class SlackHistory:
	def __init__(self, token, channel, message_limit=None):
		self._token = token
		self._channel = channel
		self._message_limit = message_limit
		self._url = "https://slack.com/api/"

	def _get_channels(self):
		endpoint = "channels.list"
		url = '{}{}?token={}'.format(self._url, endpoint, self._token)
		headers = {"content_type":"application/x-www-form-urlencoded"}
		print(url)

		result = requests.get(url, headers=headers)
		return result.json()

	def _get_history(self):
		endpoint = "channels.history"
		payload = {
			"channel": self._channel,

		}

		url = '{}{}?token={}&channel={}&count=1000'.format(self._url, endpoint, self._token, payload["channel"])
		headers = {"content_type":"application/x-www-form-urlencoded"}

		##FIXME: Need to allow iterating to get all slack channel messages and collect therm into a list

		result = requests.get(url, headers=headers)
		return result.json()

if __name__ == '__main__':
	token = os.environ['SLACK_TOKEN']

	sh = SlackHistory(token, "CACG2BXDY")

	result = sh._get_channels()
	result2 = sh._get_history()


	

	print(len(result2["messages"]))