# import pyautogui
# import time
# import tkinter as tk

# def screenshot():
#     time.sleep(5)
#     img = pyautogui.screenshot()
#     img.save("test5.png")
#     img.show()

# root = tk.Tk()  # Corrected capitalization of 'Tk'
# frame = tk.Frame(root)
# frame.pack()

# button = tk.Button(frame, text="take screenshot", command=screenshot)
# button.pack(side=tk.LEFT)

# close = tk.Button(frame, text="quit", command=root.destroy)  # Changed 'quit' to 'root.destroy'
# close.pack(side=tk.LEFT)

# root.mainloop()





# import tkinter as tk
# import pyautogui
# import time
# import tkinter as tk


# def screenshot():
#     time.sleep(5)
#     img = pyautogui.screenshot()
#     img.save("test5.png")
#     img.show()
# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()

# button = tk.Button(frame,text ="take  screenshot",command=screenshot)
# button.pack(side=tk.LEFT)

# close = tk.Button(frame,text ="quit",command=quit)
# close.pack(side=tk.LEFT)

# root.mainloop()


# class App(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()

# # create the application
# myapp = App()

# #
# # here are method calls to the window manager class
# #
# myapp.master.title("My Do-Nothing Application")
# myapp.master.maxsize(1000, 400)

# # start the program
# myapp.mainloop()




import pyautogui
import time
import tkinter as tk
def screenshot():
    time.sleep(5)
    img = pyautogui.screenshot()
    img.save("nana akua")
    img.show()
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="tap sreenshot",command= screenshot)
button.pack(side=tk.LEFT)

close = tk.Button(frame, text="quit",command= quit)
close.pack(side=tk.LEFT)
# i run this code for about 70 times not knowing the  mistake in the code was writing test instead of text.
    
root.mainloop()
    