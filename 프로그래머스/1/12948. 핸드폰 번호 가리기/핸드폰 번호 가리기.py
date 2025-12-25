def solution(phone_number):
    len_phone_number = len(phone_number)
    return "*" * (len_phone_number - 4) + phone_number[-4:]