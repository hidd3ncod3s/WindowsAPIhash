from bs4 import BeautifulSoup
import urllib2
import time

domain= "http://www.processlibrary.com"

urlstoprocess= [domain + "/en/directory/a/1/", 
                domain + "/en/directory/b/1/", 
				domain + "/en/directory/c/1/", 
				domain + "/en/directory/d/1/", 
				domain + "/en/directory/e/1/", 
				domain + "/en/directory/f/1/", 
				domain + "/en/directory/g/1/", 
				domain + "/en/directory/h/1/", 
				domain + "/en/directory/i/1/", 
				domain + "/en/directory/j/1/", 
				domain + "/en/directory/k/1/", 
				domain + "/en/directory/l/1/", 
				domain + "/en/directory/m/1/", 
				domain + "/en/directory/n/1/", 
				domain + "/en/directory/o/1/", 
				domain + "/en/directory/p/1/", 
				domain + "/en/directory/q/1/", 
				domain + "/en/directory/r/1/", 
				domain + "/en/directory/s/1/", 
				domain + "/en/directory/t/1/", 
				domain + "/en/directory/u/1/", 
				domain + "/en/directory/v/1/", 
				domain + "/en/directory/w/1/", 
				domain + "/en/directory/x/1/", 
				domain + "/en/directory/y/1/", 
				domain + "/en/directory/z/1/", 
				domain + "/en/directory/other/1/"
]

file_write = open('filelist.txt','w')

def outputme(data):
	data= data + "\n"
	try:
		file_write.write(data)
		file_write.flush();
	except:
		return;
				
def processnexturl():
	url=urlstoprocess.pop();
	print url;
	response = urllib2.urlopen(url)
	html = response.read()
	#print html
	soup = BeautifulSoup(html)
	listingdiv= soup.find("div", {"id": "listing"})
	paginationdiv= soup.find("div", {"id": "pagination"})
	
	if listingdiv is not None:
		#print "found listingdiv";
		#print listingdiv
		listringchilds= listingdiv.findAll('a');
		#print listringchilds
		for achild in listringchilds:
			outputme(achild.text);
	
	if paginationdiv is not None:
		#print "found paginationdiv";
		#print paginationdiv
		paginationchilds= paginationdiv.findAll('a');
		#print paginationchilds
		nexturl= ''
		foundCurrentSib= False;
		for achild in paginationchilds:
			if foundCurrentSib == True:
				nexturl= domain + achild['href'];
				break;
			if (domain + achild['href']) == url:
				foundCurrentSib= True;
			#print achild['href'];
		#print nexturl;
		
		if nexturl != '':
			urlstoprocess.append(nexturl);
		
while(len(urlstoprocess)):
	processnexturl();
	time.sleep(1);
	