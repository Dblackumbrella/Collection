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
    try:
        genotype1 = int(input("Choose genotype: "))
        if genotype1 in range(1,7):
            break
    except ValueError:
            print("Please enter value between 1-6")
            
if genotype1 == 1:
    genotype1 = "AA"
elif genotype1 == 2:
    genotype1 = "AS"
elif genotype1 == 3:
    genotype1 = "AC"
elif genotype1 == 4:
    genotype1 = "SC"
elif genotype1 == 5:
    genotype1 = "CC"
elif genotype1 == 6:
    genotype1 = "SS"
    
print(name)
print("Genotype %s" %(genotype1))
name1 = input("Enter name of partner: ")
print("""Genotype
1: AA
2: AS
3: AC
4: SC
5: CC
6: SS""")

while True:
    try:
        genotype2 = int(input("Choose genotype: "))
        if genotype2 in range(1,7):
            break
    except ValueError:
            print("Please enter value between 1-6")
            
if genotype2 == 1:
    genotype2 = "AA"
elif genotype2 == 2:
    genotype2 = "AS"
elif genotype2 == 3:
    genotype2 = "AC"
elif genotype2 == 4:
    genotype2 = "SC"
elif genotype2 == 5:
    genotype2 = "CC"
elif genotype2 == 6:
    genotype2 = "SS"
    
print("your partner %s" %(name1))
print("genotype: %s:" %(genotype2))
if genotype1 == genotype2 == "AA":
    print("%s, you and your partner %s are good to go!" %(name, name1))
elif genotype1 == genotype2 == "AS":
    print("%s, This is disy but you and your partner %s are good to go with caution!" %(name, name1))
elif genotype1 == genotype2 == "AC":
    print("%s, This is disy. The risk is high. You and your partner %s acan proceed with caution!" %(name, name1))
elif genotype1 == genotype2 == "SC":
    print("%s, This is not looking nice. Please the doctor or councellor!" %(name))
elif genotype1 == genotype2 == "CC":
    print("%s, I'am afraid this is not looking nice. Please the doctor or councellor!" %(name))
elif genotype1 == genotype2 == "SS":
    print("%s, I'm afraid you have to say your goodbyes. Please see doctor or councellor!" %(name))


        
    
