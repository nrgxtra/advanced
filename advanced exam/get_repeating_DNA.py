def get_repeating_DNA(txt):
    result = []
    for i in range(len(txt)):
        current = txt[i:i+10]
        rest = txt[i+1:]
        for j in range(len(rest)):
            compare = rest[j:j+10]
            if current == compare and current not in result:
                result.append(current)
                break
    return result



test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)



