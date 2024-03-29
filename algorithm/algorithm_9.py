#https://programers.co.kr/learn/courses/30/lessons/60059
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
        if new_lock[i][j] != 1:
        return False

def solution(key, lock):
    n = len(lock)
    m = len(key)
    #자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0 * (n * 3) for _ in range(n*3)]]
    #새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_metrix_by_90_degree(key)
        for x in range(n+2):
            #자물쇠에 열쇠를 끼워 넣기
            for i in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+1][y+1] += key[i][j]
return False