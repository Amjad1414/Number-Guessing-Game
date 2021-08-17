import random
import operator
def random_cal():
    """
    """
    ops={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv,'**':operator.pow}
    num1=random.randint(0,10)
    selector=random.randint(1,10)#I omit 0 from the range to not produce error with division
    op=random.choice(list(ops.keys()))
    num2=int(ops.get(op)(num1,selector))
    num3=int(ops.get(op)(num2,selector))
    result=int(ops.get(op)(num3,selector))
    print('What is the number after {},{},{},...?\n'.format(num1,num2,num3))
    return result

def ask_question(answer,guess):
    if guess < answer:
        guess='your guess less than answer'
        answer=False
    elif guess >answer:
        guess='your guess bigger than answer'
        answer=False
    else:
        answer= guess==answer
        guess=""
    return answer,guess

def main():
    while True:
        while True:
            try:
                print('Welcome to the guessing game \n')
                score=0
                answer=random_cal()
                for _ in range(3):
                    guess=int(input())
                    answer2,guess2=ask_question(answer,guess)
                    if answer2:
                        print("Correct!")
                        score+=1
                        break
                    else:
                        print('Incorrect! Hint:{}'.format(guess2))
                if guess != answer:
                    print('The correct answer was: {}'.format(answer))
                    score-=1
                break
            except ValueError:
                print("This is not a number. Please enter a valid number")
                break
        restart=input("Would you like to try again? Type 'yes' or 'no'\n").lower()
        while restart not in ['yes','no']:
            print("Please make sure you enter 'yes' or 'no' ")
            restart=input("Would you like to try again? Type 'yes' or 'no'\n").lower()
        if restart!='yes':
            print("Your score was: {}".format(score))
            break

if __name__ == "__main__":
    main()
