from SlackHistory import SlackHistory
from wordcloud import WordCloud
import os

class GenerateWordCloud:
	def __init__(self, text):
		self._text = text

	def generateWordCloud(self, save_image=None):
		text = " ".join(self._text)
		wordcloud = WordCloud(width=600,height=400,collocations=False).generate(text)

		if save_image is True:
			wordcloud.to_file("{}_wordcloud.png".format(channel))

		image = wordcloud.to_image()
		image.show()


if __name__ == '__main__':
	token = os.environ['SLACK_TOKEN']
	channel = 'cdl'
	text = SlackHistory(token, channel).getAllHistory()

	wc = GenerateWordCloud(text).generateWordCloud()
