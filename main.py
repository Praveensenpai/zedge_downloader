import re
import requests


def downloader(file_name: str, link: str):
    print("Downloading...")
    r = requests.get(link)
    if not file_name:
        d = r.headers['content-disposition']
        file_name = re.findall("filename=(.+)", d)[0]
    with open(file=file_name, mode="wb") as f:
        f.write(r.content)


def dl_link_grabber(web_link: str):
    r = requests.get(web_link, timeout=30)
    if "/wallpaper/" in web_link:
        name = re.search('"title":".*?"',r.text).group(0).replace('"title":"', '').replace('"', '') + ".png"
    else:
        name = ""
    link = re.search('"contentUrl":".*?"', r.text).group(0).replace('"contentUrl":', '').replace('"', '')
    return name, link


if __name__ == "__main__":
    webpage_link = input("Enter the download page link: ")
    try:
        f_name, dl_link = dl_link_grabber(webpage_link)
        downloader(f_name, dl_link)
    except Exception as e:
        print(f"Failed. Reason: {e}")
