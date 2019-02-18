# Reuters News
Search company's news on Reuters for Python

## Install
```
pip install ReutersNews
```

## Usage
- Initializing
```
from ReutersNews import ReutersNews
news = ReutersNews()
```
- Search company by ticker
```
news.search('AAPL.OQ')
```
- Set date range
```
news.range('2019-01-01','2019-01-10')
```
- Set news relevancy
```
news.setrelevancy(0.8)
```
- Set limit number of return result
```
news.setlimit(10000)
```
- Get search result
```
news.get()
```
Sample return result(list)
```
[{'title':...,'desc':...,'time':...},{'title':...,'desc':...,'time':...},{'title':...,'desc':...,'time':...}]
```

