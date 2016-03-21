import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(r):
    A = r[0]
    B = r[1]

    mr.emit_intermediate((A, B), 1)
    mr.emit_intermediate((B, A), 0)

def reducer(k, v):
    if (sum(v) == 0):
        mr.emit((k[0], k[1]))
        mr.emit((k[1], k[0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
