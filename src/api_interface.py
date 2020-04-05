from json import loads as parse
from urllib.parse import quote_plus as url
from urllib.request import urlopen as ureq

def get_activity(user):
    url_str = f"https://api.github.com/users/{user}/events"

    contents = parse(__load__(url_str))

    return contents


def __load__(url):
    client = ureq(url)
    content = client.read()
    client.close()
    return content
