import numpy

def tsqr(A, blocksize):
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
    # print "MADE IT THIS FAR" 
    n = A.shape[1]
    while (i < numBlocks - 1):
        temp = numpy.empty((blocksize + theR.shape[0], n))
        temp[0:theR.shape[0]] = theR
        temp[theR.shape[0]:(theR.shape[0]+blocksize)] = array[i + 1]
        theR = numpy.linalg.qr(temp, 'r')
        i = i + 1
    return theR
