def solution(m, n, sx, sy, balls):
    answer = []

    end_li = [[-sx, sy], [m * 2 - sx, sy], [sx, n * 2 - sy], [sx, -sy]]

    for x, y in balls:
        dists = []
        for ex, ey in end_li:
            b_dist = (x - ex) ** 2 + (y - ey) ** 2
            s_dist = (sx - ex) ** 2 + (sy - ey) ** 2

            if not (sx == ex == x or sy == ey == y) or (b_dist > s_dist):
                dists.append(b_dist)

        answer.append(min(dists))

    return answer
