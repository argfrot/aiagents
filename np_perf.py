# issue27174.py
import numpy as np
import threadpoolctl
import timeit
import pprint
import argparse


def test_inv(threads=-1):
    with threadpoolctl.threadpool_limits(limits=threads, user_api='blas'):
        info = threadpoolctl.threadpool_info()[0]
        t = timeit.Timer("np.linalg.inv(a)",
                 setup="import numpy as np; a = np.random.rand(1000, 1000)",
                 )
        out = t.repeat(number=10, repeat=5)
        info['benchmark time'] = out
        pprint.pprint(info)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--threads",
                       help="number of threads to use",
                       default=-1, type=int)
    args = parser.parse_args()
    test_inv(args.threads)
  