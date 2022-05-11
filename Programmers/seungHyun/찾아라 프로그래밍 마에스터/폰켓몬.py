def solution(nums):
    answer = 0
    new_list = set(nums)
    if len(nums)/2 > len(new_list):
        answer = len(new_list)
    else:
        answer = len(nums)/2
    return answer

[풀이 키워드]
=> 중복제거
