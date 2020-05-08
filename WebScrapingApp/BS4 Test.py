import bs4, requests


def getTestQuestion(testURL):
    res = requests.get(testURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elements = soup.select("#test-question-text")
    return elements[0].text.strip()


testQuestion = getTestQuestion("https://ng.cengage.com/static/nb/ui/evo/index.html?deploymentId=58359123250615173832497960537&eISBN=9781337620062&id=686357593&snapshotId=1544795&")
print(testQuestion)


