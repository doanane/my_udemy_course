# import wikipedia
# query = input("Enter your prefered topic :\n")

# result= wikipedia.summary(query)
# print(result)











# wiki 2.py
# creating a UI for wikipedia search app,
# therefore we create a text field where we can enter the name of the topic and will be adding a search button

from tkinter import *
import wikipedia

#from tkinter import *: Imports all symbols from the tkinter module,
# which is used for creating GUI applications.

#import wikipedia: Imports the wikipedia module,which provides a
# convenient interface to access Wikipedia content.

def on_press():
    q =get_q.get()
    text.insert(INSERT,wikipedia.summary(q))
    
#on_press(): This function is called when the "Search" button is pressed.
# It retrieves the user's query from the entry widget (get_q), 
# attempts to fetch a summary from Wikipedia using the wikipedia.summary method, 
# and inserts the result into the text widget (text). It also handles potential errors
# such as DisambiguationError (multiple search results) and PageError (no matching page).

    
root = Tk()
root.title("WIKI Search App")
#`root`:this represents the main Tkinter windows,
#Tk() initializes a new window and `root title` sets the title of the window.
question = Label(root, text='Quest')
question.pack()
get_q = Entry(root,bd=5)
get_q.pack()
#get_q: This variable represents an entry widget, which allows the user to input text. The bd parameter sets the border size,
# and the widget is added to the window using pack()

submit =Button(root, text="Search", command=on_press)
submit.pack()
text= Text(root)
text.pack()
# text: This variable represents a text widget, which is used to display text.
# It is added to the window using pack().
root.mainloop()
#root.mainloop(): This method starts the Tkinter event loop, which handles user interactions 
# and keeps the GUI running until the user closes the window.


    
    
    
# # ANOTHER WAY TO CREATE THE APP FOR SEARCHING
# from tkinter import *
# import wikipedia

# def on_press():
#     query  = get_q.get()
#     try:
#         result = wikipedia.summary(query)
#         text.insert(INSERT, result)
#     except wikipedia.exceptions.DisambiguationError as e:
#         text.insert(INSERT, f"DisambiguationError: {e.options}\n")
#     except wikipedia.exceptions.PageError:
#         text.insert(INSERT, "Page not found.\n")

# root = Tk()
# root.title("WIKI Search App")

# question_label = Label(root, text='Enter your query:')
# question_label.pack()

# get_q = Entry(root, bd=5)
# get_q.pack()

# search_button = Button(root, text='Search', command=on_press)
# search_button.pack()

# text = Text(root)
# text.pack()

# root.mainloop()












# import wikipedia
# from tkinter import *
# import time
# def on_press():
#     q = get_q.get()
#     text.insert(INSERT,wikipedia.summary(q))
#     time.sleep(5)
# root = Tk()
# root.title("ask app")

# question= Label(root,text="Question")
# question.pack
# get_q =Entry(root,bd=2)
# get_q.pack()

# submit = Button(root,text="SEARCH",command=on_press)
# submit.pack()

# text = Text(root)
# text.pack()

# root.mainloop()











