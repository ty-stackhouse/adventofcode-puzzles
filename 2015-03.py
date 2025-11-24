import logging
import os
import sys
import time
import typing

logger = logging.getLogger()

def read_input(filename: str = 'input.txt') -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    with open(file_path, 'r') as f:
        return f.read().strip()

#Santa is delivering presents to an infinite two-dimensional grid of houses.

#He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

#However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

#For example:

#> delivers presents to 2 houses: one at the starting location, and one to the east.
#^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
#^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

def count_houses(input_data: str, visited_houses: set) -> set:
    current_house = [0, 0]
    for c in input_data:
        if c == '^':
            current_house[1] += 1
        elif c == 'v':
            current_house[1] -= 1
        elif c == '<':
            current_house[0] -= 1
        elif c == '>':
            current_house[0] += 1
        visited_houses.add(tuple(current_house))
    return visited_houses

def solve_part1(data: typing.Any, visited_houses: set) -> typing.Any:
    if data is None:
        input_data = read_input()
    else:
        input_data = data   
    return count_houses(data, visited_houses)

#The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

#Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions 
#from the elf, who is eggnoggedly reading from the same script as the previous year.

#This year, how many houses receive at least one present?

#For example:

#^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
#^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
#^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

def solve_part2(data: typing.Any, visited_houses: set) -> typing.Any:
    input = read_input()
    input = input.replace('\r', '')
    santa_input = input[::2]
    robo_input = input[1::2]
    #logging.debug(santa_input)
    #logging.debug(robo_input)
    
    visited_houses = solve_part1(santa_input, visited_houses) 
    logging.debug(f'santa houses: {len(visited_houses)}')
    visited_houses2 = solve_part1(robo_input, visited_houses)
    logging.debug(f'robo houses: {len(visited_houses2)}')
    return visited_houses
    
def run_solver(func, data, label: str):
    visited_houses = {(0, 0)}
    logging.debug(f'visited_houses initialized: {visited_houses}')
    start_time = time.perf_counter()
    try:
        result = func(data, visited_houses)
        result = len(result)
        end_time = time.perf_counter()
        elapsed_ms = (end_time - start_time) * 1000
        
        logging.info(f'--- {label} ---')
        logging.info(f'Result: {result}')
        logging.info(f'Time:   {elapsed_ms:.4f} ms\n')
    except Exception as e:
        logging.error(f'Error in {label}: {e}', exc_info=True)

if __name__ == '__main__':
    log_level = logging.INFO
    
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'debug':
        log_level = logging.DEBUG

    logging.basicConfig(
        level=log_level,
        format='%(message)s', 
        datefmt='%H:%M:%S'
    )

    if log_level == logging.DEBUG:
        logging.debug('Debug logging enabled.')

    try:
        raw_input = read_input()
        
        run_solver(solve_part1, raw_input, 'Part 1')
        
        run_solver(solve_part2, raw_input, 'Part 2')
        
    except FileNotFoundError:
        logging.critical('Critical Error: \'input.txt\' not found in the script directory.')
    except Exception as e:
        logging.critical(f'Unexpected Error: {e}', exc_info=True)
