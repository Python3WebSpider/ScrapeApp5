import hashlib
import time
import base64
import requests

INDEX_URL = 'https://app5.scrape.center/api/movie?limit={limit}&offset={offset}&token={token}'
MAX_PAGE = 10
LIMIT = 10


def get_token(args):
    timestamp = str(int(time.time()))
    args.append(timestamp)
    sign = hashlib.sha1(','.join(args).encode('utf-8')).hexdigest()
    return base64.b64encode(','.join([sign, timestamp]).encode('utf-8')).decode('utf-8')


for i in range(MAX_PAGE):
    offset = i * LIMIT
    token = get_token(args=['/api/movie'])
    index_url = INDEX_URL.format(limit=LIMIT, offset=offset, token=token)
    response = requests.get(index_url)
    print('response', response.json())
