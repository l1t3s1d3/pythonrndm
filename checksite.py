import requests
from bs4 import BeautifulSoup
import time
import smtplib

# downloads the homepage of ICS-Cert, and if it finds the active registration link, emails me.
# If it does not find the link, it waits 10 minutes and downloads the homepage again.

# while this is true (it is true by default),
while True:
    # set the url as ics-cert,
    url = ""
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")

    # if the number of times the word occurs on the page is less than 1,
    if str(soup).find("August") == -1:
        # wait 60 seconds,
        time.sleep(600)
        # continue with the script,
        continue

    else:
        # create an email message with just a subject line,
        msg = ''
        # set the 'from' address,
        fromaddr = ''
        # set the 'to' addresses,
        toaddrs  = ['','']

        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my account login name and password,
        server.login("", "")
        #server.
        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()

        break