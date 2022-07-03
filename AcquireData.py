import requests


# 获取源码
def Acquiredata(path1, path2):
    html = requests.get(path1)
    f = open(path2, "w", encoding="utf-8")
    f.write(html.text)


Acquiredata("https://jupter-oss.oss-cn-hangzhou.aliyuncs.com/file/opensearch/documents/106411/test.json?Expires="
            "1656757094&OSSAccessKeyId=LTAI4GGBCQcb7KD7NwKinA3D&Signature=1vrRX1yTHbpcEhFpEEHPt29yWzE%3D", "test.txt")






