# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 2개씩 수록


def solution(genres, plays):
    answer = []
    album = {}
    for i, (genre, plays) in enumerate(zip(genres, plays)):
        if genre in album:
            album[genre].append([plays, i])
        else:
            album[genre] = [[plays, i]]

    genre_rank = {}
    for genre in album.keys():
        songs = album[genre]
        plays_sum = 0
        for song in songs:
            plays_sum += song[0]
        genre_rank[genre] = plays_sum
    genre_rank = sorted(genre_rank.items(), key=lambda x: x[1], reverse=True)  # 장르별 재생순 높은 순

    for genre in genre_rank:
        song_rank = sorted(album[genre[0]], key=lambda x: (-x[0], x[1]))  # 재생수 높은 순, 고유번호 낮은 순
        result = 0
        for song in song_rank:
            answer.append(song[1])  # 고유번호
            result += 1
            if result == 2:  # 장르별로 2개씩
                break

    return answer


""" 다른 풀이 1
def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
"""

""" 다른 풀이 2
def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)

    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play
"""


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]
