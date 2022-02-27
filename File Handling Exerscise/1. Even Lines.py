with open('text.txt') as text_fh:
    text = text_fh.readlines()
replacements = ["-", ",", ".", "!", "?"]
for i in range(len(text)):
    current = text[i]
    if i % 2 == 0:
        new = ''
        for ch in current:
            if ch in replacements:
                new += '@'
            elif ch == '\n':
                pass
            else:
                new += ch
        for_pr = new.split(' ')
        rev = []
        for h in range(len(for_pr)-1, -1, -1):
            rev.append(for_pr[h])
        print(' '.join(rev))


