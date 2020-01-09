import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    response = requests.get('https://api.github.com/users/{}/events'.format(username))

    # events = [event for event in response.json() if event['type'] == "PushEvent" or event['type'] == "IssueEvent"]
    events = json.loads(response.content)

    print(events[0]['created_at'])
    