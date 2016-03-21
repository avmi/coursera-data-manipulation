import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(r):
    m = r[0]
    l = r[1]
    c = r[2]
    v = r[3]

    if (m == "a"):
        mr.emit_intermediate((l, 0), (c, v))
        mr.emit_intermediate((l, 1), (c, v))
        mr.emit_intermediate((l, 2), (c, v))
        mr.emit_intermediate((l, 3), (c, v))
        mr.emit_intermediate((l, 4), (c, v))
    else:
        mr.emit_intermediate((0, c), (l, v))
        mr.emit_intermediate((1, c), (l, v))
        mr.emit_intermediate((2, c), (l, v))
        mr.emit_intermediate((3, c), (l, v))
        mr.emit_intermediate((4, c), (l, v))


def reducer(k, v):
    result = 0

    l = [0] * 5
    for pair in v:
        f = pair[0]

        if l[f] != 0:
            result = result + pair[1] * l[f]
            l[f] = 0
        else:
            l[f] = pair[1]

    mr.emit((k[0], k[1], result))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
