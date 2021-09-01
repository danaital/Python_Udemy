# import webbrowser
# #webbrowser.open("https://www.idc.ac.il/he/pages/home.aspx")
# #webbrowser.open("https://www.udemy.com")
# help(webbrowser)
#
#
# challenge 12
# with open("C:\\Users\\Ophir Danai\\Downloads\\lecture-77-challenge.txt") as file1:
#     lines = file1.readlines()
#     for line in lines:
#         print(line,end="")
#
# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.
# import time
# print("time():"+"\t"*4,time.get_clock_info('time'))
# print("perf_counter:"+"\t"*2,time.get_clock_info('perf_counter'))
# print("monotonic()"+"\t"*3,time.get_clock_info('monotonic'))
# print("process_time():"+"\t"*2,time.get_clock_info('process_time'))
#

# import time
# import datetime
# print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
#
# print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
# print()
# if time.daylight != 0:
#     print("\tDaylight Saving Time (DST) is defined for this location")
#     print("\tThe DST timezone name is " + time.tzname[1])
#
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("UTC is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
# import datetime
#
# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())
import pytz
# for x in sorted(pytz.country_names):

#     print("{}: {}".format(x, pytz.country_names[x]), end=': ')
#     if x in pytz.country_timezones:
#         for zone in sorted(pytz.country_timezones[x]):
#             tz_to_display = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz=tz_to_display)
#             print("\t\t{}: {}".format(zone, local_time))
#     else:
#         print("\t\tNo time zone defined")
#
#
#
#
#
#
#
#
#
#
#
# #webbrowser.open("http://www.ofran.co.il")
import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Test")
mainWindow.geometry('640x480-4+10')
mainWindow.mainloop()

