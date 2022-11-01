import base64
import json
import os
import random
import string

from PIL import Image, ImageDraw
import requests
import ssl


def getimg(filename):
    url = "【验证码获取网址已删除】"
    r = requests.get(url, verify=False)
    # print(r.text)
    res = json.loads(r.text)
    print(res)
    # print(res['content'])
    f = open(filename, 'wb')
    # 获取动漫头像
    anime = res['content'].split(',')[1]
    # print(anime)
    # 对返回的头像进行解码
    anime = base64.b64decode(anime)

    # 将头像写入文件当中
    f.write(anime)
    f.close()


def get_block_score(img):
    sum = 0
    black = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i, j)) == 0:
                black += 1
            sum += 1

    return black, sum


#  计算特征值
def get_features_vaule_by_img(img):
    wide = img.size[0]
    one_wide = int(wide / 2)
    high = img.size[1]
    one_high = int(high / 3)
    score_lsit = []
    for i in range(3):
        for j in range(2):
            img_one = img.crop((j * one_wide, i * one_high, (j + 1) * one_wide, (i + 1) * one_high))
            black, sum = get_block_score(img_one)
            score_lsit.append(black * 1.0 / sum)
    return score_lsit


def ez_map(thresold):
    res = []
    for i in range(256):
        if i < thresold:
            res.append(0)
        else:
            res.append(1)
    return res


def pre_hd_ez(img):
    img = img.convert("L")
    # 二值
    thresold = 140
    table = ez_map(thresold)
    # img=img.convert("1")

    img = img.point(table, '1')
    return img


def pre_split_img(img):
    imgs = []
    num1 = (20, 6, 31, 21)

    fuhao = (36, 6, 50, 21)
    num2 = (51, 6, 62, 21)
    img_num1 = img.crop(num1)
    img_fuhao = img.crop(fuhao)
    img_num2 = img.crop(num2)
    imgs.append(img_num1)
    imgs.append(img_fuhao)
    imgs.append(img_num2)
    return imgs


filename = ""


def Base64ToImage(_base64):
    str = random.sample(string.ascii_letters + string.digits, 16)
    global filename
    filename = ''.join(str) + '.jpg'
    f = open(filename, 'wb')
    # 获取动漫头像
    anime = _base64.split(',')[1]
    # 对返回的头像进行解码
    anime = base64.b64decode(anime)
    # 将头像写入文件当中
    f.write(anime)
    f.close()
    img = Image.open(filename)

    return img


fuhao = [[0.08571428571428572, 0.08571428571428572, 0.42857142857142855, 0.42857142857142855, 0.11428571428571428,
          0.11428571428571428], [0.2857142857142857, 0.0, 0.2857142857142857, 0.0, 0.0, 0.0]]
nums1 = [
    [0.36, 0.44, 0.4, 0.4, 0.36, 0.44],
    [0.24, 0.32, 0.0, 0.4, 0.24, 0.56],
    [0.32, 0.4, 0.04, 0.4, 0.48, 0.32],
    [0.32, 0.48, 0.16, 0.64, 0.32, 0.48],
    [0.04, 0.48, 0.36, 0.52, 0.16, 0.44],
    [0.4, 0.24, 0.28, 0.48, 0.32, 0.4],
    [0.36, 0.32, 0.56, 0.48, 0.36, 0.48],
    [0.32, 0.48, 0.04, 0.44, 0.24, 0.12],
    [0.4, 0.48, 0.56, 0.64, 0.4, 0.48],
    [0.4, 0.44, 0.4, 0.64, 0.24, 0.44]
]
nums2 = [
    [0.44, 0.36, 0.4, 0.4, 0.44, 0.36],
    [0.4, 0.16, 0.2, 0.2, 0.4, 0.4],
    [0.4, 0.32, 0.12, 0.32, 0.56, 0.24],
    [0.4, 0.4, 0.24, 0.56, 0.4, 0.4],
    [0.12, 0.4, 0.4, 0.52, 0.2, 0.44],
    [0.48, 0.16, 0.36, 0.4, 0.4, 0.32],
    [0.44, 0.24, 0.64, 0.4, 0.44, 0.4],
    [0.4, 0.4, 0.2, 0.28, 0.36, 0.0],
    [0.48, 0.4, 0.64, 0.56, 0.48, 0.4],
    [0.48, 0.36, 0.48, 0.56, 0.32, 0.36]
]


def Recognition(_base64):
    img = Base64ToImage(_base64)
    img = pre_hd_ez(img)  # 二值化
    imgs = pre_split_img(img)  # 分隔
    global filename

    os.remove(filename)
    code_num1 = get_features_vaule_by_img(imgs[0])  # 计算特征值
    code_fuhao = get_features_vaule_by_img(imgs[1])  # 计算特征值
    code_num2 = get_features_vaule_by_img(imgs[2])  # 计算特征值
    # print('code1：'+str( code_num1), 'code2：'+str(code_num2))
    a = 0
    b = 0
    for index in range(0, 10):
        if (code_num1 == nums1[index]):
            # print(index)
            a = index
            break
    for index in range(0, 10):
        if (code_num2 == nums2[index]):
            # print(index)
            b = index
            break
    if code_fuhao == fuhao[0]:
        print(str(a) + '+' + str(b) + '=' + str(a + b))
        return a + b
    elif code_fuhao == fuhao[1]:
        print(str(a) + '*' + str(b) + '=' + str(a * b))
        return a * b
    else:
        print('符号识别Error')


Recognition(
    "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAZCAIAAABIPBwcAAACYUlEQVR42uWYPUp2QQyFsxgbO7Hy\nawUXIIKNq7CwcD8uQlyJG3APll64EEJ+Tk5mhK8QUtx33vl95kwmE/n6/P6z9v72cRj/r/yXebia\nZOHC6Ok08L+umjVZWB5TmZxHWjPOcplX1QnfeQ7rd3lV/8YFgM3HS2KGiDp1g46WXMLa1A55BLC4\nsATacgblCqzYshXqJqwKHICFewPiJXXdUhM8AHMKdo5J1Um1baAao0dy80pY7RnGu3R8XNzdO5u6\nLbDnh70+3KilrTDidNlPV9dqM1ikN03XHEkpr/YIH3b77+Uw4E0sqZTXSCZnoSWlxvCS5UtaYbkx\nlBdzXVawHClbQt7CGJYdxeoLuzABXnYay2j5DqyoqVHYxfgg11uEVeGW9saZBn7Oc23C4m/6x+dL\nbNXkV2AtiEvrVz6+vSJTWOe3wiId1hSW9fT4zkFBaXv97cA66WA7a0bX3vLC8S1JCoQmwoe/ZOiI\neS3ASv09HwlXy9FLEMQDJay0DY5Rq64BLNdE6UQ3YUlp87Tw/Dk9hk5WrSD6Y0jySsXFbL6V0hSW\nm0MLy4lrBRbAgR9uKiKHtY1LSVjxQtRjWMXu+B3C57+q5Uvlp/ALMYagzpj0SzyGqbicVUmY0SvP\n+iwAyw0kC5kNVyElReYqLaw0ho6kgOtkTpN+jGCh23CUeBw9jJnXP/ahbVoCvLGZVM8YFgMFzxVL\nmszkgYQns0LXkHyoAM1K+47h95nJprc1gevFfCshu8L2oQIOhOwk7UjV4JwyIy5wTquf2N8zb4D4\nIaN88SgEm/JagDVKP/C8qqF/AD8/f75l3isgAAAAAElFTkSuQmCC")

Recognition(
    "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAZCAIAAABIPBwcAAADiUlEQVRYhbVZP4sTURCfhHyJ/QCWS8o0goWEk+3sRVBiJwTl5EjASjAcBuXA7oKBw94uRA4L4RrLkOv8APsVrrSYZG4yM292djcOx93bt/PvzfvNvHl7ndu7DcSoXG0BICtyZ0bwp15FxOtqc0zErfjUNQ2QjaBDJCJka+mJGGomeJRIAQUrEiA0ydmyIhd+aB5NZMtnpj1oE3Htoe+Yz9AlpYKbxtpdMUPeCLZI4ILEnWkmrgVNVb5+Iw2drRAFK+hBSzpWEmmq660Mlk4QARDTdT3JQ5lCXHxvMZsaQ7WZoPbQQJYQMMfc+6OTzvr/odkswb65DrUOKTEHWcTw7ulLrvTtqzdc0MSdmMmK3PE7K/Kr/gmOh7M5qEIZ2Tau7cnDBc2vb0Z6ReZjF/Z440jRgEpVcQAQkQKAz5dfxLJNyop8MT5bjM80ZxxN8RQj/TxS+ChmUgeaTEPusdNt6slPP77hj2BrefDj4Kp/8nzzk082UMtFltPBcjpY34yW04FpUZsoV9uKmqXzkSQRjAgiHiMcc3DVXZgIx/Xk1GRrvA2Ud44Gs3r0YF8vdCCJmw9qNeiV3anvHBHBijgJtlg9ytX2++yr78yzyWtReVMnbyonQn2WefbXIq3BaUF4z3E9OR3O5sc6EPW58eLjHwAQyZiinvPO2W0BsTjPhweF5tzV+PHucXRxjrI8ATUMhfLH/Uf6FNL+UxrRmYiREotFNmGl61++zMYyVcJSSkyng4SNgtbgX60i5jBSvG8Q2vS1t6e3qFafJgQrETe6OOd+INDe/11pBxBW9+Ca7P7iDAWREPFr8xsAAH8TsUesWVTj+BoFJlKxrjgN9RoiSjV/UH/LC3NdK/qVD47O7d2Go5ei4PSyYoxdAnbtsG8a6JE0c59oBpFFRco3jU38cDY3230/QJDIEqfZ1g7YBT51HdElPytyuAQ4bKy4CCmMtLtwWCWpdmg46JgGSfTx64D4wXWnmT3yXoCIZlJgNs2lTt6WrVxKxMGRwyaRZbadIom0Xn5zTi3AFMTS7keKtFFrKhJWi1Ruf1bkEUwJuv9S6qcGX4/pkNnRpF6lOB1VkU8XkChMvjnfLn/0TsPs8KMVj5EoQHq1jRsr093S+pBd10SDK2p5+E+AUOsgMNIgELX6NUhkNM9K7knkLkEagndb3QOX5leHyFEVpDYQa+xGZQSdeKXCivQP3QMxNurI+5oAAAAASUVORK5CYII="
)
import os, base64

img_str = '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'
img_data = base64.b64decode(
    img_str)  # 注意：如果是"data:image/jpg:base64,"，那你保存的就要以png格式，如果是"data:image/png:base64,"那你保存的时候就以jpg格式。
with open('001.png', 'wb') as f:
    f.write(img_data)
