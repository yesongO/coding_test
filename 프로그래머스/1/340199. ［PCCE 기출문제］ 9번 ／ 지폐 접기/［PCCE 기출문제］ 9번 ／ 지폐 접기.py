def solution(wallet, bill):
    result = 0
    min_bill, max_bill = min(bill), max(bill)
    min_wallet, max_wallet = min(wallet), max(wallet)
    
    while (max_bill > max_wallet) or (min_bill > min_wallet):
        max_bill = max_bill // 2
        result += 1
        if max_bill < min_bill: 
            max_bill, min_bill = min_bill, max_bill
    
    return result