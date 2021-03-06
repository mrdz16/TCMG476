#! /usr/bin/python
import urllib2
response = urllib2.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')
html = response.read()

print('(1) How many total requests were made in the time period represented in the log?')
print('(2) How many requests were made on each day? per week? per month?')
print('(3)What percentage of the requests were not successful (any 4xx status code)?')
print('(4)What percentage of the requests were redirected elsewhere (any 3xx codes)?')
print('(5)What was the most-requested file?')
print('(6)What was the least-requested file?')
print('(7) quit')
answer = int(input('Choose a question to answer:'))

if answer == 1:
	lines = len(html.splitlines())
	print('Total request made:',lines)

if answer == 3:
	fail = 0
	for line in html.splitlines():
		if (line.split('" ')[-1][0]) == '4':
			fail += 1
	print float(fail) / 726736 * 100, '%'

if answer == 4:
	redir = 0
        for line in html.splitlines():
                if (line.split('" ')[-1][0]) == '3':
                        redir += 1
        print float(redir) / 726736 * 100, '%'
