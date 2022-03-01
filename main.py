from tkinter import *
from PIL import Image, ImageTk
import anagramfile
import searchfile
import palindromefile
import subfile
import binary
root = Tk()

root.title("Projectt")
image = ImageTk.PhotoImage(Image.open("stringg.png"))
image1 = Label(image=image)
image1.pack()


def open():

    top = Toplevel()
    l=Label(top,text="CLICK TO CHOOSE ANY ONE OF THE FOLLOWING STRING MANIPULATION METHODS",font=100,bg="blue",fg="white").pack(padx=20,pady=20)
    anagram = Button(top, text="ANAGRAMS", font=100, bg="#E3DFD7", padx=50, pady=20, command=anagrams)
    anagram.pack(padx=10,pady=10)

    palin = Button(top, text="PALINDROME", font=100, bg="#C1EDEF", padx=50, pady=20, command=palindrome)
    palin.pack(padx=10, pady=10)

    sub = Button(top, text="SUBSEQUENCE STRINGS", font=100, bg="#C9D2D1", padx=50, pady=20, command=subsequence)
    sub.pack(padx=10, pady=10)

    pattern = Button(top, text="PATTERN SEARCHING", bg="#958D85", font=100, padx=50, pady=20, command=patterns)
    pattern.pack(padx=10, pady=10)

    binary = Button(top, text="BINARY SEARCH", bg="#24f3f0", font=100, padx=50, pady=20, command=binaryy)
    binary.pack(padx=10, pady=10)

    def help():
        top=Toplevel()
        mylabel = Label(top, text ="\n \nHere manipulation of strings is done using various operations.\n \n \n "
                                   "An anagram is a word that is produced by rearranging the letters of the word "
                                   "itself. "
                                   "\nLet's take a look at the word ELBOW. We can say that BELOW is anagram of ELBOW,"
                                   "\n "
                                   "since BELOW uses all the original letters of ELBOW exactly once. "
                                   
                                   "\nNot only from one word, an anagram can also be created from, and can create, "
                                   "two or more words: "
                                   "\nSCHOOL MASTER is an anagram of THE CLASSROOM, or FOURTH OF "
                                   "JULY is an anagram of JOYFUL FOURTH. "
                                   "\n \n \n A palindrome is a string, or sequence of characters, that has the exact "
                                   "same spelling both forward and backward. "
                                   "\n NOON, MADAM, RADAR, and ROTATOR are some examples of the palindrome."
                                   "\nSimilar to the anagram, we can also construct a palindrome from more than one "
                                   "word; for instance, A NUT FOR A JAR OF TUNA, or NO LEMON NO MELON. "
                                   "\n \n \n Subsequence string is a string derived from another string by deleting "
                                   "some characters without changing the order of the remaining characters. "
                                   "\n \n \n Pattern searching uses KMP Search Algorithm to find out the location of "
                                   "a string "
                                   "in another string.", font = 20)
        mylabel.pack()
    help = Button(top, text="HELP", bg= "#DED4D8", font=100, padx=50, pady=20, command=help)
    help.pack(padx=10, pady=10)



def anagrams():
    top = Toplevel()
    label = Label(top, text="ENTER FIRST STRING", font=25).pack()
    entries = [Entry(top,width=100,borderwidth=5,font=('Arial', 20)) for _ in range(2)]
    for entry in entries:
        if (entry == entries[1]):
            label = Label(top, text="ENTER SECOND STRING",font = 20).pack()
        entry.pack(padx=10, pady=10)


    submmit = Button(top, text="CLICK TO SUBMIT", font=100, bg="#E3DFD7", padx=50, pady=20, command=lambda:click(entries)).pack()

    def click(enteries):

        l1 = enteries[0].get()
        l2 = enteries[1].get()
        Text = ""
        isAnagram = anagramfile.anagramCode(l1, l2)
        if isAnagram:
            Text = "THE GIVEN STRINGS ARE ANAGRAM."
        else:
            Text = "THE GIVEN STRINGS ARE NOT ANAGRAM."
        label = Label(top, text=Text, font =20)
        label.pack()

        def delete():
            enteries[0].delete(0, END)
            enteries[0].insert(0, "")
            enteries[1].delete(0, END)
            enteries[1].insert(0, "")
            label.destroy()
            mybutton.destroy()



        mybutton = Button(top,width=20, text="CLEAR",font=20, command=delete)

        mybutton.pack(pady=10,padx=10)


def patterns():
    def click(enteries):
        text=enteries[0].get()
        pattern=enteries[1].get()
        output=searchfile.KMPSearch(pattern,text)
        textWidg = Text(top)
        if len(output) == 0:
            textWidg.insert(INSERT, "NO MATCH FOUND")
            textWidg.pack()
        else:
            textWidg.insert(INSERT,text)
            textWidg.pack()
            for label in output:
                i=0
                textWidg.tag_add(str(i),"1."+str(label),"1."+str(label+len(pattern)))
                i=i+1
            for label in output:
                i=0
                textWidg.tag_config(str(i), background="black", foreground="green")
                i=i+1
        mybutton = Button(top, text="Clear",font=20, command=lambda:delete(mybutton))
        mybutton.pack(padx=10,pady=10)
        def delete(mybutton):
            enteries[0].delete(0,END)
            enteries[0].insert(0,"")
            enteries[1].delete(0, END)
            enteries[1].insert(0, "")
            textWidg.destroy()
            mybutton.destroy()

    top=Toplevel()
    entries = [Entry(top,width=100,font=('Arial', 20)) for _ in range(2)]
    for entry in entries:
        entry.pack(pady=20,padx=20)
    submmit = Button(top, text="CLICK TO SUBMIT", font=100, bg="#E3DFD7", padx=50, pady=20,command=lambda: click(entries)).pack(pady=20)


def palindrome():
    top=Toplevel()
    text=Label(top,text="ENTER THE INPUT STRING: ", font=20).pack()
    enteries=Entry(top,font=('Arial', 12),width=50)
    enteries.pack(padx=20,pady=20)
    submit = Button(top, text="CLICK TO SUBMIT", font=100, bg="#E3DFD7", padx=50, pady=20,command=lambda: click(enteries)).pack()
    def click(entery):
        text=entery.get()
        print(text)
        isPalindrome = palindromefile.checkPalindrome(text)
        output=""
        if isPalindrome:
            output="The input string is palindrome"
        else:
            output="The input string is not palindrome"
        label = Label(top, text=output,font=20)
        label.pack()

        def delete():
            enteries.delete(0, END)
            enteries.insert(0, "")
            label.destroy()
            mybutton.destroy()



        mybutton = Button(top, width=20,text="CLEAR",font=20, command=delete)

        mybutton.pack(pady=10,padx=10)


def subsequence():
    top = Toplevel()
    text = Label(top, text="ENTER THE INPUT STRING: ", font=20).pack()
    enteries = Entry(top,width=50,font=('Arial', 20))
    enteries.pack(padx=20, pady=20)
    submit = Button(top, text="CLICK TO SUBMIT", font=100, bg="#E3DFD7", padx=50, pady=20, command=lambda: click(enteries)).pack()

    def click(entery):

        text = entery.get()
        print(text)
        sub = subfile.generatesub(text)
        output = ""
        label = Label(top, text=sub,font =20)
        label.pack()
        def delete():
            enteries.delete(0, END)
            enteries.insert(0, "")

            label.destroy()
            mybutton.destroy()



        mybutton = Button(top,width=20 ,text="CLEAR",font=20, command=delete)

        mybutton.pack(pady=20,padx=20)


def binaryy():
    top = Toplevel()
    label = Label(top, text="ENTER PATH OF FILE",font = 25).pack()
    entries = [Entry(top, width=100, borderwidth=5) for _ in range(2)]
    for entry in entries:
        if (entry == entries[1]):
            label = Label(top, text="ENTER THE STRING",font = 20).pack()
        entry.pack(padx=10, pady=10)

    #print(entries)
    submit = Button(top, text="CLICK TO SUBMIT", font=100, bg="#E3DFD7", padx=50, pady=20,
                    command=lambda: click(entries))
    submit.pack()
    def click(entries):
        path = entries[0].get()
        searchtxt = entries[1].get()
        Text = ""
        link = binary.file(path)
        label1 = Label(top,text = link)
        label1.pack()
        isPresent = binary.binarySearch(link,0,len(link)-1,searchtxt)
        if isPresent:
            Text = "THE GIVEN STRING IS PRESENT."
        else:
            Text = "THE GIVEN STRING IS NOT PRESENT."
        label = Label(top, text=Text, font =20)
        label.pack()

        def delete():
            entries[0].delete(0, END)
            #enteries[0].insert(0, "")
            entries[1].delete(0, END)
            #enteries[1].insert(0, "")
            label.destroy()
            label1.destroy()
            mybutton.destroy()



        mybutton = Button(top,width=20, text="CLEAR",font=20, command=delete)

        mybutton.pack(pady=10,padx=10)


btn = Button(root, text="PRESS TO CONTINUE...",font =100,activebackground="#00ffff",bg="#95A1AB", padx=50, pady= 50,  command=open).pack()
root.mainloop()