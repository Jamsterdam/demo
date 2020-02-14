# Object Oriented sample
import self as self


class Jobs:
    def salary(self):
        print("monthly salary")


# note: the upper lines defines a class named Jobs.
# question: why when I use salary as a method name, the pycharm prompt "method 'salary' may be static",
#     and suggests to 'make function from method' or 'make method static'
# question2: what does it mean by 'make function from method'?

Jobs.salary(self)

# job1 = jobs()
# job1.salary()
#
# job2 = jobs()
# job2.salary()
# # note: assign a object to a variable

print('---this is the end---')
# write at the end:
# question:
