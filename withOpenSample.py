# import inheritanceSample as inhs
#
# bho = inhs.Clients('BHO', 'Thailand')
# bho.status()
#
# # this is to import other files

file = open("allen.txt")
content = file.read()
print(content)
file.close()
print("\n")
# open and close a file

with open('C:/Users/Administrator/Desktop/haha.txt') as f:
    print(f.read())
# 用with open语句打开，并读文件，
# question: 用with op en语句打开文件，为什么不需要close?

