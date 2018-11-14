from . import SlackHistory
from .generate_base import Base
from wordcloud import WordCloud
import os

class GenerateWordCloud(Base):
	def __init__(self, options, *args, **kwargs):
		super().__init__(self, options, *args, **kwargs)

	def run(self):
		print(self.args[0])
		try:
			token = os.environ['SLACK_TOKEN']
		except KeyError:
			token = self.args[0]['--token']

		channel = self.args[0]['--channel']
		text = SlackHistory.SlackHistory(token, channel).getAllHistory()

		
		try:
			if self.args[0]['-f'] is True:
				wc = self.generateWordCloud(text, channel, True)
		except KeyError:
			wc = self.generateWordCloud(text, channel)

# if __name__ == '__main__':
# 	token = os.environ['SLACK_TOKEN']
# 	channel = 'cdl'
# 	text = SlackHistory.SlackHistory(token, channel).getAllHistory()

# 	wc = GenerateWordCloud(text).generateWordCloud()
