
from time import time
start = time()
import sys
try:import dotenv;sys.stdin=open('in.txt','r')
except:pass
def log(*a):print(*a,file=sys.stderr)
MIIS=lambda:map(int,input().split())



log(f'Finished in {time()-start:.3f}sec')