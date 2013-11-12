#!/usr/bin/env python
__author__ = "Gregory M Chen"
__copyright__ = "Copyright 2013, Gregory M Chen"

import urllib
import lxml.html
import re

# Get coauthor names from Google Scholar
connections = [
urllib.urlopen('http://scholar.google.ca/citations?hl=en&user=B7vSqZsAAAAJ&view_op=list_works&pagesize=100'),
urllib.urlopen('http://scholar.google.ca/citations?hl=en&user=B7vSqZsAAAAJ&pagesize=100&view_op=list_works&cstart=100')
]

links = list()

print "Searching links to citations..."
for connection in connections:
	dom =  lxml.html.fromstring(connection.read())
	for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
		if(re.match(r'^/citations\?view_op.*', link)):
			links.append(link)

for i in range(len(links)):
	links[i] = 'http://scholar.google.ca' + links[i]

first_names = []
last_names = []

print "Found " + str(len(links)) + ". Opening up each link and parsing the html for author names..."
count = 0
for link in links:
	response = urllib.urlopen(link)
	page_source = response.read()
	# Quick and dirty.
	m = re.search(r'Authors</div><div class="cit-dd">([^<]*)<', page_source)
	if not m:
		continue
	author_text = m.group(1)
	names = author_text.split(", ")
	for name in names:
		name = name.strip()
		split_name = name.split()
		if len(split_name) < 2:
			continue
		first_names.append(split_name[0].upper())
		last_names.append(split_name[-1].upper())
	count = count + 1
	if count % 10 == 0:
		print count

print "Comparing these author names to the Erdos1 data..."
# Get Erdos collaborator names

f = open('Erdos1.txt')
lines = f.readlines()

collab_first_names = []
collab_last_names = []

for line in lines:
	upper_line = line.strip().upper()
	split_line = upper_line.split(', ')
	if(len(split_line) < 2):
		continue
	
	# split_line is guaranteed to have a 0 and 1 index
	collab_last_names.append(split_line[0])
	collab_first_names.append(split_line[1].split()[0])

print "Printing to file..."
myfile = open('matches.txt', 'w')

# search for matches
for i in range(len(first_names)):
	for j in range(len(collab_first_names)):
		if(first_names[i] == collab_first_names[j] and last_names[i] == collab_last_names[j]):
			myfile.write(first_names[i] + "\t" + last_names[i] + "\n")
myfile.close()
print "Done! Printed to matches.txt."
