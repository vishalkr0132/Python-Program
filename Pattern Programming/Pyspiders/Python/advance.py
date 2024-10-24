try:
    with open('new.txt', 'r') as fh:
        if fh.readable():
            data = fh.readline()
            print(data)
    print(data.swapcase())
except Exception as e:
    print(e)