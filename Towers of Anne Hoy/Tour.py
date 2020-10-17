

# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Fall 2013.
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
from TOAHModel import TOAHModel

import time
        

def tour_of_four_stools(model: TOAHModel, delay_btw_moves: float=0.5, 
                        console_animate: bool=False) -> None:
    """Move a tower of cheeses from the first stool in model to the fourth.

       model - a TOAHModel with a tower of cheese on the first stool
                and three other empty stools
       console_animate - whether to animate the tour in the console
       delay_btw_moves - time delay between moves in seconds IF 
                         console_animate == True
                         no effect if console_animate == False
    """
    def move_three_stools(n: int, source: int, intermediate: int, 
                          destination: int) -> None:
        """
        Print moves to get n cheeses from source to destination, possibly
        using intermediate
        """
        if n > 1:
            move_three_stools(n - 1, source, destination, intermediate)
            move_three_stools(1, source, intermediate, destination)
            move_three_stools(n - 1, intermediate, source, destination)
        else:
            model.move(source, destination)
            
    def move_four_stools(model: TOAHModel, n: int, source: int, 
                         intermediate1: int, intermediate2: int, 
                         destination: int) -> None:
        """
        Print moves to get n cheeses from source to destination, possibly
        using intermediates
        """        
        def M(n) -> int:
            """
            return the minimum moves of moving n Cheeses on four stools
            >>> M(4)
            9
            """
            if n == 1:
                return 1
            else:
                moves = []
                for i in range(1, n):
                    moves.append(2 * M(n - i) + 2 ** i - 1)
                global mo
                mo = moves.copy()
    
            return min(moves)

        def find_i(n) -> int:
            """
            return the index of a in the global variable mo
            >>> find_i(9)
            1
            """
            return mo.index(n)

        def find(n):
            """
            return the index of M(n) in the global variable mo + 1
            since the index has a range from 1 to n(exclusive)
            >>>find(9)
            3
            """
            return find_i(M(n)) + 1
                        
        if n > 1:
            move_four_stools(model, n - find(n), source, 
                             intermediate2, destination, intermediate1)
            move_three_stools(find(n), source, intermediate2, destination)
            move_four_stools(model, n - find(n), intermediate1, 
                             source, intermediate2, destination)
        else:
            model.move(source, destination)
            
    move_four_stools(model, NUM_CHEESES, 0, 1, 2, 3)
    model2 = TOAHModel(4)
    model2.fill_first_stool(NUM_CHEESES)
    print(model2)
    for moves in model.get_move_seq()._moves:
        if console_animate:
            time.sleep(delay_btw_moves)
            model2.move(moves[0], moves[1])
            print(model2)

if __name__ == '__main__':
    NUM_CHEESES = 8
    DELAY_BETWEEN_MOVES = .5
    CONSOLE_ANIMATE = True
    
    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)    
    four_stools.fill_first_stool(number_of_cheeses=NUM_CHEESES)
    
    tour_of_four_stools(four_stools, 
                        console_animate=CONSOLE_ANIMATE,
                        delay_btw_moves=DELAY_BETWEEN_MOVES)
    
    print(four_stools.number_of_moves())

