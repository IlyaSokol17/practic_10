with open('input_4.txt', 'r', encoding='utf-8') as f:
    with open('output_4.txt', 'a') as r:
        for line in f:
             if (len(line)) > 20 :
                 r.write(line)
             print(len(line))
    r.close()
f.close()