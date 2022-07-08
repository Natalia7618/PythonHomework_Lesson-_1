# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = 0
y = 1
z = 1
left_str = not (x or y or z)
right_str = not x and not y and not z
statement_result = left_str == right_str
print (statement_result)