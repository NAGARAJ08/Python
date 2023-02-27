from Question import question
from Call_Class import india_quiz

options = [

    "When did india get Independence:\n a)1947\n b)1944\n c)1949\n d)1957\n",
    "When Is India's Republic day:\n a)1947\n b)1944\n c)1949\n d)1950\n"
]

Qus = [
    india_quiz(options[0], 'a'),
    india_quiz(options[1], 'd')
]


def run_Test(Q):
    score = 0
    for i in Q:
        answer = input(i.prompt)
        if answer == i.answer:
            score += 1
    print("score is " + str(score))


run_Test(Qus)
