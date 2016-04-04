############################################################
#
#    Author: Brian Keenan
#    Function: Python script to update the menu from local 
#    html page loading the data to the cloud @ parse.com
#    Date: Oct 2013
#
############################################################

import requests,json,httplib
from BeautifulSoup import BeautifulSoup

monMenu = []
tuesMenu = []
wedMenu = []
thursMenu = []
friMenu = []

def formatString(menuItem):
    a = menuItem.replace('\n', ' ')
    b = a.replace('  ', ' ')
    c = b.replace('&amp;', '&')
    return c

def Scrape(dayfile, menuArray):
    with open(dayfile) as f:
        data = f.read()

    soup = BeautifulSoup(data)
    for node in soup.findAll('p'):
        item = ''.join(node.findAll(text=True)).strip()
        menuArray.append(formatString(item))
    
############################################################
#    1. Scrape the html file and extract texts to an Array
############################################################

monfile = r"\\irdubweb.dub.sap.corp\restaurant_public\DUBMenu\Monday.htm"
tuesfile = r"\\irdubweb.dub.sap.corp\restaurant_public\DUBMenu\Tuesday.htm"
wedfile = r"\\irdubweb.dub.sap.corp\restaurant_public\DUBMenu\Wednesday.htm"
thursfile = r"\\irdubweb.dub.sap.corp\restaurant_public\DUBMenu\Thursday.htm"
frifile = r"\\irdubweb.dub.sap.corp\restaurant_public\DUBMenu\Friday.htm"
#When testing at home use local link
#monfile = r"C:\Users\I027737\Desktop\Monday.htm"


#1.monday
Scrape(monfile, monMenu)
#2.tuesday
Scrape(tuesfile, tuesMenu)
#3.wednesday
Scrape(wedfile, wedMenu)
#4.thursday
Scrape(thursfile, thursMenu)
#5.friday
Scrape(frifile, friMenu)

############################################################
#    2. Load the array in JSON format
############################################################
JSONfile = json.dumps({"JSONMenu": {"menu" : [
		{
                "date":str(monMenu[2]),
		"day":"Monday",
		"starter1":str(monMenu[4]),
		"starter2":str(monMenu[5]),
		"main1":str(monMenu[7]),
		"main2":str(monMenu[8]),
		"mainveg":str(monMenu[9]),
		"dessert":str(monMenu[12])
		},
		{
                "date":str(tuesMenu[2]),
		"day":"Tuesday",
		"starter1":str(tuesMenu[4]),
		"starter2":str(tuesMenu[5]),
		"main1":str(tuesMenu[7]),
		"main2":str(tuesMenu[8]),
		"mainveg":str(tuesMenu[9]),
		"dessert":str(tuesMenu[11])
		},
		{
                "date":str(wedMenu[2]),
		"day":"Wednesday",
		"starter1":str(wedMenu[4]),
		"starter2":str(wedMenu[5]),
		"main1":str(wedMenu[8]),
		"main2":str(wedMenu[9]),
		"mainveg":str(wedMenu[10]),
		"dessert":str(wedMenu[13])
		},
		{
                "date":str(thursMenu[2]),
		"day":"Thursday",
		"starter1":str(thursMenu[4]),
		"starter2":str(thursMenu[5]),
		"main1":str(thursMenu[7]),
		"main2":str(thursMenu[8]),
		"mainveg":str(thursMenu[9]),
                "dessert":str(thursMenu[11])
		},
		{
                "date":str(friMenu[2]),
		"day":"Friday",
		"starter1":str(friMenu[3]),
		"starter2":str(friMenu[4]),
		"main1":str(friMenu[6]),
		"main2":str(friMenu[7]),
		"mainveg":str(friMenu[8]),
		"dessert":str(friMenu[10])
		},
	]
}})

############################################################
#    3. Load the Data to Parse.com via Proxy
############################################################

#CREATE
connection = httplib.HTTPConnection('proxy', 8080)
connection.connect()
connection.request('POST', 'https://api.parse.com/1/classes/Menu', JSONfile, {
       "X-Parse-Application-Id": "gar1pcHESbLE9dolZdh71VvCzoHjO4gg8xJKo3YW",
       "X-Parse-REST-API-Key": "e5t80DQAUJjtnSUwsJtiderayDa315MPmmXn9yrJ",
       "Content-Type": "application/json"
     })
result = connection.getresponse().read()
print result








