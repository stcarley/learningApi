import requests
import json
import csv
from getToken import access_token as token

#----------------------------
# API Call
# Input - accesstoken and url
# Output - Return data in JSON
#----------------------------
def APIcall(token, url):

    # Make POST Headers
    headers = {
        "Authorization":"Bearer "+token
    }

    returnData = requests.get(url, headers=headers)
    print("Here is the request URL" + url)
    print("Here is the request URL" + returnData.text)
    return json.loads(returnData.text)


#----------------------------
# Open CSV and write header
#----------------------------
def makeCSV(token, coursePaginationURL):

    Rows = []

    # Open CSV and make header
    with open('Courses_CSV.csv','w') as csvfile:
        # Full CSV fieldnames
        #fieldnames = ['Course ID','Course Title','Author','Release Date','Level','Duration','Category','Categories','Skills','Description','Course URL','AICC URL','SSO URL','Thumbnail','Status','Library']

        #skills fieldnames
        fieldnames = ['Course ID','Course Title','Category','Categories','Skills']

        writer = csv.DictWriter(csvfile, extrasaction='ignore', fieldnames=fieldnames)

        writer.writeheader()

        # Get API data
        Rows = getRows(token, coursePaginationURL, Rows)

        for row in Rows:
            print(row)
            writer.writerow(row)

#----------------------------
# Get a rows data from an API element
#----------------------------
def getRows(token, coursePaginationURL, Rows):
    data = APIcall(token, coursePaginationURL)

    #prettyprint(data)

    #update output
    print("Processing: " + str(data['paging']['start']) + " of " + str(data['paging']['total']))

    for element in data['elements']:
        rowSkill = ''
        rowLibrary = ''
        rowSubject = ''

        for category in element['details']['classifications']:

            if category['associatedClassification']['type'] == 'SUBJECT':
                rowSubject = category['associatedClassification']['name']['value']

            if category['associatedClassification']['type'] == 'LIBRARY':
                rowLibrary = category['associatedClassification']['name']['value']

            if category['associatedClassification']['type'] == 'SKILL':
                if rowSkill != '':
                    rowSkill += ', '

                rowSkill += category['associatedClassification']['name']['value']
                print("skills  - " + rowSkill)

        # Assign approprate API values to each field in the CS

        row = {
            'Course ID': element['urn'],
            'Course Title':element['title']['value'],
            #'Course Skills'element['u']
            #'Author':element['details']['contributors'][0]['name']['value'].encode('utf-8').strip(),
            #'Release Date':time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(element['details']['publishedAt']/1000)),
            #'Level':'Not Available',
            #'Duration':str(datetime.timedelta(seconds=element['details']['timeToComplete']['duration'])),
            'Category':rowLibrary,
            'Categories':rowSubject,
            'Skills':rowSkill,
            #'Description':element['details']['description']['value'].encode('utf-8').strip()
            #'Course URL':element['details']['urls']['webLaunch'],
            #'AICC URL':element['details']['urls']['aiccLaunch'],
            'SSO URL':element['details']['urls']['ssoLaunch'],
            'Thumbnail':element['details']['images']['primary'],
            #'Status':element['details']['availability'],
            #'Library':element['details']['availableLocales'][0]['language']
        }
        print(row)
        Rows.append(row)

    debug = 'on'

    if debug == 'on':
        print("debug is on printing one row")

    elif data['paging']['links'][0]['rel'] == 'next':
        getRows(token, 'https://api.linkedin.com/' + data['paging']['links'][0]['href'], Rows)

    elif len(data['paging']['links']) > 1:
        if data['paging']['links'][1]['rel'] == 'next':
            getRows(token, 'https://api.linkedin.com/' + data['paging']['links'][1]['href'], Rows)


    return Rows



#----------------------------
# outputs JSON in a readable format
#----------------------------
def prettyprint(data):
    print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))




#Course URLs
#classificationURL = "https://api.linkedin.com/v2/learningClassifications?q=localeAndType&type=LIBRARY&sourceLocale.language=en&sourceLocale.country=US&start=0&count=1"
coursePaginationURL = "https://api.linkedin.com/v2/learningAssets?q=localeAndType&assetType=COURSE&sourceLocale.language=en&sourceLocale.country=US&expandDepth=1&includeRetired=false&start=0"

makeCSV(token, coursePaginationURL)







