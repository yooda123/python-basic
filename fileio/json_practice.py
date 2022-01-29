import json

#########################################
# ・json.load: jsonファイル -> pythonデータ構造
# ・json.dump: pythonデータ構造 -> jsonファイル
# ・json.loads: json文字列 -> pythonデータ構造
# ・json.dumps: pythonデータ構造 -> json文字列
#########################################


with open("fileio/example.json") as f:
    data = json.load(f)

# print(type(data))
print(data['glossary']['GlossDiv'])


new_json = {'key1': 'value1', 'key2': (1, 'value2')}
with open('fileio/new_json.json', 'w') as f:
    json.dump(new_json, f)


with open('fileio/new_json.json', 'r') as f:
    new_json_reload = json.load(f)

print(type(new_json_reload))
print(new_json_reload['key2'])

# python -> 文字列
json_str = json.dumps(new_json)
print(type(json_str))
print(json_str)

# 文字列 -> Python（Dictionary）
python_data = json.loads(json_str)
print(type(python_data))
print(python_data)
