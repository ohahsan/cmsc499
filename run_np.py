import numpy
import tsqr_imp
import sys, os

A = numpy.random.rand(int(sys.argv[1]), int(sys.argv[2]))
# R = tsqr_imp.tsqr(A, int(sys.argv[3]))
R = numpy.linalg.qr(A, 'r')
# print R - Rr
