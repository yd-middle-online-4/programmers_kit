genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def solution(genres, plays):
    answer = []
    play_t = {}
    order_g = {}

    for i, (x, y) in enumerate(zip(genres, plays)):
        if x in play_t:
            play_t[x] += y
        else:
            play_t[x] = y
       
        if x in order_g:
            order_g[x].append((y, i))
        else:
            order_g[x] = [(y, i)]
        
    play_t = sorted(play_t.items(), key = lambda x: x[1], reverse = True)
    

    for i in play_t:
        order_g[i[0]] = sorted(order_g[i[0]], key = lambda x: x[0], reverse = True)[:2]
        for (x,y) in order_g[i[0]]:
            answer.append(y)

    print(answer)
solution(genres, plays)