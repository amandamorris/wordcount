# put your code here.
def create_word_list(filename):
    my_file = open(filename)
    words = []
    for line in my_file:
        line = line.rstrip()
        words_per_line = line.split(" ")
        words = words + words_per_line
    my_file.close()
    return words


def make_count_dict(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


def print_counts(word_count):
    # for word in word_count:
    #     print "%s %d" % (word, word_count[word])
    for word, count in word_count.items():
        print "%s %r" % (word, count)

# print_counts(make_count_dict(create_word_list("test.txt")))
# count_words("test.txt")

words = create_word_list("test.txt")
word_count = make_count_dict(words)
print_counts(word_count)
