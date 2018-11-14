from . import SlackHistory
from .base import Base
from wordcloud import WordCloud
import os

class Base:
	def __init__(self, options, *args, **kwargs):
		self.options = options
		self.args = args
		self.kwargs = kwargs

	def generateWordCloud(self, text, channel, save_image=None):
		flat_text = " ".join(text)
		wordcloud = WordCloud(width=600,height=400,collocations=False).generate(flat_text)

		if save_image is True:
			wordcloud.to_file("{}_wordcloud.png".format(channel))

		image = wordcloud.to_image()
		image.show()


# if __name__ == '__main__':
# 	token = os.environ['SLACK_TOKEN']
# 	channel = 'cdl'
# 	text = SlackHistory.SlackHistory(token, channel).getAllHistory()

# 	wc = GenerateWordCloud(text).generateWordCloud()
