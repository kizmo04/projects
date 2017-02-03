def search(key, source):
    length = len(source)
    index = 0
    while index < length:
        cur_char = source[index]
        if cur_char == key:
            return index
        index += 1
    return 0

def search2(key, source):
    for index, char in enumerate(source):
        if char == key:
            return index

    return 0


source = 'lux, the Lady of Luminasity'
result = search('o', source)
print(result)

result2 = search2('f',source)
print(result2)


