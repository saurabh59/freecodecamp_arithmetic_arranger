def arithmetic_arranger(a, b=None):
  flag_a = 0
  flag_b = 0
  flag_c = 0
  if len(a) > 5:
    return 'Error: Too many problems.'
  for x in a:
    if x.split()[1] == '+' or x.split()[1] == '-':
      pass
    else:
        flag_a = 1
    for y in x.split()[0::2]:
      if not y.isnumeric():
        flag_b = 1
      if len(y) > 4:
        flag_c = 1
  if flag_a:
    return "Error: Operator must be '+' or '-'."
  if flag_b:
    return "Error: Numbers must only contain digits."
  if flag_c:
    return "Error: Numbers cannot be more than four digits."
  line_1 = ''
  line_2 = ''
  line_3 = ''
  line_4 = ''
  count = 0
  for x in a:
    if count == 0:
      length_of_numbers = [len(z) for z in x.split()]
      max_length = max(length_of_numbers) + 2
      line_1 += x.split()[0].rjust(max_length, " ")
      line_2 += x.split()[1] + x.split()[2].rjust(max_length - 1, " ")
      line_3 += '-' * max_length
      if b:
        if x.split()[1] == "+":
          result = int(x.split()[0]) + int(x.split()[2])
          line_4 += str(result).rjust(max_length, " ")
        else:
          result = int(x.split()[0]) - int(x.split()[2])
          line_4 += str(result).rjust(max_length, " ")
      count = 1
    else:
      length_of_numbers = [len(z) for z in x.split()]
      max_length = max(length_of_numbers) + 2
      line_1 += " " * 4 + x.split()[0].rjust(max_length, " ")
      line_2 += " " * 4 + x.split()[1] + x.split()[2].rjust(max_length - 1, " ")
      line_3 += " " * 4 + '-' * max_length
      if b:
        if x.split()[1] == "+":
          result = int(x.split()[0]) + int(x.split()[2])
          line_4 += " " * 4 + str(result).rjust(max_length, " ")
        else:
          result = int(x.split()[0]) - int(x.split()[2])
          line_4 += " " * 4 + str(result).rjust(max_length, " ")
  if b:
    return line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4
  else:
    return line_1 + "\n" + line_2 + "\n" + line_3