genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 해당 장르의 총 플레이 수를 저장
    my_dict = {}
    # 장르에 해당하는 곡들의 index와 play를 리스트로 저장
    my_index_play_dict = {}
    for i in range(len(genre_array)):
        genre = genre_array[i]
        play = play_array[i]
        if genre in my_dict:
            my_dict[genre] += play
            my_index_play_dict[genre] += [[i, play]]
        else:
            my_dict[genre] = play
            my_index_play_dict[genre] = [[i, play]]
    # my_dict를 내림 차순으로 sort
    sorted_my_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

    res = []
    # 높은 play수로 정렬된 장르부터 곡 추가
    for genre, total_play in sorted_my_dict:
        # 해당 장르의 곡들을 리스트로 받아옴
        my_index_play_list = my_index_play_dict[genre]
        # play수가 높은 곡들순으로 정렬
        sorted_my_index_play_list = sorted(my_index_play_list, key=lambda item: item[1], reverse=True)
        # 상위 2개의 곡들의 index를 res에 추가
        for i in range(len(sorted_my_index_play_list)):
            if i > 1:
                break
            res.append(sorted_my_index_play_list[i][0])
    return res


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
