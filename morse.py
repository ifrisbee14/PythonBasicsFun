english_morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

def load_file(filename: str) -> list[str]:
    infile = open(filename, "r")
    lines = infile.readlines()
    infile.close()
    return lines

def convert_english_to_morse(lines: list[str]) -> str:
    converted_text = ""
    for line in lines:
        line = line.upper()
        print(repr(line))
        for char in line:
            print(repr(line))
            if char in english_morse_dict:
                converted_text += english_morse_dict[char] + " "
            elif char == " " or char == "\n":
                converted_text += char
            else:
                print ("Unrecognized character")
    
    return converted_text

def main():
    print ("Enter -m for enlgish to morse and -t for morse to english. /n Follow your commance with the input file name and output file name. /nCMD>", end="")
    user_str = input()
    args = user_str.split(" ")
    conversion_type, infile_name, outfile_name = args
    lines = load_file("english.txt")
    print (lines)
    if conversion_type == "-m":
        converted_text = convert_english_to_morse(lines)
        print ("converted text:", converted_text)
    elif conversion_type == "-t":
        #TODO: call converted_lines = convert_morse_to_english(lines)
        pass
    #TODO: call save_file(outfile_name, converted_lines)

main()