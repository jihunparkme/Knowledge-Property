def solution(answers):
    student = [[1,2,3,4,5],
               [2,1,2,3,2,3,2,5],
               [3,3,1,1,2,2,4,4,5,5]]
    correct_answers = []
    asw = []
    for std in student:
        if len(answers) > len(std):
            std = std*(len(answers)//len(std))
        res = list(map(lambda x, y: x == y, std, answers))
        correct_answers.append(res.count(True))
    student_data = list(zip(range(1,len(student)+1), correct_answers))
    student_data_sort = sorted(student_data, key=lambda a: a[1])
    max = student_data_sort[-1][1]
    while student_data_sort:
        temp = student_data_sort.pop()
        if max == temp[1]:
            asw.append(temp[0])
    return sorted(asw)

if __name__=='__main__':
    answers = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
    answers= [1,3,2,4,2]
    print(solution(answers))



