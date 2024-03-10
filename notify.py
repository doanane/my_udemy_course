#creatin an app using which we can send notification to our windows system
from win10toast import ToastNotifier
import datetime

data = datetime.datetime.now()
data = str(data)

toast = ToastNotifier()
toast.show_toast("date-time", data,duration=3)

#practicing

# from win10toast import ToastNotifier
# import datetime

# data = datetime.datetime.now()
# data = str(data)

# Display multiple notifications with different messages
# toast = ToastNotifier()
# toast.show_toast("time alert app",data,duration=5)
# toast.show_toast("Notification 1", "time to eat ", duration=5)
# toast.show_toast("Notification 2", "time to bath", duration=5)
# toast.show_toast("Notification 3", "time to learn", duration=5)
# toast.show_toast("Title", "time to sleep", duration=5, threaded=False)

