import requests
import time

url = ['https://blog.csdn.net/qq_37745470/article/details/90413713',
'https://blog.csdn.net/qq_37745470/article/details/90270054',
'https://blog.csdn.net/qq_37745470/article/details/90105930',
'https://blog.csdn.net/qq_37745470/article/details/89817088',
'https://blog.csdn.net/qq_37745470/article/details/89601007',
'https://blog.csdn.net/qq_37745470/article/details/89162749',
'https://blog.csdn.net/qq_37745470/article/details/89158633',
'https://blog.csdn.net/qq_37745470/article/details/89145256',
'https://blog.csdn.net/qq_37745470/article/details/89094227',
'https://blog.csdn.net/qq_37745470/article/details/88804768',
'https://blog.csdn.net/qq_37745470/article/details/88778906',
'https://blog.csdn.net/qq_37745470/article/details/88562301',
'https://blog.csdn.net/qq_37745470/article/details/88542926',
'https://blog.csdn.net/qq_37745470/article/details/88233389',
'https://blog.csdn.net/qq_37745470/article/details/88115117',
'https://blog.csdn.net/qq_37745470/article/details/88089724',
'https://blog.csdn.net/qq_37745470/article/details/88087717',
'https://blog.csdn.net/qq_37745470/article/details/88087577',
'https://blog.csdn.net/qq_37745470/article/details/88086713',
'https://blog.csdn.net/qq_37745470/article/details/88082276',
'https://blog.csdn.net/qq_37745470/article/details/88082104',
'https://blog.csdn.net/qq_37745470/article/details/88080260',
'https://blog.csdn.net/qq_37745470/article/details/88078875',
'https://blog.csdn.net/qq_37745470/article/details/88066804',
'https://blog.csdn.net/qq_37745470/article/details/88057059',
'https://blog.csdn.net/qq_37745470/article/details/88046101',
'https://blog.csdn.net/qq_37745470/article/details/88041996',
'https://blog.csdn.net/qq_37745470/article/details/87090547',
'https://blog.csdn.net/qq_37745470/article/details/86770217',
'https://blog.csdn.net/qq_37745470/article/details/86708443',
'https://blog.csdn.net/qq_37745470/article/details/86584836',
'https://blog.csdn.net/qq_37745470/article/details/86575482',
'https://blog.csdn.net/qq_37745470/article/details/86574493',
'https://blog.csdn.net/qq_37745470/article/details/86229781',
'https://blog.csdn.net/qq_37745470/article/details/86150491',
'https://blog.csdn.net/qq_37745470/article/details/85874243',
'https://blog.csdn.net/qq_37745470/article/details/85838104',
'https://blog.csdn.net/qq_37745470/article/details/85108592',
'https://blog.csdn.net/qq_37745470/article/details/84849632',
'https://blog.csdn.net/qq_37745470/article/details/84849617',
'https://blog.csdn.net/qq_37745470/article/details/84849577',
'https://blog.csdn.net/qq_37745470/article/details/84849546',
'https://blog.csdn.net/qq_37745470/article/details/84849512',
'https://blog.csdn.net/qq_37745470/article/details/84849485',
'https://blog.csdn.net/qq_37745470/article/details/84849236',
'https://blog.csdn.net/qq_37745470/article/details/84499273',
'https://blog.csdn.net/qq_37745470/article/details/84499174',
'https://blog.csdn.net/qq_37745470/article/details/84499110',
'https://blog.csdn.net/qq_37745470/article/details/84343758',
'https://blog.csdn.net/qq_37745470/article/details/84331174',
'https://blog.csdn.net/qq_37745470/article/details/84202344',
'https://blog.csdn.net/qq_37745470/article/details/84202315',
'https://blog.csdn.net/qq_37745470/article/details/84202299',
'https://blog.csdn.net/qq_37745470/article/details/84202267',
'https://blog.csdn.net/qq_37745470/article/details/84202244',
'https://blog.csdn.net/qq_37745470/article/details/84202220',
'https://blog.csdn.net/qq_37745470/article/details/84202179',
'https://blog.csdn.net/qq_37745470/article/details/84202113',
'https://blog.csdn.net/qq_37745470/article/details/84202081',
'https://blog.csdn.net/qq_37745470/article/details/83859379',
'https://blog.csdn.net/qq_37745470/article/details/83757100',
'https://blog.csdn.net/qq_37745470/article/details/83717223',
'https://blog.csdn.net/qq_37745470/article/details/83690761',
'https://blog.csdn.net/qq_37745470/article/details/83658508',
'https://blog.csdn.net/qq_37745470/article/details/83653551',
'https://blog.csdn.net/qq_37745470/article/details/83651596',
'https://blog.csdn.net/qq_37745470/article/details/83650390',
'https://blog.csdn.net/qq_37745470/article/details/83591734',
'https://blog.csdn.net/qq_37745470/article/details/83549595',
'https://blog.csdn.net/qq_37745470/article/details/83042124',
'https://blog.csdn.net/qq_37745470/article/details/83041327',
'https://blog.csdn.net/qq_37745470/article/details/83019321',
'https://blog.csdn.net/qq_37745470/article/details/83019187',
'https://blog.csdn.net/qq_37745470/article/details/83019097',
'https://blog.csdn.net/qq_37745470/article/details/83018996',
'https://blog.csdn.net/qq_37745470/article/details/83018678',
'https://blog.csdn.net/qq_37745470/article/details/82557582',
'https://blog.csdn.net/qq_37745470/article/details/81904361',
'https://blog.csdn.net/qq_37745470/article/details/81903943',
'https://blog.csdn.net/qq_37745470/article/details/81903869',
'https://blog.csdn.net/qq_37745470/article/details/81603936',
'https://blog.csdn.net/qq_37745470/article/details/81584901',
'https://blog.csdn.net/qq_37745470/article/details/81584421',
'https://blog.csdn.net/qq_37745470/article/details/81454424',
'https://blog.csdn.net/qq_37745470/article/details/81388488',
'https://blog.csdn.net/qq_37745470/article/details/81260062']

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
countUrl = len(url)
def access_csdn_url():
    count =0
    try:  # 正常运行
        for i in range(countUrl):
            response = requests.get(url[i], headers=headers)
            if response.status_code == 200:
                count = count + 1
                print('Success ' + str(count), 'times')
                time.sleep(10)
    except Exception:  # 异常
        print('Failed and Retry')
        time.sleep(10)

if __name__ == '__main__':
    while(1):
        access_csdn_url()


