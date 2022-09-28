# Написать функцию palindrome, которая для заданного числа num возвращает список всех числовых палиндромов, 
# содержащихся в каждом номере. Массив должен быть отсортирован в порядке возрастания, 
# а любые дубликаты должны быть удалены. 
# 
# Пример: 
# palindrome(34322122) => [22, 212, 343, 22122] 
 
 
import traceback 
 
 
def palindrome(num): 
  ans = [] 
  num = str(num) 
  for i in range(0, len(num) - 1, 1): 
    for j in range(i + 1, len(num) + 1, 1): 
      cnum = int(num[i:j]) 
      t = cnum 
      rev = 0 
      while (cnum > 0): 
        dig = cnum % 10 
        rev = rev * 10 + dig 
        cnum = cnum // 10 
      if (t == rev) and (t>=10): 
        ans.append(t) 
 
  ans = list(set(ans)) 
  return (sorted(ans)) 


# Тесты 
try: 
  assert palindrome(1551) == [55, 1551] 
  assert palindrome(221122) == [11, 22, 2112, 221122] 
  assert palindrome(10015885) == [88, 1001, 5885] 
  assert palindrome(13598) == [] 
except AssertionError: 
 print("TEST ERROR") 
 traceback.print_exc() 
else: 
 print("TEST PASSED")
