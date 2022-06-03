import requests # getting the content of the TED Talk page
from bs4 import BeautifulSoup # web scraping, process text
import re # pattern matching
import os # path
import sys # arguments parsing at a terminal

# Exception Handling
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

file_name = url.split('/')[-1]

r = requests.get(url)

print('Download is about to start')

soup = BeautifulSoup(r.content, features='html.parser')

for val in soup.find_all("script", attrs={'id':'__NEXT_DATA__'}):
    if re.search(".mp4", str(val)) is not None:
        result = str(val)
        break

# print(result)
result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group(0)

print("Downloading video from ..... " + result_mp4)

r = requests.get(result_mp4) # it may take a few seconds

file_path = os.path.join(os.getcwd(), 'download/' + file_name + '.mp4')
with open(file_path, 'wb') as f:
    f.write(r.content)


