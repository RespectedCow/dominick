# Functions
def parse_arguments(arguments):
    return arguments

def command(func):
    def inner(argument):
        func(argument)
    return inner