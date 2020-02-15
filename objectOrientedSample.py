# Object Oriented sample
print('---this is the start---', '\n')

# import self as self
#
#
# class Jobs:
#     def salary(self):
#         print("monthly salary")
#
#
# # note: the upper lines defines a class named Jobs.
# # question: why when I use salary as a method name, the pycharm prompt "method 'salary' may be static",
# #     and suggests to 'make function from method' or 'make method static'
# # question2: what does it mean by 'make function from method'?
#
# Jobs.salary(self)
#
# # job1 = jobs()
# # job1.salary()
# #
# # job2 = jobs()
# # job2.salary()
# # # note: assign a object to a variable

print('---本部分是一个最简单，无变量(属性)的class---', '\n')


# class Jobs:
#     gender = 'male'
#     age = '23'
#
#     @staticmethod
#     def salary():
#         print("hi, I am a static method")
#
#     def in_office(self):
#         print('well, I am a class method, I use variable like', Jobs.age, 'and', Jobs.gender)
# # note: 在class variable 中只要引用class variable, 只能用class.variable的格式，或者赋值，不能直接引用变量名，
# # 错误示范：print('well, I am a class method, I use variable like', age, 'and', gender)
#
# Jobs().salary()
# Jobs().in_office()

print('---本部分是一个带有static method 的class---', '\n')


class Jobs:
    def __init__(self, name, gender, age):
        self.gender = gender
        self.age = age
        self.name = name

    def salary(self):
        age = self.age
        name = self.name
        if age > 18:
            print('yes, we can pay you,', name)
        else:
            print('sorry, we can not hire you,', name)

    @staticmethod
    def rule():
        print('higher age, higher salary')


Nick = Jobs('Nick', 'male', 23)
Alex = Jobs('Alex', 'male', 16)
# create some objects belong  to the class Jobs

Nick.rule()
Nick.salary()
Alex.salary()
# note: static method also belong to the class, but it doesn't use the class variable
# note: as a class method, as long as it is defined, it can call the class's all variables.
print('---本部分是一个初始化了的class---', '\n')

print('---this is the end---')
# write at the end:
# question: 1. class的名字居然可以重复用？我这里用Jobs这个名字建立了两个不同的class
