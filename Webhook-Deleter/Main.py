import requests
from dhooks import Webhook

def banner():
    print("""
Fuck Off Loggers
        Input Webhook URL
    """)

def deleter():
    start = input(">")
    hook = Webhook(start)
    hook.send("Stop logging shit whore")
    x = requests.delete(start)

banner()
deleter()

# Simple shit can be used for anything besides robloxloggers