def solution(genres, plays):
    answer = []
    genre_hash = dict()
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in genre_hash:
            genre_hash[genre].append([play, i])
        else:
            genre_hash[genre] = [[play, i]]
    
    genre_sort = sorted(genre_hash.values(), key = lambda genre : sum(map(lambda info: info[0], genre)), reverse = True)
    
    for songs in genre_sort:
        songs.sort(key = lambda x : (-x[0], x[1]))
        for _, index in songs[:2]:
            answer.append(index)
    
    return answer