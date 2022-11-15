def sum_1_to_n(n):
  answer = 0
  for i in range(1, n + 1):
    total = answer
    answer = answer + i
    print(f'步驟{i} => total + {i} => {total} + {i} = {answer}')

  return answer


print(sum_1_to_n(10))
