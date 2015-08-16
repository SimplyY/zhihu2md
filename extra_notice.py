import zhihu
import save_answer
import my_json

def extra_notice():
    set_noticers()
    get_notice()

# 增加noticer
def set_noticers():
    old_datas = my_json.get_user_datas()
    new_datas = get_new_noticers_datas(old_datas)
    my_json.write_user_data(new_datas)


def get_new_noticers_datas(old_datas):
    datas = old_datas
    urls = [data[0] for data in datas]

    while input("是否添加新的关注，y/n:") == 'y':
        url = input("请输入关注作家的首页网址：")
        if url not in urls:  # 禁止添加重复的urls
            datas.append((url, None))
            print("添加成功")
        else:
            print("添加失败，此用户已关注")

    return datas


def get_noticers_urls():
    user_datas = my_json.get_user_datas()

    if user_datas is not None:
        urls = [user_data[0] for user_data in user_datas]
    else:
        urls = []

    return urls


# 获取最新动态
def get_notice():
    # 加载所有关注者的信息
    user_datas = my_json.get_user_datas()

    for user_data in user_datas:
        the_url = user_data[0]
        latest_answer_title = get_latest_answer(the_url).question.title
        print(latest_answer_title)
        # 如果文件数据中的最新回答的问题title不对
        if user_data[1] != latest_answer_title:
            save_answer.save2md(url=the_url, max_number=10)

            print("new notice about " + zhihu.Author(the_url).name)  # TODO need a notice

            # 更新最近回答发生改变的用户信息
            user_datas.remove(user_data)
            user_datas.insert(0, (the_url, latest_answer_title))
            # 将用户信息写入json文件
            my_json.write_user_data(user_datas)  # 更新最近下载下来的回答



def get_latest_answer(url):
    answers = zhihu.Author(url).answers
    return next(answers)


if __name__ == "__main__":
    extra_notice()
