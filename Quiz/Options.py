from Question import question

Question_list = [
    "What color are apples?\n(a) Red/Green\n(b)Orange",
    "What color are bananas?\n(a) Red/Green\n(b)Yellow",
    "What color are Oranges?\n(a) Red/Green\n(b)Orange"
]

Questions = [
    question(Question_list[0], "a"),
    question(Question_list[1], "b"),
    question(Question_list[2], "b"),
]


def run_test(Question):
    score = 0
    for q in Question:
        answer = input(q.prompt)
        if answer == q.answer:
            score += 1
    print("Score " + str(score))


run_test(Questions)