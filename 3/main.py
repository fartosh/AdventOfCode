import numpy

def load_claims(input_filename):
    wrong_IDs = []
    with open(input_filename) as f:
        for claim in [x.rstrip() for x in f.readlines()]:
            ID, _, position, size = claim.split()
            ID = int(ID.lstrip('#'))
            #print(str(ID))
            column, row = map(lambda x: int(x), position.rstrip(':').split(','))
            #print(str(column), str(row))
            size_x, size_y = map(lambda x: int(x), size.split('x'))
            #print(str(size_x), str(size_y))
            overlapped_y,overlapped_x = numpy.where(fabric[row:row+size_y, column:column+size_x] != 0)
            for i in range(overlapped_x.size):
                wrong_IDs.append(fabric[row+overlapped_y[i], column+overlapped_x[i]])
                wrong_IDs.append(ID)
            
            fabric[row:row+size_y, column:column+size_x] += ID
            fabric[row:row+size_y, column:column+size_x] = numpy.where(fabric[row:row+size_y, column:column+size_x] != ID, -1, fabric[row:row+size_y, column:column+size_x])
            #print(numpy.where(fabric[row:row+size_y, column:column+size_x] == -1))
            #print(fabric[row:row+size_y, column:column+size_x])
    #print(numpy.where(fabric == -1))
    wrong_IDs = list(set(wrong_IDs))
    for el in wrong_IDs:
        try:
            not_overlapped.remove(el)
        except ValueError:
            pass
    print(numpy.where(fabric == -1)[0].size)
    print(not_overlapped)


if __name__ == "__main__":
    inches = 1000
    not_overlapped = list(range(1,1001))
    fabric = numpy.zeros((inches,inches), dtype='int').reshape(inches,inches)
    input_filename = "input"
    load_claims(input_filename)

