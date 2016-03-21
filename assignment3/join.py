import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(r):
    table = r[0]
    order_id = r[1]
    mr.emit_intermediate(order_id, r)

def reducer(k, v):
    id_order = 0
    id_items = []

    for index,r in enumerate(v):
        if(r[0] ==  "order"):
            id_order = index;
        elif(r[0] == "line_item"):
            id_items.append(index);

    for id_item in id_items:
        data_out = []
        order = v[id_order]

        for i in range(10):
            data_out.append(order[i])

        item = v[id_item]

        for i in range(17):
            data_out.append(item[i])

        mr.emit(data_out)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
