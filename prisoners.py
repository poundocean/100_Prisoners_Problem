import random

def simulate_prisoners_problem(num_prisoners):
    # 죄수들을 초기화합니다.
    prisoners = list(range(num_prisoners))
    random.shuffle(prisoners)

    # 자신의 번호를 찾은 죄수의 수를 초기화합니다.
    count = 0

