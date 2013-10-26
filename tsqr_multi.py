import numpy
import threading

# TODO (maybe)
# def combine_qr(array): 

def seq_tsqr(A, blocksize, threadNum, resultArray):
    array = []
    m = A.shape[0]
    i = 0
    numBlocks = m / blocksize
    while (i < numBlocks):
        array.append(A[(i * blocksize):((i + 1) * blocksize), :])
        i = i + 1
    i = 1
    temp = numpy.empty((2 * blocksize, A.shape[1]))
    temp[0:blocksize, :] = array[0]
    temp[blocksize:(2 * blocksize), :] = array[1]
    theR = numpy.linalg.qr(temp, 'r')
    n = A.shape[1]
    while (i < numBlocks - 1):
        temp = numpy.empty((blocksize + theR.shape[0], n))
        temp[0:theR.shape[0]] = theR
        temp[theR.shape[0]:(theR.shape[0]+blocksize)] = array[i + 1]
        theR = numpy.linalg.qr(temp, 'r')
        i = i + 1
    resultArray[threadNum] = theR

# ASSUMPTIONS:
# blocksize divides (n / numThreads) cleanly
# EXAMPLE: (A is 100x10, 5, 10) is LEGAL b/c 5 divides 10
# EXAMPLE: (A is 100x10, 15, 5) is ILLEGAL b/c 15 does not divide 20
def tsqr(A, blocksize, numThreads):
    (m, n) = A.shape
    rowsPerThread = m / numThreads;
    array = []
    rArray = []
    threads = []
    for i in range(0, numThreads):
        thisBlock = A[(i * rowsPerThread):((i + 1) * rowsPerThread), :]
        array.append(thisBlock)
        threads.append(threading.Thread(
            target=seq_tsqr, args=(thisBlock, blocksize, i, rArray, )))
        threads[i].start
    for i in range(0, numThreads):
        threads[i].join
    theR = array[0]
    for j in range(0, numThreads - 1):
        r1 = array[j].shape[0]
        r2 = array[j + 1].shape[0]
        temp = numpy.empty((r1 + r2, n))
        temp[0:r1] = array[j]
        temp[r1:(r1 + r2)] = array[j + 1]
        array[j + 1] = numpy.linalg.qr(temp, 'r')
        theR = array[j + 1]
    return theR
