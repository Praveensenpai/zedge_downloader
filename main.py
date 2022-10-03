import re
import requests


def downloader(link: str):
    print("Downloading...")
    r = requests.get(link)
    d = r.headers['content-disposition']
    file_name = re.findall("filename=(.+)", d)[0]
    with open(file=file_name, mode="wb") as f:
        f.write(r.content)


def dl_link_grabber(web_link: str):
    r = requests.get(web_link, timeout=30)
    link = re.search('"contentUrl":".*?"', r.text).group(0).replace('"contentUrl":', '').replace('"', '')
    return link


if __name__ == "__main__":
    webpage_link = input("Enter the download page link: ")
    try:
        dl_link = dl_link_grabber(webpage_link)
        downloader(dl_link)
    except Exception as e:
        print(e)
