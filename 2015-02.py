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

#The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

#Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

#For example:

#A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
#A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
#All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

def get_side_areas_from_dimenstions(dims_str: str) -> tuple[int, int, int]:
    '''Helper function to get the three dimensions of a box from its dimensions string.'''
    tokens = dims_str.split('x')
    assert len(tokens) == 3, f'Invalid dimensions string: {dims}'
    dims = tuple(int(token) for token in tokens)
    side1, side2, side3 = dims[0]*dims[1], dims[1]*dims[2], dims[0]*dims[2]
    return side1, side2, side3

def get_smallest_side_area_from_dimenstions(sides: tuple[int, int, int]) -> int:
    '''Helper function to get the smallest side area from the three side areas of a box.'''
    return min(sides)   

def get_total_wrapping_paper_from_dimenstions(sides: tuple[int, int, int]) -> int:
    '''Helper function to get the total wrapping paper needed for a box from its three side areas.'''
    return 2 * sum(sides) + get_smallest_side_area_from_dimenstions(sides)
     

def solve_part1(data: typing.Any) -> typing.Any:
    total = 0
    for line in data.splitlines():
        sides = get_side_areas_from_dimenstions(line.strip())
        total += get_total_wrapping_paper_from_dimenstions(sides)
    return total

#The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, 
# which they would again like to be exact.

# The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each 
# present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet 
# of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

#For example:

#A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
#A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
#How many total feet of ribbon should they order?

def solve_part2(data: typing.Any) -> typing.Any:
    logger.debug('Starting Part 2 logic...')
    #total = 0
    #for line in data.splitlines():
        #sides = get_side_areas_from_dimenstions(line.strip())

    return 'Not Implemented'

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
