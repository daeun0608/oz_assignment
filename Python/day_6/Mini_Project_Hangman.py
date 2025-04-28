#문제와 조건은 Mini_Project_Hangman.ipynb



# 기본 라이브러리라 파이썬 설치시 자동으로 설치됩니다!
# random 모듈은 랜덤한 숫자를 생성할 때 사용합니다.
import random
from calendar import error
from multiprocessing.connection import answer_challenge

# 게임에 사용될 단어 목록
words = ["apple", "banana", "orange", "grape", "lemon"]

# 행맨 그림
hangman_pics = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---""",
]



class HangmanGame:
    def __init__(self):
        self.answer=''
        self.count=0
        self.try_ans=''
    def display(self):
        print(hangman_pics[self.count])
    def play(self):
        print('행맨 게임을 시작하겠습니다.')
        self.answer=random.choice(words)
        self.try_ans='_'*len(self.answer)
        while True:
            print("~"*20)
            print("   정답 :",self.try_ans)
            print("~"*20)
            alpha=input('알파벳(소문자)을 입력하세요-->')

            if alpha in self.answer:
                for i in range(len(self.answer)):
                    if(self.answer[i]==alpha):
                        temp=list(self.try_ans)
                        temp[i]=alpha
                        self.try_ans="".join(temp)
                if(self.answer==self.try_ans):
                    print("축하합니다! 단어를 맞추셨습니다. 틀린 시도 횟수 :",self.count)
                    break
                print("단어를 맞추셨군요. 더 힘내봐요.")
            else:
                self.count+=1
                print("틀렸습니다. 남은 시도 횟수 :",7-self.count)
                print(hangman_pics[self.count-1])
                if(self.count==7):
                    print("남은 시도 힛수가 없습니다. 게임을 종료합니다.")
                    break



if __name__ == "__main__":
    game = HangmanGame()
    game.play()