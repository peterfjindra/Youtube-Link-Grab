"""
ytlinkgrab.py

Script which reads a text file containing html of a youtube playlist
or youtube page containing links to videos and pastes valid links
to all of the videos in a new text file.

author: Peter Jindra
"""

from re import findall
import codecs

html_input = ""

with codecs.open("html_input.txt", 'r', 'utf-8') as f:
    for line in f:
    	html_input += line
f.close()

links = findall("/watch.+?;", html_input)
new_links = set()
old_links = set()

for link in links:
	new_links.add("youtube.com" + link[:-1] + '\n')

with open("backlog.txt") as backlog:
	for line in backlog:
		old_links.add(line)
backlog.close()
#we now have a set of old links and a set of new links

newfile = open("newurls.txt", 'w')
oldfile = open("backlog.txt", 'a')

for link in new_links:
	if link not in old_links:
		newfile.write(link)
		oldfile.write(link)

newfile.close()
oldfile.close()
