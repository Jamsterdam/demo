try:
    print(10 / "t")
# except:
#     print('wrong')
# except ArithmeticError:
#     print("you can't divide 0")

except ArithmeticError as e:
    print(e)
except TypeError as e:
    print(e, "\n", "字符不能与数字运算")
except:
    print("something is wrong")

