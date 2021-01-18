def solution(N, stages):
    save = {}
    total_members = len(stages)

    for stage in range(1, N + 1):
        cnt = stages.count(stage)

        if total_members == 0:
            save[0] = save.get(0, []) + [stage]

        else:
            fail_rate = cnt / total_members
            save[fail_rate] = save.get(fail_rate, []) + [stage]

        total_members -= cnt
    
    result = []

    for key in sorted(save, reverse=True):
        for value in sorted(save[key]):
            result.append(value)
    
    return result


if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    print(solution(4, [4, 4, 4, 4, 4]))