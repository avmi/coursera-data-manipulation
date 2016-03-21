import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(r):
    s = r[1][0:-10]

    mr.emit_intermediate(s, 1)


def reducer(k, v):
    mr.emit(k)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
