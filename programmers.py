# def solution(phone_number):
#     answer = print('{0}{1}'.fromat(phone_number[0:4], phone_number[4:6]))
#     return answer

# solution('01087973323')

import re
def solution(phone_number):
    if len(phone_number) == 4 :
        return phone_number
    elif 4 < len(phone_number) <= 20 :
        answer =  re.sub('[0-9]', '*', phone_number, count = len(phone_number) - 4)
        return answer
    else :
        print("잘못 입력하였습니다.")

solution('19374744481')



# def solution(phone_number):
#     return "*"*(len(phone_number)-4) + phone_number[-4:]

# solution('01087973323')


