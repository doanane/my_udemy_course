# import pyautogui
# import time

# def screenshot():
#     time.sleep(5)
#     img = pyautogui.screenshot()
#     img.save("test2.png")
#     img.show()
# screenshot()


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


import pyautogui
import time 
import tkinter as tk


def screenshot():
    img = pyautogui.screenshot()
   # time.sleep(5)
    img.save("sam.png")
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="take screenshot",command=screenshot)
button.pack(side=tk.LEFT)

close = tk.Button(frame, text="quit",command=quit)
close.pack(side=tk.LEFT)

root.mainloop()


# from unicodedata import name
# import pyautogui
# import time

# def screenshot():
# #    name= time.time()
#     name = 'C:/Users/anane/OneDrive/Desktop/UDEMY PYTHON/{}.png'.format(name)
#     img= pyautogui.screenshot()
#     img.save(name)
#     img.show()
# screenshot()