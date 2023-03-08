# Imports
import sys
from src import error, input_handler
from src.print_helper import print_colour

# Variables
command_data = {}

ABOUT_DETAILS = "This program runs applications as containers and helps developers debug their programs"

# Functions
def parse_command_data(function, handle, about, arguments):
    command_data[handle] = [function, about, arguments]

# Commands
@input_handler.command
def help(arguments):
    def general_help():
        print_colour("^Blue^About:")
        print_colour(ABOUT_DETAILS)
        
        # Make Commands first
        print("")
        print_colour("^Blue^Commands:")
        
        for handle, command in command_data.items():
            help = command[1]
            
            print_colour(handle + ": " + help)
            
        print("")
        
    def command_help():
        """"
        Gives extra detail about the nature of the command, their functions and arguments.
        """
        print_colour("^Blue^Still under development." + "\n")
        
        # Check if the argument matches any known commands
        com_handle = arguments[2]
        
        for handle, data in command_data.items():
            if handle == com_handle:
                matched = True
                
        # If matched, display the command data
        if matched:
            com_dat = command_data[com_handle]
            
            about = com_dat[1]
            com_args = com_dat[2]
            
            # Display the given data
            print_colour("^Blue^About:")
            print_colour(about + "\n")
            
            print_colour("^Blue^Arguments:")
            for argument, detail in com_args.items():
                print_colour(argument + ": " + detail)
                
            print_colour("")
        
        return
    
    if len(arguments) < 3:  
        return general_help()
    else:
        command_help()

@input_handler.command
def run(argument):
    print_colour("^Blue^Still under development")

# Main
def main():
    """
    Starts the program
    """
    
    # Adds command data
    parse_command_data(run, "run", "Runs programs as containers, requires a container image", {"None":"Nothing yet as functionality is not yet done"})
    parse_command_data(help, "help", "Lists out commands and their functions, may give more detail if command names are passed as arguments", 
                       {"Any command": "Lists out their arguments, functions etc."})

    # Get arguments
    arguments = sys.argv

    # Check arguments with commands
    arguments = input_handler.parse_arguments(arguments)
    
    if len(arguments) == 1:
        help(arguments)
        
    if len(arguments) >= 2:
        command = arguments[1] # Get command data
        matched = False
        
        # Create redirector here
        for handle, data in command_data.items():
            if handle == command:
                data[0](arguments)
                matched = True
                
        if matched == False:
            arguments_text = ""
            
            for argument in arguments:
                arguments_text += " " + argument + " " 
            
            e = error.CError("Argument given does not match known commands. Arguments: [" + arguments_text + "]")
            e.print()

main()