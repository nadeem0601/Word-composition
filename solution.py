def is_construction_possible(word, words_set, is_original=True) -> bool:
    """
        -param: `word` The current word under verification
        -param: `words_set` The set of words from the input file
        -param: `is_original` A flag indicating whether the current word is the original or new constructed one

        Returns: bool - `True` if the word can be constructed otherwise `False`.
    """

    if word in words_set and not is_original:
        return True
    
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]

        if prefix in words_set and is_construction_possible(suffix, words_set, is_original=False):
            return True
        
    return False

def find_longest_compound_words(file_path: str) -> tuple:
    with open(file_path, 'r') as file:
        words =[line.strip() for line in file.readlines()]

    
    words_set = set(words)

    words.sort(key=len, reverse=True)  

    longest_word, second_longest_word = None, None

    for  current_word in words:

        if is_construction_possible(current_word, words_set):

            if longest_word is None:
                longest_word = current_word
            elif second_longest_word is None:
                second_longest_word = current_word

                break

    return longest_word, second_longest_word

if __name__ == "__main__":
    import time

    #Test for Input_01.txt
    start_time = time.time()
    longest, second_longest = find_longest_compound_words("Input_01.txt")
    print(f"Input_01.txt Results:")
    print(f"1. Longest Compound Word: {longest}")
    print(f"2. Second Longest Compound Word: {second_longest}")
    print(f"Time taken: {time.time() - start_time:.4f} seconds\n")

    #Test for Input_02.txt
    start_time =time.time()
    longest,second_longest = find_longest_compound_words("Input_02.txt")
    print(f"Input_02.txt Results:")
    print(f"1. Longest Compound Word: {longest}")
    print(f"2. Second Longest Compound Word: {second_longest}")
    print(f"Time taken: {time.time() - start_time:.4f} seconds")


