from json import loads as parse
from json import dumps
import urllib3
from time import sleep

def get_activity(user, page=1, auth = None):
    url_str = f"https://api.github.com/users/{user}/events?page={page}"

    reply = __load__(url_str)
    try:
        contents = parse(reply)
    except:
        print("Value Error")
        print(reply)

    return contents


def get_activity_data(input, type="user"):

    act_list = [["ID","Type","Date", "Commits"]]

    if type == "user":

        activity = []
        page = 1

        while True:
            act_page = get_activity(input, page=page)
            if len(act_page) > 0:
                activity += act_page
                page += 1
                sleep(0.01) # wait 10ms
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

    with open("token.txt", "r") as file:
        token = parse(file.read())["token"]

    print(token)

    headers = {
        "Authorization": f"token {token}",
        "user-agent": "Python Urllib3/2.5"
    }

    http = urllib3.PoolManager()
    rq = http.request('GET', url, headers=headers)
    return rq.data
