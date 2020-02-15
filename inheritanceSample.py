class Clients:
    def __init__(self, name, region):
        Clients.name = name
        Clients.region = region

    def status(self):
        name = Clients.name
        region = Clients.region
        print(name, 'based in ', region)


ncrac = Clients('ncrac', 'Namibia')
ncrac.status()

cgi = Clients('cgi', 'South Africa')
cgi.status()


# this is the father class


# class Customers:
#     def __init__(self, name, amount):
#         self.name = name
#         self.amount = amount
#
#     def inquiry(self):
#         name = self.name
#         amount = self.amount
#         print(name 'want to buy ', amount 'units')


# this is another father class
# note: but there is a issue: the child class can't inherit the both father classes, if the second father class
# has some different arguments.

class Customers:
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def inquiry(self):
        name = self.name
        amount = self.region
        print(name, 'want to buy from', region)

    @staticmethod
    def message():
        print('hi, I want an aircon')

# this is the other father class too.


class ClientSA(Clients, Customers):
    def status(self):
        name = Clients.name
        region = Clients.region
        print(name, 'based in ', region, 'assigned to Allen')


tkkm = ClientSA('tkkm', 'Limpopo')
tkkm.status()
tkkm.message()
# tkkm.inquiry()

print('---this is the end---')
# at the end
# 子class在继承父class的过程中，如果有两个以上父class，那它继承谁的属性    ？如果都继承，那开始的属性应该怎样初始化？
