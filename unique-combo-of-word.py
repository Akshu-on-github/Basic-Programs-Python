def uniquecombos(word):
    """_get all unquie combinations of a word

    Args:
        word (string): a word
    Returns:
        list: unique combinations of a word_
    """  
    arr = list(word)
    list1 = []
    list2 = []
    i = 0
    j = 1
    while i<len(arr):
        j= i+1
        for k in arr:
            k = arr[i:j]
            list1.append(k)
            out = listToString(k)
            list2.append(out)
            j += 1
        i += 1
    combos = removeduplicates(list2)
    print(combos)
    return combos

def removeduplicates(x):
    """checks there are no duplicates in a string

    Args:
        x (list): a list
    Returns:
        list: list without any repeats
    """    
    return list(dict.fromkeys(x))

def listToString(s):
    """turns list to  a string

    Args:
        s (list): list of letters
    Returns:
        string: word
    """    
    str1 = ""
    for ele in s:
        str1 += ele

    return str1

if __name__ == "__main__":
    word = input("Enter your word:")
    uniquecombos(word)
