import os 
import json
import csv
import argparse

class GetWordList:
	def __init__(self, directory):
		self._directory = directory
		self._general_channel = []

	def _get_files(self):
		directory = os.listdir(self._directory)

		for file in directory:
			file_path = os.path.join(self._directory, file)
			try:
				self._general_channel.append(open(file_path).read())
			except UnicodeDecodeError:
				pass

		return self._general_channel

	def _get_text(self):
		word_list = self._get_files()
		text_list = []

		for words in word_list:
			text = json.loads(words)
			for t in text:
				text_list.append(t['text'])
			
		return text_list

	def write_list(self):
		text_list = self._get_text()

		with open('word_list.txt.', 'w', newline='') as OUT:
			wr = csv.writer(OUT)
			for text in text_list:
				wr.writerow([text])


if __name__ == '__main__':
	argsparser = argparse.ArgumentParser()
	argsparser.add_argument('directory')
	args = argsparser.parse_args()
	directory = args.directory

	wordList = GetWordList(directory)


	wordList.write_list()

