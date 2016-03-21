import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(r):
    A = r[0]
    B = r[1]
    mr.emit_intermediate(A, 1)

def reducer(k, v):
    mr.emit((k, len(v)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
