#import module
from tkinter import *

# initialize window
root = Tk()
root.geometry('300x300')
root.title('Bina Cerita')
Label(root, text= 'Mad Story!' , font = 'arial 20 bold').pack()
Label(root, text = 'Pilih cerita :', font = 'arial 15 bold').place(x=40, y=80)


################Stories##############


def madlib1 ():
   
    adjactive = input('masukkan kata sifat : ')
    color = input('masukkan warna : ')
    thing = input('masukkan nama benda :')
    place = input('masukkan nama tempat : ')
    person= input('masukkan nama orang : ')
    adjactive1 = input('masukkan kata sifat : ')
    insect= input('masukkan nama serangga : ')
    food = input('masukkan nama makanan : ')
    verb = input('masukkan kata kerja : ')

    print('Malam tadi saya bermimpi saya ' +adjactive+ ' rama-rama dengan ' + color+ ' yang kelihatan seperti '+thing+ ' .Saya terbang ke ' + place+ ' bersama sahabat baik saya iaitu '+person+ ' yang merupakan '+adjactive1+ ' ' +insect +' .Kami makan ' +food+ ' apabila kami sampai, kami membuat keputusan untuk '+verb+ ' dan mimpi itu berkhir selepas saya berkata jom ' +verb+ '.')


def madlib2 ():
    person = input('masukkan nama: ')
    color = input('masukkan warna : ')
    foods = input('masukkan nama makanan : ')
    adjective = input('masukkan kata sifat : ')
    thing = input('masukkan nama benda : ')
    place = input('masukkan nama tempat : ')
   
    food = input('masukkan nama makanan: ')
    

   
    print('Hari ini, kami memetik durian di kebun ' +person+ '. Terdapat pelbagai jenis buah durian di kebun itu. Saya makan isi durian berwarna ' +color+ ' yang rasanya seperti '+foods+ '.\n Selepas itu terdapat durian '+adjective+ ' seperti ' + thing + '.Apabila raga kami sudah penuh, kami berjalan-jalan ke '+place+ ' dan balik. kami tak sabar untuk buat '+food+ '!')  



######buttons   
Button(root, text= 'Seekor Rama-rama', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'Durian Oh Durian', font ='arial 15', command = madlib2 , bg = 'ghost white').place(x=70, y=180)


root.mainloop()

    



