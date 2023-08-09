'''
create a database in local storage

takes in an array (the tree) that contains input

returns an object (py dict) representation of a varibales
'''


class Data:
    """class Data: base data"""
    def __init__(self):
        self.varibales = {}

    def __str__(self):
        pass
    
    def __repr__(self):
        pass

    def read(self, id):
        """method read. returns a variable"""
        return self.variables[id]

    def read_all(self):
        """method read_all. returns all variables"""
        return self.variables

    def write(self, variable, expression):
        """method write. adds a var:expr to dict"""
        variable_name = variable_value
        self.variables[variable_name] = expression