import os

lista=["się","i","oraz","nigdy","dlaczego"]


file=open("Artykuł.txt",'r')

text=file.read()

file.close()

text_to_save=text.replace(" dlaczego"," ")
text_to_save=text_to_save.replace(" się"," ")
text_to_save=text_to_save.replace(" i"," ")
text_to_save=text_to_save.replace(" oraz"," ")
text_to_save=text_to_save.replace(" nigdy"," ")



file=open("Artykuł.txt",'w')
file.write(text_to_save)












