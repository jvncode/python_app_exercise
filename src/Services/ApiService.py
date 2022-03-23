from sys import stderr
import requests
import json
from datetime import datetime
import pathlib


class ApiService:
    def __init__(self):
        pass

    def run(self):
        print('Running ApiService', file=stderr)
        path = '{}/{}/'.format(pathlib.Path(__file__).parent.parent.parent, 'storage')
        try:
            r = requests.get('https://jsonplaceholder.typicode.com/todos/')
            data = json.loads(r.text)
            now = datetime.now()
            for td in data:
                filename = '{}_{}_{}_{}.csv'.format(
                    now.year, now.strftime('%m'), now.strftime('%d'), td['id'])
                with open(path + filename, 'w') as f:
                    f.write(json.dumps(td))
                    f.close()
        except Exception as err:
            print(err)
