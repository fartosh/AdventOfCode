if __name__ == "__main__":
    frequency = 0
    frequencies = [frequency]
    input_filename = "input"
    found_double = False
    
    while not found_double:
        with open(input_filename, 'r') as f:
            for operation in [x.rstrip() for x in f.readlines()]:
                frequency = eval(str(frequency) + operation)
            
                if frequency in frequencies:
                    found_double = True
                    break
                else:
                    frequencies.append(frequency)
            print("frequency =", frequency)
    print("doubled frequency = ", frequency)
