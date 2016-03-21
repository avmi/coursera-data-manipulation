import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(r):
    v = r[0]
    k = r[1]
    words = k.split()

    words_list = []
    for w in words:
        if w not in words_list:
            words_list.append(w)
            mr.emit_intermediate(w, v)

def reducer(k, v):
    mr.emit((k, v))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
