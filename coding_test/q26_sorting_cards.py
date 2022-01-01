""" 카드 정렬하기 Page 363
"""

def solution(cards):
    
    result = 0
    
    while len(cards)>1:
        first = min(cards)
        cards.remove(first)
        second = min(cards)
        cards.remove(second)
        print('cards:',cards)
        
        total = first + second
        print('total:',total)
        result += total
        
        
        cards.append(total)
        
    
    return result
    
        
    

def main():
    cards = []
    n = int(input())
    for _ in range(n):
        cards.append(int(input()))
    
    print(solution(cards))
    
if __name__ == '__main__':
    main()