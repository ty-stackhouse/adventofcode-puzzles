import logging
import os
import sys
import time
import hashlib
import typing

logger = logging.getLogger()

def read_input(filename: str = 'input.txt') -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    with open(file_path, 'r') as f:
        return f.read().strip()

# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.
def solve_part1(data: typing.Any) -> typing.Any:
    logger.debug('Starting Part 1 logic...')
    # Convert the input data into a string
    secret_key = data
    
    # Initialize the number
    number = 0
    
    while True:
        # Create the MD5 hash
        md5_hash = hashlib.md5(f"{secret_key}{number}".encode()).hexdigest()
        
        # Check if the hash starts with at least five zeroes
        if md5_hash.startswith('00000'):
            return number
        
        # Increment the number
        number += 1
        
        # Add debug statement every 100 checksums
        if number % 100 == 0:
            logger.debug(f'Processed {number} checksums')

def solve_part2(data: typing.Any) -> typing.Any:
    logger.debug('Starting Part 2 logic...')
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
        logger.debug('Debug logging enabled.')

    try:
        raw_input = read_input()
        
        run_solver(solve_part1, raw_input, 'Part 1')
        
        run_solver(solve_part2, raw_input, 'Part 2')
        
    except FileNotFoundError:
        logging.critical('Critical Error: \'input.txt\' not found in the script directory.')
    except Exception as e:
        logging.critical(f'Unexpected Error: {e}', exc_info=True)
