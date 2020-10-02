import numpy as np
import logging

import wahoovian

def main(matrix):
    logging.basicConfig(filename='Wahoovian-log.txt', level=logging.DEBUG,
                        filemode='w',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')

    logging.info('Beginning program now')
    
    wahoovian.wahoovian(matrix)

    logging.info('Leaving program now')

    print(matrix)

    

#array1 = np.array(  [[1, 2], [3, 4]]  )
array1 = np.array(  [[1], []]  )

#print(main(array1))
#print(main(array2))

if __name__ == '__main__':
    main(array1)