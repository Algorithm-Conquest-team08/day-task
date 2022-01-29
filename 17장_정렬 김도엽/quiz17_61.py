nums = [3, 30, 34, 5, 9]

# def solution(numbers):
#     str_numbers = list(map(str, numbers)) # 문자자료형으로 변환
#     str_numbers.sort(reverse=True) # sort 함수로 큰 숫자대로 분류
#     answer = "".join(str_numbers) # Join함수로 연결
#
#     return  answer
#
# print(solution(nums))

nums = [3, 30, 34, 5, 9]
li = list(map(str, nums))
print(li)

li.sort(reverse = True)
print(li)

for j in range (100):
    for i in range(1, len(li)):
        if (li[i-1] + li[i]) < (li[i] + li[i-1]):
            li[i-1], li[i] = li[i], li[i-1]
print(li)

answer = str(int(''.join(map(str, li))))

print(answer)