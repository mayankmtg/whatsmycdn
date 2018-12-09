import requests
import sys
import re



def simulate_get_check_cdn(domain_name):
    URL = "http://www.whatsmycdn.com/?uri="+domain_name+"&location=GL"
    r = requests.get(url = URL)
    html_response = r.text
    is_cdn = False
    for html_line in html_response.split('\n'):
        title_search = re.search('<div class="six columns" style="margin-left: 2px; word-wrap:break-word;">(.*)</div>', html_line, re.IGNORECASE)
        # print(title_search)
        if title_search:
            title = title_search.group(1)
            if(title!='-'):
                is_cdn = True
                break
    if(is_cdn):
        print(domain_name)



with open('alexatop.csv') as f:
    for line in f:
        domain_name = line.split(',')[1]
        simulate_get_check_cdn(domain_name)