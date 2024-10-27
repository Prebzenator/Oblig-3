
# Beregner lengden på en gitt string
# Argumenter: String (Str): Strengen som skal måles
# Return: int: Antall bokstaver i strengen


def my_str_len(string):
    Antall_bokstaver = 0 
    for bokstaver in string:
        Antall_bokstaver += 1
    return Antall_bokstaver
print("Antall bokstaver i Preben er", my_str_len("Preben"))

# Beregner lengden på en gitt string
# Argumenter: String (Str): Strengen som skal måles
# Returns: List: En liste med lengdenpå hver string

def my_str_len(lst):
    return [len(string) for string in lst]
print("Preben, ida og Jonathan inneholder x antall bokstaver") 
print(my_str_len(["Preben" "ida", "Jonathan"]))


# Finner det største tallet i en liste
# Argumenter: nummer(list): Liste med tall
# Returns: Int: Det største tallet i listen

def my_max(nummer):
   Max = 0
   for item in nummer:
       if item > Max:
           Max=item
   return Max

List = [1,2,8,77,24,10]
tom_liste = []	
print("Høyeste tall")
print(my_max(List))



