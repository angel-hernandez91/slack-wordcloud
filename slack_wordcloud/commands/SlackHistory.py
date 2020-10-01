import os
import requests
import json 
import time

class InvalidResponseException(Exception): pass

class SlackHistory:
	def __init__(self, token, channel, message_limit=None):
		self._token = token
		self._message_limit = message_limit
		self._url = "https://slack.com/api/"
		self._channel = self._create_channel_map()[channel]

	def _get_channels(self):
		endpoint = "conversations.list"
		url = '{}{}?token={}'.format(self._url, endpoint, self._token)
		headers = {"content_type":"application/json"}

		result = requests.get(url, headers=headers)
		r = result.json()
		if 'error' in r.keys():
			raise InvalidResponseException(r['error'])
		return r

	def _get_history(self, timestamp=None):
		endpoint = "conversations.history"
		payload = {
			"channel": self._channel,

		}
		
		if self._message_limit is not None:
			url = '{}{}?token={}&channel={}&count={}'.format(self._url, endpoint, self._token, payload["channel"], self._message_limit)
		else:
			url = '{}{}?token={}&channel={}&count={}'.format(self._url, endpoint, self._token, payload["channel"], 1000)
		headers = {"content_type":"application/x-www-form-urlencoded"}

		if timestamp is not None and self._message_limit is None:
			url = '{}&inclusive=False&latest={}'.format(url, timestamp)

		result = requests.get(url, headers=headers)
		r = result.json()
		if 'error' in r.keys():
			raise InvalidResponseException(r['error'])
		return r

	def _create_channel_map(self):
		channels = self._get_channels()['channels']

		name_id_mapping = {}
		for channel in channels:
			name_id_mapping[channel['name']] = channel['id']

		return name_id_mapping

	def getAllHistory(self):
		message_store = []
		timestamp_store = []

		result = self._get_history()
		if result['has_more'] == True:
			has_more = True
			for message in result['messages']:
				message_store.append(message['text'])
				timestamp_store.append(float(message['ts']))

			min_ts = min(timestamp_store)
			while has_more:
				result = self._get_history(min_ts)
				has_more = result['has_more']

				for message in result['messages']:
					message_store.append(message['text'])
					timestamp_store.append(float(message['ts']))

				min_ts = min(timestamp_store)
				time.sleep(2)

		return message_store



if __name__ == '__main__':
	token = os.environ['SLACK_TOKEN']
	channel = 'data_science_general'

	sh = SlackHistory(token, channel)

	result = sh.getAllHistory()

	print(result)

	
