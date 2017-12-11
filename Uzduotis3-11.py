list1 =[1, 6, 5]
list2 = [4, 5, 6]

print("PROC1".ljust(9)+"|"+"PROC2".ljust(9)+"|")
for sk1, sk2 in zip(list1, list2):
    if (sk1+sk2) >=10:
        print (("*" * sk1).ljust(9) + "|" + ("*" * sk2).ljust(9) + "| X" )
    else:
        print (("*" * sk1).ljust(9) + "|" + ("*" * sk2).ljust(9) + "|")
    
