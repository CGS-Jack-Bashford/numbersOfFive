def readIntoList(fileName):
    data = []
    try:
        f = open(fileName)
        line = f.readline()
        c = 1

        while line:
            data.append(float(line.strip()))
            line = f.readline()
            c += 1

    finally:
        return []

    return data
