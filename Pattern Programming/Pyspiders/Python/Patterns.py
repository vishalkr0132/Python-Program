n = int(input('Enter the number:'))
bin = 0
place = 1
while n > 1:
    rem = n % 2
    bin += rem * place