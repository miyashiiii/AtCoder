
import random

import numpy as np
def main():

    start_row = [1,2,3,4,5,6]
    r = 1000
    # r = 1
    for i in range(r):
        l = []
        for v in start_row:
            l.append((i*7+v))
        print(" ".join(list(map(str,l))))



if __name__ == "__main__":
    main()
