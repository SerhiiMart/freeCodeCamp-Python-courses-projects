import re
def arithmetic_arranger(problems, answer = False):
    first = ""
    second = ""
    lines = ""
    summ = ""
    result = ""
    nL = "\n"

    if (len(problems) > 5):
      return "Error: Too many problems."
    for problem in problems:
      if (re.search("[^\s0-9.+-]", problem)): 
        if (re.search("[/]", problem) or re.search("[*]", problem)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."
        
      first_number = problem.split(" ")[0]
      operator = problem.split(" ")[1]
      second_number = problem.split(" ")[2]

      if (len(first_number) >= 5 or len(second_number) >= 5):
        return "Error: Numbers cannot be more than four digits."
      sum = ""
      if (operator == "+"):
        sum = str(int(first_number) + int(second_number))
      elif (operator == "-"):
        sum = str(int(first_number) - int(second_number))

      maxLen = max(len(first_number), len(second_number)) + 2  
      top = str(first_number).rjust(maxLen)  
      mid = operator + str(second_number).rjust(maxLen - 1)
      line = ""
      bot = str(sum).rjust(maxLen)

      for i in range(maxLen):
        line += "-"

      if problem != problems[-1]:
        first += top + "    "
        second += mid + "    "
        lines += line + "    "
        summ += bot + "    "
      else:
        first += top
        second += mid
        lines += line
        summ += bot

    if answer:
      result = first + nL + second + nL + lines + nL + summ
    else:
      result = first + nL + second + nL + lines
    return result