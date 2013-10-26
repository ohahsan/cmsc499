import numpy
import tsqr_multi
import sys, os

A = numpy.random.rand(int(sys.argv[1]), int(sys.argv[2]))
R = tsqr_multi.tsqr(A, int(sys.argv[3]), int(sys.argv[4]))
if (len(sys.argv) == 6 and sys.argv[5] == "verify"):
    Rr = numpy.linalg.qr(A, 'r')
    print R
    print Rr
