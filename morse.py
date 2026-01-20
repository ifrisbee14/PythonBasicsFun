english_morse_dict = {
    "A": ".-",
    "B": "-...",
}

def load_file(filename: str) -> list[str]:
    infile = open(filename, "r")
    lines = infile.readlines()
    infile.close()
    return lines

def main():
    # print ("Enter -m for enlgish to morse and -t for morse to english. /n Follow your commance with the input file name and output file name. /nCMD>", end="")
    # user_str = input()
    # args = user_str.split(" ")
    # conversion_type, infile_name, outfile_name = args
    lines = load_file("english.txt")
    print (lines)
    # if conversion_type == "-m":
    #     #TODO: call converted_lines = convert_english_to_morse(lines)
    #     # converted_lines = convert_english_to_morse(lines)
    #     pass
    # elif conversion_type == "-t":
    #     #TODO: call converted_lines = convert_morse_to_english(lines)
    #     pass
    # #TODO: call save_file(outfile_name, converted_lines)

main()