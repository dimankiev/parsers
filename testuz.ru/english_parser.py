#!/usr/bin/python3
import requests, re
from bs4 import BeautifulSoup

print("testuz.ru english test parser (v. 1.0.0b)")
print("by dimankiev | https://github.com/dimankiev")

template = "http://testuz.ru/eng_test.php?id="
parsed = {}
pattern = re.compile('''<table class='test'>[\s\S]*?<\/table>''')

boundaries = [int(input("Please, enter the first question's ID: ")), int(input("Please, enter the last question's ID: "))]

parsedFile = open(f'parsed_from{str(boundaries[0])}to{str(boundaries[1])}.html', 'w')

parsedFile.write('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  ''' + f'<title>ENG :: {str(boundaries[0])}-{str(boundaries[1])}</title>' + 
  '''<style>p{margin:0;}.test{margin:15px 0 15px 0;}.test_mid{text-decoration:underline;}</style>
</head>
<body>
''')

parsedFile.write(f'<h1>English test :: Questions from {str(boundaries[0])} to {str(boundaries[1])} :: testuz.ru</h1>')

for num in range(boundaries[0],boundaries[1] + 1):
  print(f"Getting question No. {str(num)}... ", end = '')
  try:
    url = requests.get(template + str(num))
    html = url.text
    result = pattern.search(html)
    parsedFile.write(f'''{BeautifulSoup(result.group(0), 'html.parser').prettify()}\n''')
    print("Success")
  except:
    parsedFile.write('<p>The question was skipped<br>Reason: Some errors were occured while script was fetching the page</p>')
    print("Failed.. Skipping..")

parsedFile.write('''</body>
</html>''')

parsedFile.close()
print("Well done !\nBye-bye :)")