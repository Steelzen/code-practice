# I need a function called decode(message_file) that can read in an encoded message from a .txt file and return the decoded version as a string.
# Here's an example of what the message_file .txt file will look like:
# 3 love
# 6 computers
# 2 dogs
# 4 cats
# 1 I
# 5 you
# As you can see, each word is associated with a number. Imagine you ordered all those numbers from smallest to biggest and arranged them into a pyramid. Each line of the pyramid includes one more number than the line before it:
# 1
# 2 3
# 4 5 6
# The numbers at the end of each line (1, 3 and 6) correspond to the words that are part of the message. You should ignore all the other words. So for the example input file above, the message words are:
# 1: I
# 3: love
# 6: computers
# and your function should return the string "I love computers"

# Path: Coding_Starter_Assesment/decode.py
def decode(message_file):
    with open(message_file, 'r') as f:
        lines = f.readlines()
        lines = [line.strip().split() for line in lines]
        lines = [[int(line[0]), line[1]] for line in lines]
        lines.sort(key=lambda x: x[0])
        lines = [lines[(i * (i + 1) // 2) - 1] for i in range(1, len(lines)) if (i * (i + 1) // 2) - 1 in range(len(lines))]

        ans = ""
        for line in lines:
            ans += line[1] + " "

        return ans.strip()

if __name__ == "__main__":
    print(decode("coding_qual_input.txt"))    