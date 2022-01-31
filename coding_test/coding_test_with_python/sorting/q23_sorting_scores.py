
"""
[Input]
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90

[output]
Donghyuk, 80,60,100
Sangkeun, 80,60,50
Sunyoung, 80,70,100
nsj, 80,80,80
Wonseob, 70,70,90
Sanghyun, 70,70,80
Sei, 70,70,70
Kangsoo, 60,80,100
Haebin, 50,60,100
Junkyu, 50,60,100
Soong, 50,60,90
Taewhan, 50,60,90
"""

class Score:
    
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
    
    def __gt__(self, other):
        if self.score1 == other.score1: 
            if self.score2 == other.score2:
                if self.score3 == other.score3: 
                    return self.name > other.name
                else:
                    return self.score3<other.score3
            else:
                return self.score2 > other.score2
        else:
            return self.score1 < other.score1
        
    def __repr__(self):
        return '{}'.format(self.name)
    

def main():
    n = int(input())
    students = []  
    
    for _ in range(n):
        name, *scores = input().split()
        scores = [int(score) for score in scores]
        student = Score(name, *scores)
        students.append(student)
        
    print("==result==")
        
    for student in sorted(students):
        print(student)
           

if __name__ == '__main__':
    main()