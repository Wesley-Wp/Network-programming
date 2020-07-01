from gevent import monkey
import urllib.request
import gevent

monkey.patch_all()


def download_img(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img = req.read()
    with open(img_name, "wb") as f:
        f.write(img)


def main():
    gevent.joinall([
        gevent.spawn(download_img, "1.jpg", " https://rpic.douyucdn.cn/live-cover/appCovers/2020/03/12/8114978_20200312164158_small.jpg"),
        gevent.spawn(download_img, "2.jpg", "https://rpic.douyucdn.cn/live-cover/roomCover/2020/02/21/94966971b091f42568448a4fd2fb28da_big.jpg")
    ])


if __name__ == '__main__':
    main()
