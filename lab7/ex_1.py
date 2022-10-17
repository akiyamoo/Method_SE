with open('ex_1_product.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        lines = line.split(' ')
        if len(lines) == 3:
            print('Name product: ' + lines[0])
            print('Count product: ', (int(lines[1]) // int(lines[2])))
        else:
            print('Name product: ' + lines[0])
            print('Count product: ', int(lines[1]))
        print('\n')