cdef class CoordString:
    cdef int length
    cdef double *coords
    cdef readonly int rank
    cdef readonly int ring
    @staticmethod
    cdef CoordString new(double *coords, int length, int rank, int ring)
    cpdef CoordString slice(self, int start, int stop=?, int step=?)
    cdef double getX(self, int index)
    cdef double getY(self, int index)
    cdef double getZ(self, int index)
