try:
    with open('input_6.txt', 'r', encoding='utf-8') as f:
        with open('output_6.txt', 'w', ) as r:
            s = int(f.readline())
            print(s)
            lines = 0
            for line in f:
                lines += 1
            print(lines)
            if s == lines:
                r.write('YES')
            else:
                r.write('NO')
except Exception:
    with open('output_6.txt', 'w', ) as r:
        r.write('ERROR')