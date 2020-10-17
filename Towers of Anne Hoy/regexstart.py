#class Tree:
    #"""Bare-bones Tree ADT"""

    #def __init__(self,
                 #value=None, children=None):
        #"""Create a node with value and any number of children"""

        #self.value = value
        #if not children:
            #self.children = []
        #else:
            #self.children = children[:] # quick-n-dirty copy of list

    #def __repr__(self):
        #"""Return representation of Tree as a string"""

        #return ('Tree(' + repr(self.value) + ', ' +
                #repr(self.children) + ')')
                
#class TernaryAlphabet:
    #"""Define ternary alphabet"""
    
    #def __init__(self):
        #"""Create class of ternary alphabet {0,1,2}"""
        
        
            
class regex:
    """The single, length one regex."""
    
    def __init__(self, value):
        """
        Creates a regex of length one from ternary alphabet.
        >>>regex('1')
        '1'
        """
        
        if value in (0, 1, 2, 'e'):
            self.value = value
        else:
            raise Exception('Follow the ternary alphabet fomrat!')
    
    def __repr__(self):
        """Return representation of length one regex as string."""
        
        return "'" + str(self.value) + "'"
    

class regex_dot:
    """Regex class for the dot internal node."""
    
    def __init__(self, regex1, regex2):
        """
        Create a (.) node number with two regexes.
        """
        
        self.regex1 = regex1
        self.regex2 = regex2
        self.value = '(' + str(self.regex1.value) + '.' + str(self.regex2.value) + ')'         
            
    def __repr__(self):
        """Return representation of dot regex as a string"""
        
        return "'" + ('(' + str(self.regex1.value) + '.' + str(self.regex2.value) 
                + ')') + "'"

class regex_slash:
    """Regex class for the slash (|) node."""
    
    def __init__(self, regex1, regex2):
        """
        Create a (|) node number with 2 regexes.
        """
        
        self.regex1 = regex1
        self.regex2 = regex2
        self.value = '(' + str(self.regex1.value) + '.' + str(self.regex2.value) + ')'
    
    def __repr__(self):
        """Return representation of slash regex as a string"""
                       
        return "'" + ('(' + str(self.regex1.value) + '.' + str(self.regex2.value) 
                        + ')') + "'"

class regex_star:
    """Regex class for the star (*) node."""
        
    def __init__(self, regex1):
        """
        Create a (*) node number with one regex.
        """
            
        self.regex1 = regex1
        self.value = '(' + str(self.regex1.value) + ')'
        
    def __repr__(self):
        """Return representation of star regex as a string"""
                           
        return "'" + str(self.regex1.value) + '*' + "'"   
    
if __name__ == "__main__":
    a=regex(1)
    b=regex('e')
    c=regex_dot(a,b)
    d=regex_slash(a,c)
    e=regex_slash(c,d)
    f=regex_star(d)
    