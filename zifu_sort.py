def zimi_sort(l):
    bucket = {}
    for each_word in l:
        temp_key = ''.join(sorted(each_word))
        if temp_key not in bucket.keys():
            bucket[temp_key] = [each_word]
        else:
            bucket[temp_key].append(each_word)
    result = [each_value for each_value in bucket.values()]
    print(result)
l = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
zimi_sort(l)