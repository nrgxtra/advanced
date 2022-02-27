with open('text.txt') as text_fh:
    text = text_fh.readlines()
text_lines = []
count = 1
for sentence in text:
    sentence = sentence.replace('\n', '')
    new = sentence.replace(' ', '')
    ch_count = 0
    letter_count = 0
    for item in new:
        if item.isalpha():
            letter_count += 1
        else:
            ch_count += 1
    text_lines.append(f'Line {count}: {sentence} ({letter_count})({ch_count})\n')
    count += 1
with open('output.txt', 'x') as output_fh:
    output_fh.writelines(text_lines)
