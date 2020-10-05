import numpy as np
import logging

import wahoovian

def main():
    logging.basicConfig(filename='Wahoovian-log.txt', level=logging.DEBUG,
                        filemode='w',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')

    logging.info('Beginning program now')

    array1 = np.array([[1, 2], [3, 4]])
    array2 = np.array([[1], [2]])
    
    m1 = wahoovian.wahoovian(array1)
    print(m1, "\n")

    m2 = wahoovian.wahoovian(array2)
    print(m2)

    logging.info('Leaving program now')

if __name__ == '__main__':
    main()