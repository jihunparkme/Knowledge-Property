def solution(participant, completion):
    participant.sort()
    completion.sort()

    for pn, cn in zip(participant, completion):
        if pn != cn:
            return pn

    return participant[-1]

if __name__ == "__main__":
    participant = ['leo', 'kiki', 'leo', 'eden']
    completion = ['kiki', 'eden', 'leo']
    ans = solution(participant, completion)
    print(ans)