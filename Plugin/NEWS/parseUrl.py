import feedparser
import io
import unicodedata
import sys

file = open("/home/pi/Plugin/NEWS/festival_news.festival","wb")

fchanels=open("/home/pi/Plugin/NEWS/chanels.conf")
lines=fchanels.readlines()
rss_data=lines[int(sys.argv[1])-1]

feed = feedparser.parse(rss_data)

file.write('(voice_JuntaDeAndalucia_es_sf_diphone)') 

for item in feed["items"]:

	#item = item.title.encode('utf-8')
	item = item.title
	item = ''.join((c for c in unicodedata.normalize('NFD', item) if unicodedata.category(c) != 'Mn'))	
	file.write('(SayText "' + item + '")')
	print item

file.write('(quit)')
file.close()
fchanels.close()
