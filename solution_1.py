s = ''
with open('input_1.txt', 'r', encoding ='utf-8') as f:
    for row in f:
        for letter in row:
          s += letter
f.close()
print(s)
n = str(s.upper())
with open('output1.txt', 'w',) as r:
   r.write(str(n))
r.close()

