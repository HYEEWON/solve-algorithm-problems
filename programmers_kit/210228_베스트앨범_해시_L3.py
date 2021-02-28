from collections import defaultdict

def solution(genres, plays):
    answer = []
    genresSum = defaultdict(int)
    genresDict = defaultdict(list)

    for i in range(len(genres)):
        genresSum[genres[i]] += plays[i]
        genresDict[genres[i]].append([plays[i], i])

    for key in genresDict.keys():
        genresDict[key] = sorted(genresDict[key], key = lambda x : (-x[0], x[1]))

    genresSort = sorted(genresSum, key = lambda x: -genresSum[x])
    for genre in genresSort:
        answer.append(genresDict[genre][0][1])
        if len(genresDict[genre]) > 1:
            answer.append(genresDict[genre][1][1])

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))