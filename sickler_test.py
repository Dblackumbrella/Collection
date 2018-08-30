#This test informs couples of their chance of having a child with sickel cell trait#
print("**|SICKLER CHILD TEST|**")
#Collect users name#
name = input("Enter your name: ")
#Display the various genotypes for user to pick from# 
print ("""Genotype
1: AA
2: AS
3: AC
4: SC
5: CC
6: SS""")

while True:
    genotype1 = input("Choose genotype: ")
    genotype_1_int = int(genotype1)
    if genotype_1_int <= 0 or genotype_1_int > 6:
        print("Enter any of options 1-6")
    else:
        break
if genotype_1_int == 1:
    genotype_1_int = "AA"
print("%s you have selected %s as your genotype" %(name, genotype_1_int)) 
name1 = input("Enter name of partner: ")
print("""Genotype
1: AA
2: AS
3: AC
4: SC
5: CC
6: SS""")
while True:
    genotype2 = input("Choose %s's genotype: " %name1)
    genotype_2_int = int(genotype2)
    if genotype_2_int <= 0 or genotype_2_int > 6:
        print("Enter any of options 1-6")
    else:
        break
if genotype_2_int == 1:
    genotype_2_int = "AA"
print("%s you have selected %s as your partner's genotype" %(name, genotype_2_int)) 



        
    
