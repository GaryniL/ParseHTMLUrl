#!/usr/bin/env python
import sys
import re


def main():
	filename = "test.html" #default file name

	# if no filename argument
	if len(sys.argv) >= 2:
		filename = sys.argv[1]
	
	try:
		with open(filename, 'r') as myfile:
			print "Proceed file: \"%s\"" % filename
			data = myfile.read().replace('\n', '')

			urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)

			if len(urls) > 0:
				print
				for url in urls:
					print url
				print "\n[Result] Found ",len(urls)," url links"
			else:
				print "[Result] Nothing found"

	except Exception: 
		print "[Error] No such file\n";
		return

if __name__ == "__main__":
	main()
