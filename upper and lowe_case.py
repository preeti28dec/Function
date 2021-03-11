def test():
    find="The quick Brow Fox"
    i=0
    UPPER_CASE=0
    lower_case=0
    while i<len(find):
        if find[i].isupper():
            UPPER_CASE+=1
        elif find[i].islower():
            lower_case+=1
        else:
            pass
        i+=1
    print(UPPER_CASE)
    print(lower_case)
test()