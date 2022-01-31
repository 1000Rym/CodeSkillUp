""" 가사 검색 Page370
"""
def check_match(word, query):  
    if len(word) != len(query):
        return False
    
    for index in range(len(query)):
        if query[index] == '?':
            continue
        else:
            if word[index] != query[index]:
                return False
    
    return True
    

def solution(words, queries):
    result = []
    for query in queries:
        count = 0
        for word in words:
            count += check_match(word, query)
        result.append(count)
    
    return result
    
def main():
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    
    print(solution(words, queries))

if __name__ == '__main__':
    main()