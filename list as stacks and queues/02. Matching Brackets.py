def get_matching_brackets(expression):

    opening_bracket_indices = []
    sub_expression = []
    for i in range(len(expression)):
        ch = expression[i]
        if ch == '(':
            opening_bracket_indices.append(i)
        elif ch == ')':
            start_idx = opening_bracket_indices.pop()
            end_idx = i
            sub_expression.append(
                expression[start_idx:end_idx+1]
            )
    for element in sub_expression:
        print(element)

expression = input()
get_matching_brackets(expression)

