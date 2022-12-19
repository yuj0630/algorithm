n = int(inptut())
students = []

for _ in range(n):
    students.append(input().split())

#정렬 기준
# 두 번째 원소를 기준으로 내림차순 정렬
# 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬렬#
#

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])