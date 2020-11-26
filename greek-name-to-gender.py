# request a name from the user
name_Is     =       input("Δώσε όνομα: ")

# Use for print on end
name_Real   =       name_Is

# make the name lowercase
name_Is     =       name_Is.lower()

# array ending of Greek names gender
array_Of_Name_Male_Ending   = ['ας', 'ος', 'ός', 'ης', 'ής', 'ων', 'ών', 'άμ', 'ύς', 'ως']
array_Of_Name_Female_Ending = ['α', 'η', 'ή', 'ω', 'ώ', 'υ', 'ύ']

if   name_Is.endswith( tuple(array_Of_Name_Male_Ending) ):
        # if the name is Male this will being executed
        print("Ending With Male Name:[♂] "   + name_Real)

elif name_Is.endswith( tuple(array_Of_Name_Female_Ending) ):
        # if the name is Female this will being executed
        print("Ending With Female Name:[♀] " + name_Real)

else:
        # if the name is Unknown this will being executed
        print("Ending With Unknown Gender Name: " + name_Real)