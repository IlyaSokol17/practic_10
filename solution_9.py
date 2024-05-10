with open('input_9.txt', 'r', encoding='utf_8') as f:
    with open('output_9.txt', 'w' ) as r:
          n = f.readlines()
          print(len(n))
          for i in range(1, len(n), 2):
              r.write(n[i])


