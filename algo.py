import random

def generate_sessions(num_sessions, seq):
    n = len(seq)

    #matrix for keeping track of pair occurences
    used_pairs = [[0] * n for _ in range(n)]


    for i in range(num_sessions):
        available = [i for i in range(len(seq))]
        random.shuffle(available)

        pairs = []

        while len(available) >= 2:
            # Pick entity with fewest unused partners
            a = min(
                available,
                key=lambda x: sum(
                    used_pairs[x][y] == 0
                    for y in available if x != y
                )
            )
            available.remove(a)

            #pick entity with lowest paired occurence
            b = min(available, key=lambda x: used_pairs[a][x])

            available.remove(b)

            used_pairs[a][b] += 1
            used_pairs[b][a] += 1
            pairs.append((seq[a], seq[b]))

        groups = [(pairs[i], pairs[i + 1]) for i in range(0, len(pairs) - 1, 2)]
        print(groups)


if __name__ == '__main__':
    # num_people = int(input())
    # num_sessions = int(input())
    # generate_groups(num_people, num_sessions)

    seq = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    num_sessions = 7

    generate_sessions(num_sessions, seq)
