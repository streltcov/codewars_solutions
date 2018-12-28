# Define a method 'hello' that returns "Hello, Name!" to a given parameter 'name', or says 'Hello, World!'
# if name is not given (or passed an empty string)

def hello(name = None):
    return 'Hello, World!' if name == '' or name == None else 'Hello, ' + name.title() + '!'
