# TED Talk Downloader

## Description
A tool for downloading videos from TED Talk

## Packages
`pip install -r /path/to/requirements.txt`

## Instructions
Example URL: https://www.ted.com/talks/bernhard_kowatsch_how_innovation_and_technology_can_fight_global_hunger

Open a terminal and run `python3 main.py [Give your URL here]`

## Explanation
- `requests`: A package that helps us to get the web content
- A http request represents how the communication between a server and a client happens
- `BeautifulSoup`: Extract data out of XML and HTML

## Lessons learned
- Basic knowledge of the `requests` package
- Building the basic script to download videos
- Using `sys` to get arguments from terminal