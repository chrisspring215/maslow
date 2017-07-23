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

# This is working it just takes forever. The range should be set to listOfCategoriesHrefsLength
for i in range(listOfCategoriesHrefsLength):

    alpha = indexCat = requests.get(baseURL + listOfCategoriesHrefs[i])
    beta = html.fromstring(alpha.content)
    theta = beta.xpath('//div[@class="paginationContent"]/ul/li')
    indexCat = requests.get(baseURL + listOfCategoriesHrefs[i])
    bizTree = html.fromstring(indexCat.content)
    thetaLength = len(theta)

    print (thetaLength / 2) - 1

    

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
