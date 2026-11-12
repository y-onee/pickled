import random

def generate_sessions(num_sessions, seq):
    n = len(seq)

    used_pairs = [[0] * n for _ in range(n)]
    # print(used_pairs)

    for i in range(num_sessions):
        available = [i for i in range(len(seq))]
        random.shuffle(available)
        # print(available)

        pairs = []

        while len(available) >= 2:
            a = available.pop()
            b = min(available, key=lambda x: used_pairs[a][x])

            available.remove(b)

            used_pairs[a][b] += 1
            used_pairs[b][a] += 1
            pairs.append((a, b))

        groups = [(pairs[i], pairs[i + 1]) for i in range(0, len(pairs) - 1, 2)]
        print(groups)


if __name__ == '__main__':
    # num_people = int(input())
    # num_sessions = int(input())
    # generate_groups(num_people, num_sessions)

    seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    num_sessions = 10

    generate_sessions(num_sessions, seq)
