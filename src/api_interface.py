from json import loads as parse
from json import dumps
from urllib.util import make_headers
from urllib.parse import quote_plus as url
from urllib.request import urlopen as ureq

def get_activity(user, page=1, auth = None):
    url_str = f"https://api.github.com/users/{user}/events?page={page}"

    if auth:
        headers = make_headers(basic_auth=f'{auth[0]}:{auth[1]}')
    else:
        headers = None

    contents = parse(__load__(url_str))

    return contents


def get_activity_data(input, type="user"):

    act_list = [["ID","Type","Date", "Commits"]]

    if type == "user":

        activity = parse('[{}]')
        page = 1

        while True:
            act_page = get_activity(input)
            if len(act_page) > 0:
                #dumps(act_page, indent=4)
                activity += act_page
                sleep(50)
            else:
                break

    elif type == "activity":
        activity = input

    for event in activity:
        id = event["id"]
        type = event["type"]
        date = event["created_at"]
        try:
            commits = len(event["payload"]["commits"])
        except:
            commits = "-"

        act_list.append([id, type, date, commits])

    return act_list



def __load__(url):
    client = ureq(url)
    content = client.read()
    client.close()
    return content
