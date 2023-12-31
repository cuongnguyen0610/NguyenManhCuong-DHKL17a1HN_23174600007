## hàm random
#1 hàm seek
from random import randrange
a = randrange(1,201)
print(a)
####
import random
a1 = random.randrange(1,300)
print(a1)
#####
import random
the_number = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10"))  # thử đoán 1 giá trị từ 1 đến 10
print(the_number)
count =4
while guess!=the_number: #Trong khi số bạn nhập còn khác với máy thì cứ tiếp tục với vòng lặp while
    if guess>the_number:
        print(guess,"was to high , try again") # số bạn cho quá lớn hãy thử lại
    if guess<the_number:
        print(guess,"was to low , try again") # số bạn cho quá bé hãy thử lại
    guess = int(input("Guess again:")) 
    count-=1
    if count==0:
        print("Good luck to the next time")
        break
print(guess,"Guess the number, you win")            