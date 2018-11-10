#This test informs couples of their chance of having a child with sickel cell trait#
print("**|SICKLER CHILD TEST|**")
#Collect users name
name = input("Enter your name: ")
#Display the various genotypes for user to pick from 
print ("""Genotype
1: AA
2: AS
3: AC
4: SC
5: CC
6: SS""")
#Collect input for genotype and control for error
while True:
    try:
        genotype1 = int(input("Choose genotype: "))
        if genotype1 in range(1,7):
            break
    except ValueError:
            print("Please enter value between 1-6")
#Display name and genotype for confirmation
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

#Collect partner's name
name1 = input("Enter name of partner: ")

#Display list of Genotype for user to select from
print("""Genotype
1: AA
2: AS
3: AC
4: SC
5: CC
6: SS""")

#Take input for partner's genotype and control for error
while True:
    try:
        genotype2 = int(input("Choose genotype: "))
        if genotype2 in range(1,7):
            break
    except ValueError:
            print("Please enter value between 1-6")
            
#Redisplay Name and genotype of partner for confirmation
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

#Print advice based on user data
if genotype1 == genotype2 == "AA":
    print("%s, you and your partner %s are good to go!" %(name, name1))
elif genotype1 == "AA" and genotype2 == "AS":
    print(
        """%s, you and your partner are good to go. Here is a catch:
There's a 25 percent chance that one of your children
will carry the Sickler gene with no severe consequence.""" %(name)
          )
elif genotype1 == "AA" and genotype2 == "AC":
    print(
        """%s, you and your partner are good to go. Heare is a catch:
There's a 25 percent chance that one of your children will carry
the Sickler gene with no severe consequence.""" %(name)
          )
elif genotype1 == "AA" and genotype2 == "SC":
    print(
        """%s, you and your partner are good to go but all your children
will carry the Sickler gene with no severe consequence.
Please see a doctor or counsellor""" %(name)
          )
elif genotype1 == "AA" and genotype2 == "CC":
    print(
        """%s, you and your partner are good to go but all your children
will carry the Sickler gene with no severe consequence.
Please see a doctor or counsellor""" %(name)
          )
elif genotype1 == "AA" and genotype2 == "SS":
    print(
        """%s, you and your partner are good to go but all your children
          will carry the Sickler gene with no severe consequence.
          Please see a doctor or counsellor""" %(name)
          )
    
#Print advice based on user data
if genotype1 == genotype2 == "AS":
    print(
        """%s, There is a 25 percent chance you will have a sickler child
and another 25 percent chance one of your hildren will carry the sickler gene.
I'm sorry, see a doctor or councellor!""" %(name)
          )
elif genotype1 == "AS" and genotype2 == "AC":
    print(
        """%s, There is a 25 percent chance you will have a sickler child and
another 25 percent chance one of your children will carry the sickler gene.
I'm sorry, see a doctor or councellor!""" %(name)
          )
elif genotype1 == "AS" and genotype2 == "SC":
    print(
        """%s, There is a 25 percent chance you will have a sickler child and
another 25 percent chance one of your children will carry the sickler gene.
I'm sorry, see a doctor or councellor!""" %(name)
          )
elif genotype1 == "AS" and genotype2 == "CC":
    print(
        """%s, There is a 50 percent chance you will have a sickler child.
If youre lucky, all of your children will probably carry the sickler gene.
I'm sorry, see a doctor or councellor!""" %(name)
          )
elif genotype1 == "AS" and genotype2 == "SS":
    print(
        """%s, There is a 50 percent chance you will have a sickler child.
If youre lucky, all of your children will probably carry the sickler gene.
I'm sorry, see a doctor or councellor!""" %(name)
          )

#Print advice based on user data
if genotype1 == genotype2 == "AC":
    print(
        """%s, There is a 25 percent chance you will have a sickler child
and most of your children will carryt the sickler gene.
I'm sorry, see a doctor or councellor!""" %(name)
          )
elif genotype1 == "AC" and genotype2 == "SC":
    print("""%s, There is a 75 percent chane you will have a sickler child.
If you're lucky, all your children will probably carry the sickle cell gene.
I'm sorry, see a doctor or councellor!""" %(name)
          )
elif genotype1 == "AC" and genotype2 == "CC":
    print(
        """%s, There is a 75 percent chane you will have a sickler child.
If you're lucky, all your children will probably carry the sickle cell gene.
I'm sorry, see a doctor or councellor!""" %(name)
          )
elif genotype1 == "AC" and genotype2 == "SS":
    print("""%s, There is a 75 percent chane you will have a sickler child.
If you're lucky, all your children will probably carry the sickle cell gene.
I'm sorry, see a doctor or councellor!""" %(name)
          )


#Print advice based on user data
if genotype1 == genotype2 == "SC":
    print(
        """%s, This is not looking nice.
All your children will have sickel cell anaemia. Don't do this.
Please a doctor or councellor!""" %(name)
          )
elif genotype1 == "SC" and genotype2 == "CC":
    print(
        """%s, This is not looking nice. All your children will have sickel cell anaemia.
Don't do this. Please a doctor or councellor!""" %(name)
          )
elif genotype1 == "SC" and genotype2 == "SS":
    print(
        """%s, This is not looking nice.
All your children will have sickel cell anaemia.
Don't do this. Please a doctor or councellor!""" %(name)
          )


#Print advice based on user data

if genotype1 == genotype2 == "CC":
    print(
        """%s, This is not looking nice. All your children will have sickel cell anaemia.
Don't do this. Please a doctor or councellor!""" %(name)
          )
elif genotype1 == "CC" and genotype2 == "SS":
    print("""%s, This is not looking nice. All your children will have sickel cell anaemia.
Don't do this. Please a doctor or councellor!""" %(name)
          )

#Print advice based on user data
if genotype1 == genotype2 == "SS":
    print("""%s, This is not looking nice. All your children will have sickel cell anaemia.
I beg you, don't do this.
Please a doctor or councellor!""" %(name)
          )

print("Thank you for your patronage. Have a good life")





        
    
