def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)

    print(f"Found {num_words} total words")

def get_num_char(file_contents):
    lower_words = file_contents.lower()

    chars = {}
    for ch in lower_words:
        #print(f"Testing character: {ch}")
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1

    return chars

def sort_on(chars):
    char_lod = []
    
    for char, num in chars.items():
        char_list = {"char": char, "num": num}
        char_lod.append(char_list)
        
    def sort_helper(char_lod):
        return char_lod["num"]
    
    char_lod.sort(reverse=True, key=sort_helper)
    for i in char_lod:
        ch = i["char"]
        if not ch.isalpha():
            continue
        print(f"{i["char"]}: {i["num"]}")
    return char_lod
