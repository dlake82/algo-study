from collections import deque

def solution(plans):
    def get_time(time):
        hour, minute = int(time[0:2]), int(time[3:5])
        return hour * 60 + minute

    answer = []
    plans = sorted(list(map(lambda x: [x[0], get_time(x[1]), int(x[2])], plans)), key=lambda x: x[1])
    wait = deque()
    print(plans)

    for i, v in enumerate(plans[:-1]):
        print("=================", v)
        now, next_time = v[1], plans[i + 1][1] 

        while wait:
            j, t, q = wait.pop()
            now += q
            lest = t + now

            if lest > next_time:
                wait.append([j, next_time, lest - next_time])
                print(answer, wait)
                break
            else:
                answer.append(j)
                print(answer, wait)
            
                
        wait.append(v)
        print(answer, wait)
    
    while wait:
        answer.append(wait.pop()[0])
        
    print(answer, wait)

    return answer

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "15:00", "30"], ["computer", "12:30", "100"]]))