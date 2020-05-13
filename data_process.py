import json
import random

CONFIG_PATH = 'data/config.json'

def read_json_obj(filepath,encoding="UTF-8"):
    with open(filepath,'r',encoding='UTF-8') as f:
        obj = json.load(f)
    return obj


CONFIG = read_json_obj(CONFIG_PATH)

def write_result(result,path=CONFIG['result']):
    with open(path, 'w') as f:
        f.write(json.dumps(result, indent=2))

DATA_PATH = CONFIG['sourceDataPath']
ITEM_ID = CONFIG['itemId']


data = read_json_obj(DATA_PATH)
DATA = {d[ITEM_ID]: d for d in data} if type(data)==list else data

FIELDS = CONFIG['fields']
LONG_FIELDS = CONFIG['longFields']
SPLIT_FIELDS = CONFIG['splitFields']

if not FIELDS:
    for item in DATA.values():
        FIELDS = list(item.keys())

try:
    results = read_json_obj(CONFIG['result'])
except FileNotFoundError:
    results = {}

result_fields = CONFIG['resultOptions']

left_data = [item for item in DATA if item not in results]

random.shuffle(left_data)


