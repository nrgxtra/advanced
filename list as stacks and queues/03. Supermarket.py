def solve_supermarket():
    from collections import deque
    q = deque()
    while True:
        command = input()
        if command == 'End':
            break
        elif command == 'Paid':
            while q:
                print(q.popleft())
        else:
            q.append(command)

    print(f'{len(q)} people remaining.')

solve_supermarket()
