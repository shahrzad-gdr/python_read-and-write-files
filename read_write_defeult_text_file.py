"""
+---------------------------------------------------------------+
+    How to read and write in a text file, using Python         +
+    in this project we use the default file to read and write  +
+---------------------------------------------------------------+
"""

read_path = "E:/"

number_list = []
with open(read_path+'input.txt') as read_file:
    content = read_file.readlines()
    for item in content:
        # print(item.strip())     # output: print each line in text file
        number = int(item.strip())
        number_list.append(number)
        print(number)           # output: print each number with integer type




write_path = "E:/"
with open(write_path+'output.txt', 'w') as write_file:
    for item in number_list:
        for i in range(0,item):
            write_file.write('*')
        write_file.write('\n')

