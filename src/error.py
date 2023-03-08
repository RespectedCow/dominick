from src.print_helper import print_colour

class CError:
    def __init__(self, error):
        self.error = error
        
    def print(self):
        print_colour("Systems encountered an error")
        print_colour("^Red^`Error:` " + self.error)
        

def check_errors(arguments):
    if len(arguments) == 1:
        error = CError("No argument given. Arguments: [" + arguments[0] + "]")
        return error
    
    return True