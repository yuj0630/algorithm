#https://programers.co.kr/learn/courses/30/lessons/60061
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1:
            if[x, y, -1, 0] in answer or [x + 1, y - 1] in answer

