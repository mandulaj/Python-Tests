def combinations(List,length):
    final = ""
    if length > 0:
        for i in List:
            final += i+combinations(List,length-1)
        return

combinations([1,2,3],3)
