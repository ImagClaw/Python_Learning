from tqdm import tqdm
import time
#from multiprocessing import pool as ThreadPool
#
#def make_pi(num):
#    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
#    for j in range(num):
#        if 4 * q + r - t < m * t:
#            yield m
#            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
#        else:
#            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


# = 200000  # set number of digits
#print(mp.pi)   # print pi to a thousand places
try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp


def main():

    #pool_size = 10
    #my_array = []

    #pool = ThreadPool.Pool(pool_size)
    mp.dps = str(int(input("Enter a nth degree of pi you want: ")))

    bd = input("Enter your birthday (MM-DD-YY): ")
    bd = bd.replace("-", "")
    start = time.time()
    found = str(mp.pi)
    end = time.time()
    print("Big string incoming:\n ", found)
    print("Time Duration: {:.2f} seconds".format(end-start))
    


if __name__ == "__main__":
    main()