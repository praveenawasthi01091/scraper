from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

myurl = "https://twitter.com/melindagates?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"  # url as u wish
uclient = ureq(myurl)  # online connection and load page
page_html = uclient.read()  # store data in this page
uclient.close()
page_soup = soup(page_html, "html.parser")
prat = page_soup.findAll("div", {"class": "content"})

for prac in prat:
    tweets = prac.p.text
    print("------->" + tweets)  # print tweet
    tweet_details = prac.div.text.strip()
    print(tweet_details)  # print tweet details
    reply = prac.findAll("span", {"class": "ProfileTweet-actionCount"})
    reply2 = reply[0].text
    print(reply2)  # print no of reply on tweet
    retweet = reply[1].text
    print(retweet)  # print no of reweets
    likes = reply[2].text
    print(likes)  # print no of likes
    