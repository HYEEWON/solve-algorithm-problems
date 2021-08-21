from collections import defaultdict
import re

def solution(word, pages):
    word = word.lower()
    score = [[0 for j in range(2)] for i in range(len(pages))]
    matchingScore = [0 for j in range(len(pages))]
    link = [{} for i in range(len(pages))]
    
    for i in range(len(pages)):
        page = pages[i].lower()
        for f in re.findall(r'[a-zA-Z]+', page):
            if f == word:
                score[i][0] += 1
        myLink = re.search(r'<meta property=\"og:url\" content=\"https://([\S]*)\"/>', page).group(1)
        outLink = list(set(re.findall(r'<a href="https://([\S]+)">', page)))
        score[i][1] = len(outLink)
        link[i][myLink] = outLink

    for i in range(len(pages)):
        scores = 0
        for j in range(len(pages)):
            if i != j and list(link[i].keys())[0] in list(link[j].values())[0]:
                scores += (score[j][0] / score[j][1])
        matchingScore[i] = score[i][0]+scores
    return matchingScore.index(max(matchingScore))

word = 'blind'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution(word, pages))