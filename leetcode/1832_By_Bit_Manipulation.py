def checkIfPangram(sentence: str) -> bool:
    # Initialize seen = 0 since we start with no letter
    seen = 0

    # Iterate over each character in the sentence
    for curr_char in sentence:
        mapped_index = ord(curr_char) - ord('a')

        curr_bit = 1 << mapped_index

        seen |= curr_bit

    # Once we finish interating, check if 'seen' contains 26 bits of 1
    return seen == (1 << 26 ) - 1

if __name__ == "__main__":
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    print(checkIfPangram(sentence))        