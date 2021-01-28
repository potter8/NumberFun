for i in range(int(input())):
    num1, num2, num3 = map(int, input().split())

    if num1+num2==num3 or num1-num2==num3 or num2-num1==num3 or num1*num2==num3 or num1/num2==num3 or num2/num1==num3:
        print("Possible")
    else:
        print("Impossible")



