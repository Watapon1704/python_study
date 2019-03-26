﻿class PropertyTest(object):
 
    def __init__(self, url):
        self._url = url
 
    @property
    def url(self):
        print('-- get_url --')
        return self._url
 
 
prop = PropertyTest('https://www.python-izm.com/')

print(prop.url)