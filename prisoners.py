import random

def simulate_prisoners_problem(num_prisoners):
    # 죄수들을 초기화합니다.
    prisoners = list(range(num_prisoners))
    random.shuffle(prisoners)

    # 자신의 번호를 찾은 죄수의 수를 초기화합니다.
    count = 0

    # 각 죄수마다 반복합니다.
    for i in range(num_prisoners):
        # 현재 죄수와 그가 있는 셀을 초기화합니다.
        current_prisoner = i
        current_cell = prisoners[current_prisoner]

        # 현재 죄수가 자신의 번호를 찾을 때까지 반복합니다.
        while current_cell != i:
            # 다음 셀로 이동합니다.
            current_prisoner = current_cell
            current_cell = prisoners[current_prisoner]

        # 자신의 번호를 찾은 죄수의 수를 증가시킵니다.
        count += 1

    # 자신의 번호를 찾은 죄수의 확률을 반환합니다.
    return count / num_prisoners

num_prisoners = 100
num_trials = 1000
success_count = 0
for i in range(num_trials):
    if simulate_prisoners_problem(num_prisoners) == 1:
        success_count += 1
