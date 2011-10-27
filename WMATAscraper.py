# Simple screen scraper for WMATA SmarTrip Card Usage History
# Scrapes data from WMATA's website and returns clean CVS file of SmarTrip Card Usage History.

import re
import urllib
import urllib2 #extensible lib for opening urls
import BeautifulSoup #Beautiful Soup lib for html parsing
import mechanize
#import cookielib #coookie lib does what? gens cookie?

#cookie storage
#cj = cookielib.CookieJar()

#create an opener
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#opener.addheaders.append(('User-agent', 'Mozilla/4.0'))
#opener.addheaders.append( ('Referer', 'http://www.yahoo.com') )

#login_data = urllib.urlencode({'ctl00$MainContent$txtUsername' : '<user>','ctl00$MainContent$txtPassword' : '<password>','ctl00$MainContent$btnSubmit' : 'Login'})

#resp = opener.open('https://smartrip.wmata.com/Account/AccountLogin.aspx',login_data)
#print resp

#y = urllib2.urlopen("https://smartrip.wmata.com/Account/Account/AccountLogin.aspx __EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKLTc2NDI3NTcwNWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFG2N0bDAwJE1haW5Db250ZW50JGJ0blN1Ym1pdE0N4FFqxxyFKGzFZmwweg441M%2BY&__EVENTVALIDATION=%2FwEWBAKU97HPCgKMrfvLAgKOsPfSCQL25qnqCCr34JdQTPtmshm%2BHfM4dclmab88&ctl00%24MainContent%24txtUsername=justgrimes&ctl00%24MainContent%24txtPassword=four28&ctl00%24MainContent%24btnSubmit.x=27&ctl00%24MainContent%24btnSubmit.y=15") 
#print y.read()

#br = mechanize.Browser()
#br.open("https://smartrip.wmata.com/Account/AccountLogin.aspx")
#response1 = br.open("https://smartrip.wmata.com/Account/AccountLogin.aspx")
#assert br.viewing_html()
#print br.title() #ascii simple out of range bad metro
#print response1.geturl()
#print response1.info()  # headers

#for form in br.forms():
#       print form

login_data = urllib.urlencode({'ctl00$MainContent$txtUsername' : '<username>','ctl00$MainContent$txtPassword' : '<password>'})
rq = mechanize.Request("https://smartrip.wmata.com/Account/AccountLogin.aspx", login_data)
rs = mechanize.urlopen(rq)
data = rs.read()

print data

#print response1.read()  # body
#br.select_form(name="aspnetForm")

#response2 = br.submit()

#print br.form
#resp.close()

#once the data is pulled down, load files and use beautiful soup to extract data from HTML table and write to csv
#f = open("jan2011.html","r")
#g = open("output.csv","w")


#soup = BeautifulSoup.BeautifulSoup(f)
#t = soup.findAll('table')[1:]

#for table in t:
#	rows = table.findAll('tr')
# 	for tr in rows:
#		cols = tr.findAll('td')
#		for td in cols:
#			g.write(str(td.find(text=True)))
#			g.write(",")
#		g.write("\n")
