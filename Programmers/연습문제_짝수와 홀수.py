# date: 2022/09/26
# author: psS2mj
# brief: 프로그래머스_코딩테스트 연습_연습문제_짝수와 홀수

def solution(num):
    answer = ''
    if num%2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer