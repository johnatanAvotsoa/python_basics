nbr = input("enter numbers :")
nbr = [int(i) for i in nbr.split()]
counted_nbr = []
vals = []
i = 0
for i in range(len(nbr)) :
    counter = 1
    if nbr[i] not in counted_nbr :
        counted_nbr.append(nbr[i])
        for j in range(i+1,len(nbr)) :
            if nbr[i] == nbr[j] :
                counter +=  1
        vals.append({
            "value" : nbr[i] ,
            "counter" : counter
        })
    else :

        i += 1
print(vals)
