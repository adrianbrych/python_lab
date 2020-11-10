import os

file=open("Artykuł.txt",'r')

text=file.read()

file.close()


slownik={'i':' oraz','oraz':' i','nigdy':' prawie nigdy','dlaczego':' czemu' }

text_to_save=text.replace(" i",slownik['i'])
text_to_save=text_to_save.replace(" oraz",slownik['oraz'])
text_to_save=text_to_save.replace(" nigdy",slownik['nigdy'])
text_to_save=text_to_save.replace(" dlaczego",slownik['dlaczego'])




file=open("Artykuł.txt","w")

file.write(text_to_save)
file.close()