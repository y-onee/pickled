import random

def generate_sessions(seq, used_pairs, available):
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

    groups = [[pairs[i], pairs[i + 1]] for i in range(0, len(pairs) - 1, 2)]
    print(groups)


def bye_tracking(seq, num_sessions):
    n = len(seq)
    #matrix for keeping track of pair occurences
    used_pairs = [[0] * n for _ in range(n)]
    bye_seq = {}

    for i in range(num_sessions):
        bye_len = len(seq) % 4
        curr_seq = list(range(n))
        random.shuffle(curr_seq)

        while bye_len:
            entity = min(curr_seq, key=lambda x: bye_seq.get(x, 0))
            curr_seq.remove(entity)
            bye_seq[entity] = bye_seq.get(entity, 0) + 1
            bye_len -= 1

        print("Byes:", [seq[x] for x in range(n) if x not in curr_seq])

        generate_sessions(seq, used_pairs, curr_seq)


if __name__ == '__main__':
    # num_people = int(input())
    # num_sessions = int(input())
    # generate_groups(num_people, num_sessions)

    seq = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    num_sessions = 10

    # generate_sessions(num_sessions, seq)
    bye_tracking(seq, num_sessions)