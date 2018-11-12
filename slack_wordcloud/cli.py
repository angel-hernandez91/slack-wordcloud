"""
slack_worcloud
 
Usage:
  slack_wordcloud hello 
  slack_wordcloud -h | --help
  slack_wordcloud --version
 
Options:
  -h --help                         Show this screen.
  --version                         Show version.
 
Examples:
  slack_wordloud generate [SLACK_TOKEN] [CHANNEL] [OUTFILE]
 
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/angel-hernandez91/slack-wordcloud
"""
 
 
from inspect import getmembers, isclass
 
from docopt import docopt
 
from . import __version__ as VERSION
 
 
def main():
    """Main CLI entrypoint."""
    from . import commands
    options = docopt(__doc__, version=VERSION)
 
    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for k, v in options.items():
      print(k)  
      print(commands)
      print(hasattr(commands, 'Hello'))
      if hasattr(commands, k):
          module = getattr(commands, k)
          commands = getmembers(module, isclass)
          print(commands)
          command = [command[1] for command in commands if command[0] != 'Base'][0]
          command = command(options)
          command.run()