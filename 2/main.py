def count_checksum(input_filename):
    doubles = 0
    triples = 0
    
    with open(input_filename) as f:
        for ID in [x.rstrip() for x in f.readlines()]:
            found_double = False
            found_triple = False
            
            for letter in ID:
                if ID.count(letter) == 2:
                    if not found_double:
                        found_double = True
                        doubles += 1
                elif ID.count(letter) == 3:
                    if not found_triple:
                        found_triple = True
                        triples += 1
    return doubles*triples

def get_differences(s1, s2):
    differences = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            differences.append(i)
    return differences

def find_neighbours(input_filename):
    with open(input_filename) as f:
        IDs = [x.rstrip() for x in f.readlines()]
        for i in range(len(IDs)):
            s1 = IDs[i]
            for s2 in IDs[i+1:]:
                differences = get_differences(s1, s2)
                if len(differences) == 1:
                    return (s1,s2,differences[0])


if __name__ == "__main__":
    input_filename = "input"
    print(count_checksum(input_filename))
    s1,s2,difference = find_neighbours(input_filename)
    print(s1,s2,s1[:difference]+s1[difference+1:])
