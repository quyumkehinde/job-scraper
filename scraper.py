import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

data = json.load(open('positions.json'))
response = []

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

for i in range(len(data)):
    driver.get(data[i]['url'])
    content = driver.page_source.lower()
    status = 'Not Found'
    found_keyword = ''
    for j in range(len(data[i]['keywords'])):
        if data[i]['keywords'][j].lower() in content:
            status = 'Found'
            found_keyword = data[i]['keywords'][j]
            break
    result = {
        'company': data[i]['company'],
        'url': data[i]['url'],
        'status': status,
        'found_keyword': found_keyword
    }
    response.append(result)
output = open('output.json', 'w')
json.dump(response, output, indent=2)

print('\n Open output.json to view result')
