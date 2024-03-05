import urllib.request
import os.path

def get_file(url):
    req= urllib.request.urlopen(url)
    html=req.read()
    return html

if __name__ == "main":
    url="https://elcomercio.pe/resizer/TGsCCYstVtXfUlqzlUV46HCctbI=/580x330/smart/filters:format(jpeg):quality(90)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/3NQAYPOE4FD4XCLWYKVDI4LIYA.jpg"
    f=open(os.path.basename(url),"wb")
    f.write(get_file(url))
    f.close()
    print("fin del programa")