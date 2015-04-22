# curl -s http://community.livejournal.com/_fandom_icons_/2001/07/29/
# http://community.livejournal.com/_fandom_icons_/2001/09/06/


import urllib
from bs4 import BeautifulSoup

#url = 'http://community.livejournal.com/_fandom_icons_/2001/07/29/'
url = 'http://community.livejournal.com/_fandom_icons_/2001/09/06/'
data = urllib.urlopen(url).read()
soup = BeautifulSoup(data)

alert = "this user's account is deleted and purged"

def get_date():
	date = soup.select('.date')[0].text.strip()
	return date
	#print date

def get_caption():
	caption = soup.select('.entry_text b')[1].text.strip()
	return caption
	#print caption

def get_user_name():
	username = soup.select('.i-ljuser-username')[0].text.strip()
	return username
	#print username

print get_date()
print get_caption()
print '- ' + get_user_name()
print alert



# TODO: 
# only use deleted users: if class="i-ljuser-deleted" == true

