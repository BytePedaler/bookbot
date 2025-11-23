def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)

    print(f"Found {num_words} total words")

def get_num_char(file_contents):
    normalized = file_contents.lower()

    chars = {}
    for ch in normalized:
        #print(f"Testing character: {ch}")
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1

    print(f"{chars}")

    return chars