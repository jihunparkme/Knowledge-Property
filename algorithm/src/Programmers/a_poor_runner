def solution(participant, completion):
    answer = ''
    participant_dict = dict(zip(participant, [0]*len(participant)))
    participant_dict = {i: 0 for i in participant}
    for n in completion:
        if n in participant_dict:
            if participant_dict[n] == 1:
                answer = n
            else:
                participant_dict[n] = 1

    for name, flag in participant_dict.items():
        if answer != '':
            break
        elif flag == 0:
            answer = name

    return answer

if __name__ == "__main__":
    participant = ['leo', 'kiki', 'leo', 'eden']
    completion = ['kiki', 'eden', 'leo']
    ans = solution(participant, completion)
    print(ans)