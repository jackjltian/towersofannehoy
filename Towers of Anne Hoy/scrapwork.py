def move_cheeses3(n: int, source : int, intermediate : int, destination : int) -> None:
    if n > 1:
        move_cheeses(n - 1, source, destination, intermediate)
        move_cheeses(1, source, intermediate, destination)
        move_cheeses(n -1, intermediate, source, destination)
    else:
        model.move(source, destination)

def move_cheeses4(n: int, source: int, intermediate1: int, intermediate2: int, destination: int) -> None:
    if n > 1:
        move_cheeses4(n - min_i(model.number_of_cheeses()), source, intermediate2, destination, intermediate1)
        move_cheeses3(min_i(model.number_of_cheeses()), source, intermediate2, destination)
        move_cheeses4(n - min_i(model.number_of_cheeses()), intermediate1, source, intermediate2, destination)
    else:
        if console_animate == True:
            print(model)
            time.sleep(delay_btw_moves)
        model.move(source, destination)
    move_cheeses4(model.number_of_cheeses(), 0, 1, 2, 3)
    print (model)