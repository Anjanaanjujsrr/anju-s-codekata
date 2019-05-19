TEXT=input()
WORD=0
for i in TEXT:
 if not( i.isalpha() or i.isdigit() or i==" "): 
    WORD=WORD+1

print(WORD)