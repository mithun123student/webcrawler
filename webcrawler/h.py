from urllib import *
urlText=urlopen("http://www.google.com").read()
countofLinks = urlText.count("<a href=")



i=0
while(i<countofLinks):
#print urlText[firstHref:]
#print firstHref
#print firstHref + endIndex
#print countofLinks
    firstHref = urlText.find("http://")
    #firstHref=firstHref-1
    endIndex = urlText[firstHref:].find('"')
    endIndex=firstHref+endIndex
    print "link is ->"
    print urlText[firstHref:endIndex]
    urlText=urlText[endIndex:]
    i=i+1
