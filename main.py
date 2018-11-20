import urllib.request
import re

test_website='https://tieba.baidu.com/p/1753935195'

def get_html_str(url):
    page=urllib.request.urlopen(url)
    page_str=page.read().decode('utf-8')
    return page_str


def download_jpg(html_str):
    pic_reg=r'src="(.+?\.jpg)" width'
    picture_reg=re.compile(pic_reg)

    imglist = picture_reg.findall(get_html_str(website))
    img_id=0
    for img in imglist:
        urllib.request.urlretrieve(img,"./jpg_download/download_img%d.jpg"%img_id)
        img_id+=1

print("------this is a web spider-------")
website=input("input url to download jpg:")
if website:
    pass
else:
    print("no url input, we will use default website instead")
    website=test_website
print("fetching web page")
page_str=get_html_str(website)
print("downloading jpg")
download_jpg(page_str)
print("successfully download jpg")



# pagefile=open('pagetxt.txt','w')
# pagefile.write(pagecode)
# pagefile.close()