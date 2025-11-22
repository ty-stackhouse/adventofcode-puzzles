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

    
# Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

# An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

# The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

# For example:

# (()) and ()() both result in floor 0.
# ((( and (()(()( both result in floor 3.
# ))((((( also results in floor 3.
# ()) and ))( both result in floor -1 (the first basement level).
# ))) and )())()) both result in floor -3.
# To what floor do the instructions take Santa?

def solve_part1(data: typing.Any) -> typing.Any:
    logger.debug('Starting Part 1 logic...')
    floor = 0
    for line in str(data).splitlines():
        for c in line.strip():
            if c == '(':
                floor += 1
            elif c == ')':
                floor -= 1
    return floor

#Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

#For example:

#) causes him to enter the basement at character position 1.
#()()) causes him to enter the basement at character position 5.
#What is the position of the character that causes Santa to first enter the basement?

def solve_part2(data: typing.Any) -> typing.Any:
    logger.debug('Starting Part 2 logic...')
    floor = 0
    position = 0
    for line in str(data).splitlines():
        for c in line.strip():
            position += 1
            if c == '(':
                floor += 1
            elif c == ')':
                floor -= 1
            if floor == -1:
                return position
    return None

def run_solver(func, data, label: str):
    start_time = time.perf_counter()
    try:
        result = func(data)
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
