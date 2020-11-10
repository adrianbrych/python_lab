from xml.dom.minidom import parse
from xml.dom import minidom

doc=minidom.parse("newxmlfile.xml")

title1=doc.getElementsByTagName("name")[0]
title2=doc.getElementsByTagName("Films")[0]
print(title1.firstChild.data)

rooms = doc.getElementsByTagName("room")
for room in rooms:
        title = room.getElementsByTagName("title")[0]
        year = room.getElementsByTagName("year")[0]
        time=room.getElementsByTagName("time")[0]
        number=room.getElementsByTagName("number")[0]
        print(" Tytuł:",title.firstChild.data,"|Godzina rozpoczecia:",time.firstChild.data,"|Numer pokoju: ",number.firstChild.data,"|Rok produkcji:",year.firstChild.data)




new_title=doc.createElement("title")
new_title.appendChild(doc.createTextNode("Bond"))

new_time=doc.createElement("time")
new_time.appendChild(doc.createTextNode("16:10"))


new_year=doc.createElement("year")
new_year.appendChild(doc.createTextNode("1987"))


new_number=doc.createElement("number")
new_number.appendChild(doc.createTextNode("20"))




new_room=doc.createElement("room")
new_room.appendChild(new_title)
new_room.appendChild(new_year)
new_room.appendChild(new_time)
new_room.appendChild(new_number)
title2.appendChild(new_room)







doc.writexml(open("newxmlfile.xml","w"))

doc2=minidom.parse("newxmlfile.xml")
rooms2 = doc2.getElementsByTagName("room")

for room in rooms2:
        title = room.getElementsByTagName("title")[0]
        year = room.getElementsByTagName("year")[0]
        time=room.getElementsByTagName("time")[0]
        number=room.getElementsByTagName("number")[0]
        print(" Tytuł:",title.firstChild.data,"|Godzina rozpoczecia:",time.firstChild.data,"|Numer pokoju: ",number.firstChild.data,"|Rok produkcji:",year.firstChild.data)