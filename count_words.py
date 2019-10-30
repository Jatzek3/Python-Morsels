def count_words1(string):
    list_of_words = string.split(" ")
    dict = {}
    for word in list_of_words:
        word.strip()
        if word not in dict.keys():
            dict[word] = 1
        else:
            dict[word] += 1
    print(dict)

def count_words2(string):
    list_of_words = string.split(" ")
    separate_words = []
    for word in list_of_words:
        if word not in separate_words:
            word = word.strip()
            separate_words.append(word)
    words_count = []
    for i in separate_words:
        i = i.strip()
        words_count.append(list_of_words.count(i))
    dictionary = dict(zip(separate_words, words_count))
    print(dictionary)

