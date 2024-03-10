import yagmail
reciever = 'doanane@st.ug.edu.gh'
message = 'email automation'

sender = yagmail.SMTP("georginafokou@gmail.com")
password = input('bwzl owtr qnvh ootp')
sender.send(to= 'donane@st.ug.edu.gh',subject='this is a lecture from one of my udemy courses',contents=message)
# # # to parameter helps holds the reciever email id value
# # # subject parameter helps to send subject of email
# # # content parameter is used to pass the message


# import yagmail # the library that we are working with

# # all the necessary login information here 
# user = 'georginafokou@gmail.com' # your email goes here
# password = 'bwzl owtr qnvh ootp' # the password we just generated goes here 
# to = 'oou37773@nezid.com' # the user you're sending an email to goes here 

# # content information here 
# subject = 'hello desmond'
# contents = 'hi'

# try:
#     yag = yagmail.SMTP('georginafokou@gmail.com', 'bwzl owtr qnvh ootp')
#     yag.send('oou37773@nezid.com', 'hello desmond', 'hi')
#     print('Your email was sent successfully')
# except:
#     print('mail sent')