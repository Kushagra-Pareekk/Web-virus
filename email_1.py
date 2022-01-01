import webbrowser
import time
import random

while True:
    sites = random.choice(['getintopc.com', 'mastercode.online', 'proxyrarbg.org', 'weather.gov', 'hackertyper.net', 'prank.com'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 10)
    time.sleep(seconds)