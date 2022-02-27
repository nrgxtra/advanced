import re
with open('words.txt') as words_fh:
    words = words_fh.read().split()
with open('text.txt') as text_fh:
    text = text_fh.read()
result = []
for el in words:
    matches = re.findall(rf'[\s-]({el})[\s.?!,]', text, re.MULTILINE + re.IGNORECASE)
    word_count = len(matches)
    result.append([el, word_count])

sorted_result = sorted(result, key=lambda x: -x[1])
with open('output.txt', 'w') as output_fh:
    for item in sorted_result:
        print(f'{item[0]}-{item[1]}', file=output_fh)

