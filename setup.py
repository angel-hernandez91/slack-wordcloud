import setuptools

with open('README.md', 'r') as rm:
	long_description = rm.read()

setuptools.setup(
	name='slack_wordcloud',
	version='1.0.3',
	description='Generate word clouds for Slack channels!',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='Angel Hernandez',
	url='https://github.com/angel-hernandez91/slack-wordcloud',
	author_email='ahernandez0691@gmail.com',
	license='MIT',
	packages=setuptools.find_packages(),
	zip_safe=False,
	install_requires=['docopt', 'wordcloud', 'requests'],
	keywords=['cli', 'slack', 'wordcloud', 'app'],
	classifiers= [
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	entry_points = {
        'console_scripts': [
            'slack_wordcloud=slack_wordcloud.cli:main',
        ],
    }


	)