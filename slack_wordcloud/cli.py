"""
slack_worcloud
 
Usage:
  slack_wordcloud generate --channel <channel> [--token=token] [-f]
  slack_wordcloud -h | --help
  slack_wordcloud --version
 
Options:
  -h --help     Show this screen.
  --version     Show version.
  --token 	Slack API token.
  --channel 	Slack channel name.
  --file 	Ouput to file in current dir.
 
Examples:
  slack_wordcloud generate --channel my_channel
  slack_wordcloud generate --channel my_channel --token $API_TOKEN
  slack_wordcloud generate --channel my_channel --token $API_TOKEN --file
 
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/angel-hernandez91/slack-wordcloud
"""
 
 
from inspect import getmembers, isclass
 
from docopt import docopt
 
from . import __version__ as VERSION
 


	# Here we'll try to dynamically match the command the user is trying to run
	# with a pre-defined command class we've already created.
 
def main():
	"""Main CLI entrypoint."""
	import slack_wordcloud.commands
	options = docopt(__doc__, version=VERSION)

	for (k, v) in options.items(): 
		if hasattr(slack_wordcloud.commands, k) and v:
			module = getattr(slack_wordcloud.commands, k)
			slack_wordcloud.commands = getmembers(module, isclass)
			command = [command[1] for command in slack_wordcloud.commands if command[0] != 'Base'][0]

			command = command(options)
			command.run()