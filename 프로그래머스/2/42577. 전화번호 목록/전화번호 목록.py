def solution(phone_book):
    phone_book.sort(key=len)
    my_set = set()
    
    for number in phone_book:
        pre = ""
        for num in number:
            pre += num
            if pre in my_set:
                return False
        my_set.add(pre)
        
    return True
                 
            
'''
1 길이순 정렬하기
2 각각의 숫자에서 처음 숫자부터 한자리씩 기록하기
3 하나씩 자릿수가 늘어날 때, 만약 같은 숫자가 하나라도 존재할 경우
   return false
4 가장 자릿수가 적은 숫자가 기록이 완료됐을 때까지 같은 숫자가 없으면
   return true
'''