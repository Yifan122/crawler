from lxml import etree
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

response = requests.get('https://dss1.bdstatic.com/lvoZeXSm1A5BphGlnYG/skin/12.jpg?2',
            headers=headers)

with open('./pic.png','wb') as f:
    f.write(response.content)
