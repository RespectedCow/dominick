import colorama
colorama.init(autoreset=True)

TEXT_COLOURS = {
    "Green": colorama.Fore.GREEN,
    "Blue": colorama.Fore.BLUE,
    "Red": colorama.Fore.RED
}

# Main
def print_colour(text, color_character="^", boundary_character="`"):
    new_text = {}
    word_index = 0
    colour = {}
    colour_mode = False
    selection_mode = False
    text_mode = False
    
    # Seperate out text with styles and none
    for character in text:
        # Mode checks
        if character == boundary_character:
            selection_mode = not selection_mode
            if selection_mode:
                new_text[word_index] = ""
            else:
                word_index += 1
                
        if character == color_character:
            colour_mode = not colour_mode
            if colour_mode:
                if colour.__contains__(word_index) == False:
                    colour[word_index] = ""
            
        if colour_mode and not selection_mode:
            if character != color_character:
                if colour.__contains__(word_index) == False:
                    colour[word_index] = ""
                colour[word_index] += character
            
        if selection_mode and not colour_mode:
            if character != boundary_character:
                new_text[word_index] += character
        
        if not selection_mode and not colour_mode:
            if character != boundary_character and character != color_character:
                text_mode = True
            
                if new_text.__contains__(word_index) == False:
                    new_text[word_index] = ""
                
                new_text[word_index] += character
        elif text_mode:
            text_mode = False
            word_index += 1
                
    # Printing the text
    index = 0
    echo_text = ""
    for word in new_text:
        word = new_text[index]
        word_colour = None
        if colour.__contains__(index):
            word_colour = colour[index]
        
        if word_colour != None:
            word_colour = TEXT_COLOURS[word_colour]
            echo_text += word_colour + word
        else:
            echo_text += colorama.Fore.WHITE + word 
        
        index += 1
    
    print(echo_text)