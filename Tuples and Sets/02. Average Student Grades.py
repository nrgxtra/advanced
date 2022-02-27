def solve(n):
    notebook = {}
    for _ in range(n):
        student, grade = input().split(' ')
        if student not in notebook:
            notebook[student] = []
        notebook[student] += [float(grade)]
    for st, gr in notebook.items():
        print(f"{st} ->", end=' ')
        [print(f"{x:.2f}", end=' ') for x in gr]
        print(f"(avg: {(sum(gr)/len(gr)):.2f})")


solve(int(input()))
