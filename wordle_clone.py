from os import truncate
from random import randint

def get_initial_words(pop):
    word_list = []
    if pop == True:
        word_file = open("count_1w.txt", "r")
        content = word_file.read()
        line_list = content.split("\n")
        for line in line_list:
            word = line.split("\t")[0]
            if len(word) == 5:
                word_list.append(word)
    else:
        word_file = open("sgb-words.txt", "r")
        content = word_file.read()
        word_list = content.split("\n")        
    return word_list[:-1]

def get_word(word_list, method):
    if method == "most_popular":
        index = 0
    elif method == "rand_most_popular":
        index = randint(0, round(0.10*len(word_list), 0))   
    elif method == "random":
        index  = randint(0, len(word_list)-1)
    else:
        index = 0
    return word_list[index]

def check_word(guess, actual):
    actual_arr = list(actual)
    guess_arr = list(guess)
    hints = []

    for i in range(5):
        hint = {}
        if guess_arr[i] == actual_arr[i]:
            hint["val"] = "g"
            hint["pos"] = i
            hint["letter"] = guess_arr[i]
            hints.append(hint)
        elif guess_arr[i] in actual_arr:
            hint["val"] = "y"
            hint["pos"] = i
            hint["letter"] = guess_arr[i]
            hints.append(hint)
        else:
            hint["val"] = "b"
            hint["pos"] = i
            hint["letter"] = guess_arr[i]
            hints.append(hint)
    return hints    
 
def narrow_words(valid_words, hints):
    allowed_words = []
    for word in valid_words:
        allowed_flag = True
        word_arr = list(word)
        for k in range(len(word_arr)):
            if hints[k]["val"] == "g" and word_arr[k] != hints[k]["letter"]:
                allowed_flag = False
                break
            elif hints[k]["val"] == "y" and (hints[k]["letter"] == word[k] or hints[k]["letter"] not in word_arr):
                allowed_flag = False
                break
            elif hints[k]["val"] == "b" and hints[k]["letter"] in word_arr:
                allowed_flag = False
                break
        if allowed_flag:
            allowed_words.append(word)
    return allowed_words

def check_winner(hints):
    for hint in hints:
        if hint["val"] != "g":
            return 0
    return 1

def play_game(word, word_list, index_method, log):
    #word_list = get_initial_words(pop)
    true_word = word #get_word(word_list, "random")
    
    if log:
        print("True word: {}".format(true_word))
    allowed_words = word_list
    hints = []
    
    for j in range(6):
        if log:
            print("Number Allowed Words: {}".format(len(allowed_words)))
        guess = get_word(allowed_words, index_method)
        
        if log:
            print("Guess: {}".format(guess))
        hints = check_word(guess, true_word)
        win = check_winner(hints)
        if win == 1:
            if log:
                print("Win in {} steps".format(j+1))
            return j+1
        allowed_words = narrow_words(allowed_words, hints)
    if log:
        print("Did not win in 6 steps")
    return 0

