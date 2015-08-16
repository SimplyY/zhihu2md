import zhihu
import html2text
import os

# 将url对应用户的最近answers在一个md里面输出, 默认answers数量最多100
def save2md(url, min_upvote=-1, max_number=1000):
    answers = zhihu.Author(url).answers

    file_name = get_file_name(url, min_upvote)

    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name + '.md')

    write_md(answers, file, min_upvote, max_number)


def get_file_name(url, min_upvote):
    if min_upvote == -1:
        file_name = zhihu.Author(url).name + '最近回答'
    else:
        file_name = zhihu.Author(url).name + min_upvote + '+赞回答锦集'
    return file_name


def write_md(answers, file, min_upvote, max_number):
    with open(file, 'wb') as f:
        h2t = html2text.HTML2Text()
        h2t.body_width = 0
        content = ''
        index = 0
        for answer in answers:
            if index >= max_number:
                break
            if answer.upvote > int(min_upvote):
                index += 1
                content += '# ' + str(index) + '.' + answer.question.title
                content += answer.content

        f.write(h2t.handle(content).encode('utf-8'))
        print("saved")


if __name__ == "__main__":
    save2md(input("请输入作家的首页网址："), input("请输入要生成的回答的最小赞数："))
