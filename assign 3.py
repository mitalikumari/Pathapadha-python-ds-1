#1

def string_both_ends(str):
    if len(str)<2:
        return''
    return str[0:2]+str[-2:]
print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

#2

def add_string(str1):
    length=len(str1)
    if length>2:
        if str1[-3:]=='ing':
            str1+='ing'
            return str1
        print(add_string('ab'))
        print(add_string('abc'))
        print(add_string('string'))

#3

        def change_string(str1):
            return str1[-1:]+str1[1:-1]+str1[:1]
        print(change_string('abcd'))
        print(change_string('12345'))
