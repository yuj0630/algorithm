#프로그래머 사이트에서 해야 함

def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        #단위 (step)크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            #이전 관계와 동일하다면 압축 횟수 증가
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        #만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))

return answer