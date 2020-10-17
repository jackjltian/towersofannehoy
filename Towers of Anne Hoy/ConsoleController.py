

# Copyright 2014 Dustin Wehr
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2014.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see .
"""
ConsoleController: User interface for manually solving Anne Hoy's problems 
from the console.

move: Apply one move to the given model, and print any error message 
to the console. 
"""

from TOAHModel import TOAHModel, Cheese, IllegalMoveError


def move(model: TOAHModel, origin: int, dest: int):
    '''
    Module method to apply one move to the given model, and print any
    error message to the console. 
    
    model - the TOAHModel that you want to modify
    origin - the stool number (indexing from 0!) of the cheese you want 
             to move
    dest - the stool number that you want to move the top cheese 
            on stool origin onto.        
    '''
    try: # one move
        model.move(origin, dest)
        model.moves += 1
    
    except IllegalMoveError:
        print('Please enter the right move')
    
    except IndexError:
        print('Please select the origin stool where there is at least one cheese on it')
        print('and cannot be out of range(0 to the number of stools you entered before minus 1')
    except ValueError:
        print('Please enter a number within 0 to the number of stools you entered before(without alphabetical letters')
    
    


class ConsoleController:
    
    def __init__(self: 'ConsoleController', 
                 number_of_cheeses: int, number_of_stools: int):
        """
        Initialize a new 'ConsoleController'.

        number_of_cheeses - number of cheese to tower on the first stool                            
        number_of_stools - number of stools
        """
        self.number_of_cheeses = number_of_cheeses
        self.number_of_stools = number_of_stools
        self.model = TOAHModel(number_of_stools)
        self.model.fill_first_stool(number_of_cheeses) 
                
    def play_loop(self: 'ConsoleController'):
        '''    
        Console-based game. 
        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've 
        provided to print a representation of the current state of the game.
        '''
        print('')
        print('Move the top cheese from the origin stool to the destination stool')
        print('by entering the number within the number of stools you have entered')
        print('(number between 0 to the number of stools you entered before minus one')
        print('since the order of stools starts with 0)')
        print('')
        print(self.model)
        origin = int(input('Please enter the original stool: '))
        dest = int(input('Please enter the destination stool: '))       
        move(self.model, origin, dest)
            
            


if __name__ == '__main__':
    # TODO: 
    # You should initiate game play here. Your game should be playable by
    # running this file.
    number_of_cheeses = int(input('Please enter the number of cheeses: '))
    number_of_stools = int(input('Please enter the number of stools: ')) 
    repeat = True
    game = ConsoleController(number_of_cheeses, number_of_stools)
          
    
    while repeat:
        game.play_loop()
        for i in range(1, number_of_stools):
            if len(game.model.stools[0]) == 0 and len(game.model.stools[i]) == number_of_cheeses:
                print('Congradulations! You have successfully finished the game')                
                second_round = input('Do you want to play again? enter Yes/No ')
                if second_round == 'Yes':
                    number_of_cheeses = int(input('Please enter the number of cheeses: '))
                    number_of_stools = int(input('Please enter the number of stools: '))
                    game = ConsoleController(number_of_cheeses, number_of_stools)
                elif second_round == 'No':
                    repeat = False
                    print('End of the game')
            
        
        
        

