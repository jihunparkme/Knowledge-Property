from collections import defaultdict

def solution(genres, plays):
    play_count_by_senres = defaultdict(int)
    songs_in_genres = defaultdict(list)

    for song_id, genre, play in zip(range(0,len(genres)), genres, plays):
        play_count_by_senres[genre] += play
        songs_in_genres[genre].append((-play, song_id))

    genre_in_order = sorted(play_count_by_senres.keys(), key=lambda g:play_count_by_senres[g],reverse=True)

    answer = []
    for genre in genre_in_order:
        answer.extend([id for play, id in sorted(songs_in_genres[genre])[:2]])

    return answer

if __name__ == '__main__' :
    genres = ['classic', 'pop', 'classic', 'classic', 'pop']
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))