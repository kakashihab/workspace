# make a list of punctuation marks
punctuationmarks = [".", ",", ":", ";", "(", ")", '“', "”", "’", "-", "—", "?", "!", "…", "*", "[", "]", "$"]

# open the input and output files
infile = open("infile.txt")
outfile = open("words.txt", "w")

# create an empty dictionary
words_dictionary = {}

# read each line from the file
for line in infile:
    longest_word = ""

    # remove extra line feeds, convert the line to lower case
    line = line.rstrip().lower()

    # remove all punctuation marks from the line
    for mark in punctuationmarks:
        line = line.replace(mark, "")

    # at this point we should have a "sanitised" line 
    # with all extra characters removed
    print(line)

    # split up the line into a list of words
    # (default is to use a space as the separator between words)
    words = line.split()
    print(words)

    # look at each word in the list
    for word in words:
        print(word)

        # keep track of which is the longest word
        if len(word) > len(longest_word):
            longest_word = word

        # make a dictionary of the words
        # if the word is already there, add 1 to the count
        # if the word is not already there, set the counter to 1
        if word in words_dictionary:
            words_dictionary[word] += 1
        else:
            words_dictionary[word] = 1

    print("Longest word is : " + longest_word)
    print(longest_word, file=outfile)

# close the files
infile.close()
outfile.close()

print(words_dictionary)