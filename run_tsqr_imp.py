import numpy
import tsqr_imp
import sys, os

A = numpy.random.rand(int(sys.argv[1]), int(sys.argv[2]))
R = tsqr_imp.tsqr(A, int(sys.argv[3]))
if (len(sys.argv) == 5 and sys.argv[4] == "verify"):
    Rr = numpy.linalg.qr(A, 'r')
    print R
    print Rr
