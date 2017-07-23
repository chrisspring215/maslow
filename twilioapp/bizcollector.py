from lxml import html
import requests

# Base URl for the site
baseURL = 'http://businessfinder.mlive.com'

# Source of the biz index
index = requests.get('http://businessfinder.mlive.com/MI-Ann-Arbor')

# Creates a tree of all the biz categories
indextree = html.fromstring(index.content)

# Grabs the href for each categories
listOfCategoriesHrefs = indextree.xpath('//div[@class="group"]/ul/li/a//@href')

# finds the length of the index categories for the for loop
listOfCategoriesHrefsLength = len(listOfCategoriesHrefs)

bizs = []

# For every category...
for i in range(listOfCategoriesHrefsLength):

    # Open each category
    a = requests.get(baseURL + listOfCategoriesHrefs[i])
    # Create a tree with the DOM structure
    b = html.fromstring(a.content)
    # Look through that tree to find how many pages are within the category (pagination)
    c = b.xpath('//div[@class="paginationContent"]/ul/li')
    # If the category only has one page, look for results on the page
    if c == []:
        cc = b.xpath('//div[@class="innerDetailsSubLeft"]/div[contains(@class, "resultWrapper")]/div[@class="resultInner "]/h3/a/text()')
        if cc == []:
            #do nothing
        else:
            print "have a party"
    else:
        print "multi pages"


    d = len(c) 
    # This is the true number of pages, will sometimes be -1 since some pages have no results
    e = d / 2 - 1
   
    # This is the results on each page
    h = b.xpath('//div[@class="innerDetailsSubLeft"]/div[contains(@class, "resultWrapper")]/div[@class="resultInner "]/h3/a/text()')

    # This is the number of results on each page
    j = len(h)
    
    #for x in range(e):
        #print j
        #if e == 1:
        #    h = b.xpath('//div[@class="resultInner "]/h3//@title')
        #    print h
        # Elif category is empty
        #elif e == -1:
        #    print "do nothing"
        #else:
        #    print "do nothing"



    # other for loop goes here !!!!!
    #bizsGroup = bizTree[i].xpath('//div[@class="resultInner reviews"]/h3//@title ')
    #bizs = bizTree.xpath('//div[@class="resultInner reviews"]/h3/a//text()')
    #bizs.append(bizsGroup)
    #print bizTree[i].xpath('//div[@class="resultInner reviews"]/h3//@title ')
   
# Creates a tree of each categories results page (they are paginated so figure that out)
#categorieTree = html.fromstring(indexCats.content)

# Grabs the name of each biz
#category = categorieTree.xpath('//div[@class="resultInner "]/h3/a/text()')
#cattree.join(cat)

#print cattree
#    if i = 0:
#        # Concats the Base URL and the href
#        indexCat = requests.get(baseURL + indexCats[0])
#    else:
#        indexCat = requests.get(baseURL + indexCats[0] + )
