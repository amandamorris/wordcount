# put your code here.
import string
import sys


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
        word = word.lower()
        final_word = ""
        for char in word:
            if char not in string.punctuation:
                final_word += char
        # word = word.translate(word.maketrans("", ""), string.punctuation)
        word_count[final_word] = word_count.get(final_word, 0) + 1
    return word_count


def print_counts(word_count):
    # for word in word_count:
    #     print "%s %d" % (word, word_count[word])
    for word, count in word_count.iteritems():
        print "%s %r" % (word, count)

# print_counts(make_count_dict(create_word_list("test.txt")))
# count_words("test.txt")

words = create_word_list(sys.argv[1])
word_count = make_count_dict(words)
print_counts(word_count)
