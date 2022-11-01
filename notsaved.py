#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    arset,res = set(ar), 0
    for item in arset:
		if ar.count(item):
			print()

if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

