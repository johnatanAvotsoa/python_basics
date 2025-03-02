def compress(array):
    counted = []
    compressed = []
    for i in range(len(array)) :
        j = i + 1
        counter = 1
        if array[i] not in counted :
            counted.append(array[i])
            for j in range(i+1, len(array)):
                if array[j] == array[i] :
                    counter += 1
            compressed.append({
                "value" : array[i] ,
                "occurrences" : counter
            })
        else:
            i += 1

    return compressed

def decompress(compressed) :
    decompressed = []
    for element in compressed :
        for i in range(int(element["occurrences"])) :
            decompressed.append(element["value"])
    return decompressed

names = input("enter some names : ");
names = names.split(" ")
print(f"compresses = {compress(names)}")
print(f"decompresses = {decompress(compress(names))}")


