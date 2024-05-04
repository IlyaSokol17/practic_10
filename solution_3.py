s = ''
with open('input_3.txt', 'r', encoding='utf-8') as f:
    with open('output_3.txt', 'a') as r:
        for line in f:
            s += line[0]
        print(s)
        r.write(s)
    r.close()
f.close()