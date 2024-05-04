with open('input_2.txt', 'r', encoding='utf-8') as f:
    with open('output_2.txt', 'a') as r:
       for line in f:
           if line[0] == 'A' or line[0] == 'a':
              r.write(line)
              print(line, end ='')
    r.close()
f.close()