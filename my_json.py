import json

__author__ = 'yuwei'

noticers_file_name = 'noticer.json'

# 读json文件
def get_user_datas():
    with open(noticers_file_name, mode='r') as f:
        json_user_datas = f.readlines()
        if json_user_datas:
            user_datas = json.loads(json_user_datas[0])
        else:
            user_datas = []
    return user_datas

# 写json文件
def write_user_data(user_datas):
    json_user_datas = json.dumps(user_datas)
    with open(noticers_file_name, mode='w') as f:
        f.write(json_user_datas)
