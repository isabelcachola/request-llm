'''
Main script
'''
import argparse
import logging
import time

from example import data, models

def main(args):
    my_model = models.MyModel()
    my_dataset = data.MyDataset()

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--example')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

    start = time.time()
    # Do things here
    main(args)
    end = time.time()
    logging.info(f'Time to run script: {end-start} secs')