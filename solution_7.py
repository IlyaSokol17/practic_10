with open('input_7.txt','r', encoding='utf-8') as f:
    with open('output_7.txt', 'w') as r:
        for line in f:
            if int(line) != 100:
                r.write(line)

with open('output_7.txt', 'r') as r:
    with open('input_7.txt','w', encoding='utf-8') as f:
        for line in r:
            f.write(line)
