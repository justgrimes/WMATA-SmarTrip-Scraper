# Simple python screen scraper for WMATA SmarTrip Card Usage History Data
# Scrapes data from WMATA's website and returns clean CVS file of SmarTrip Card Usage History.
# NOTES - ONLY THING NECESSARY IS TO ADD USER NAME AND PASSWORD IN CODE 

# importing libs
import BeautifulSoup, mechanize, csv, sys, datetime, re

now = datetime.datetime.now()

br = mechanize.Browser()
br.open("https://smartrip.wmata.com/Account/AccountLogin.aspx") #login page

br.select_form(nr=0) #form name
br["ctl00$MainContent$txtUsername"] = "" #<-- enter your username here
br["ctl00$MainContent$txtPassword"] = "" #<-- enter your password here

response1 = br.submit().read()

if len(sys.argv) == 1:
	# download the first card, but show all card names so the user can choose
	
	print "Available cards are..."
	for cards in re.findall(r"CardSummary.aspx\?card_id=(\d+)\">(.*?)<", response1):
		print cards[0], cards[1]
	print ""
	print "And you can specify a card number on the command line!"
	print
	
	matching_card = re.search(r"CardSummary.aspx\?card_id=(\d+)\">(.*?)<", response1)
	if not matching_card: raise Exception("card not found")
	card_id = matching_card.group(1)
	card_name = matching_card.group(2)

	print "Downloading data for...", card_id, card_name

else:
	# download just one card's data
	card_id = sys.argv[1]

#follows link to View Card Summary page	for a particular card
response1 = br.follow_link(url_regex=r"CardSummary.aspx\?card_id=" + card_id).read()

#follows link to View Usage History page for a particular card
response1 = br.follow_link(text_regex=r"View Usage History").read()

br.select_form(nr=0)

response1 = br.submit().read()

br.select_form(nr=0)

#transaction status either 'All' or 'Successful' or 'Failed Autoloads'; All includes every succesful transaction including failed (card didn't swipe or error)  
br["ctl00$MainContent$ddlTransactionStatus"] = ["All"]

br.submit()

#write files
g = csv.writer(open('wmata_log_' + card_id + '.csv', 'w'))

#wmata only started posting data in 2010, pulls all available months
for year in xrange(2010, now.year+1):
	for month in xrange(1, 12+1):
		time_period = ("%d%02d" % (year, month))
		print "\t", time_period

		try:
			#opens link to 'print' version of usage page for easier extraction 
			br.open("https://smartrip.wmata.com/Card/CardUsageReport2.aspx?card_id=" + card_id + "&period=M&month=" + time_period)
			response1 = br.follow_link(text_regex=r"Print Version").read()
		except:
			continue
			
		#extracts data from html table, writes to csv
		soup = BeautifulSoup.BeautifulSoup(response1)
		t = soup.findAll('table')[1:]

		for table in t:
			rows = table.findAll('tr')
			for tr in rows:
				cols = tr.findAll('td')
				g.writerow( [str(td.find(text=True)) for td in cols] )
