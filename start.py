# 1. Login
# 2. Collection all urls for each page
# 3. getting all product url
# 4. merging json results and create csv/xls
import requests

url = "https://www.alibaba.com/"
url = "https://seekingalpha.com/article/4406922-wesfarmers-limited-wfaff-ceo-rob-scott-on-half-year-2021-results-earnings-call-transcript"
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux i686; rv:85.0) Gecko/20100101 Firefox/85.0."
}
url = 'https://www.alibaba.com/'

res = requests.get(url)
print('status code {}'.format(res.status_code))
print(res)

with open('result.txt', 'w+') as file:
    file.write(res.text)
    file.close()

print(f'content {res.text}')
