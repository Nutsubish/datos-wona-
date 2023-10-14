
#exlapi =float(input("exlapi: "))

#exlap  =float(input("exlap:"))

#sum = exlap + exlapi
#print("sum: "+ str(sum))

#temp = 15

#if temp > 30:
    #print("its a hot day")
    #print("dwink wataa")
#elif temp > 20: #(20,30,infinityyyyy)
    #print("its a nice day")   
#elif temp > 10:
    #print("its little cold")
#else:
    #print("its cold")
#print("done")

weight = int(input("weight: "))
unit = input("(K)g tu (L)bs")
if unit.upper() == "K":
    convet = weight / 0.45
    print("weight in Lbs:" + str(convet))
else:
    convet = weight * 0.45
    print("weight in Kgs: " + str(convet))

    






