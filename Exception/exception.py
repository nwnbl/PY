print('enter two numbers for division:\n')
print('enter "q" to quit\n')

while(1):
    first=input("\nfirst number: ")
    if(first=='q'):
        break
    second=input("\nsecond number: ")
    if(second=='q'):
        break
    try:
        result=int (first)/ int (second)
    except ZeroDivisionError:
        pass
        #print('donnot devide zero!!!')
    else:
        print(int (result))
