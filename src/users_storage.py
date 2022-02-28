from datetime import datetime

# UserName : Count of messages
storage = {}


def update(username: str):
    if storage.get(username) is None:
        storage[username] = 1
    else:
        storage[username] += 1

    print(f"@{username} has been requested - {storage[username]} - {datetime.now()}", flush=True)
