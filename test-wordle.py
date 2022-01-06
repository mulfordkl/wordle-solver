import wordle_clone

n_runs = 10000

def run_game(word_selection_method, n_runs):
    wins = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
    word_list = wordle_clone.get_initial_words(pop = False)
    for ii in range(n_runs):
        word = wordle_clone.get_word(word_list, "random")
        result = wordle_clone.play_game(word, word_list, word_selection_method, False)
        result = str(result)
        wins[result] += 1
    return wins

def print_results(wins, n_runs):
    for key in wins:
        if key == "0":
            print("Not Solved:\t{}\ttimes ({}%)".format(wins[key], (wins[key]/n_runs)*100))
        else:
            print("{} Turns:\t{}\ttimes ({}%)".format(key, wins[key], round((wins[key]/n_runs)*100,1)))
    print("\n\n")

wins_most_popular_selection = run_game("most_popular", n_runs)
wins_random_selection = run_game("random", n_runs)
wins_random_most_popular_selection = run_game("random_most_popular", n_runs)

print("Results selecting the most popular word at each loop")
print_results(wins_most_popular_selection, n_runs)
print("Results selecting a random word at each loop")
print_results(wins_random_selection, n_runs)
print("Results selecting from the most popular 10% of words at each loop")
print_results(wins_random_most_popular_selection, n_runs)

