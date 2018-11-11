from SlackHistory import SlackHistory
from wordcloud import WordCloud
import os

class GenerateWordCloud:
	def __init__(self, text):
		self._text = text

	def generateWordCloud(self):
		text = " ".join(self._text)
		wordcloud = WordCloud().generate(text)
		# The pil way (if you don't have matplotlib)
		wordcloud.to_file("{}.png".format(channel))
		image = wordcloud.to_image()
		image.show()


if __name__ == '__main__':
	token = os.environ['SLACK_TOKEN']
	channel = 'cdl'
	text = SlackHistory(token, channel).getAllHistory()

	wc = GenerateWordCloud(text).generateWordCloud()
