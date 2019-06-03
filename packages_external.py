# external packegaes need to be installed
# you can find packages in https://pypi.org/
# lets look at the package of requests

# install using pip or your interpreter

import requests

# package for making http requests

sparta_home_page = requests.get('https://www.spartaglobal.com/')
print(sparta_home_page)
print(sparta_home_page.status_code)
print(sparta_home_page.content)