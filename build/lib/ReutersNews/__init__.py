import requests
import json
import datetime
import pandas as pd

class ReutersNews:
        def __init__(self):
                self.limit = 10000
                self.relevancy = 0.8
                self.days = 30
                self.end = datetime.datetime.now()

        def search(self,ticker):
                self.ticker = ticker

        def range(self, start, end):
                daterange = pd.date_range(start, end)
                result = [(item.strftime('%s')) for item in daterange]
                self.days = len(result)
                self.end = result[-1]

        def setlimit(self,limit):
                self.limit = limit

        def setrelevancy(self, relevancy):
                self.relevancy = relevancy
       
        def get(self):
                url = 'https://uk.mobile.reuters.com/assets/jsonCompanyNews?channel=companyNewsEntity&defaultDaysInterval=' + str(self.days) + '&limit=' + str(self.limit) + '&relevancy=' + str(self.relevancy) + '&symbol=' + self.ticker + '&endTime=' + str(self.end)+'000'
                res = requests.get(url)
                data = json.loads(res.text)
                result = []
                for item in data['headlines']:
                        result.append({'title':item['headline'].replace('\n', ' '),'desc':item['blurb'].replace('\n', ' '),'time':item['formattedDate'].replace('\n', ' ')})
                return result


