import datetime
laiks = datetime.datetime.now()
laiks.hour
0
if laiks.hour < 12:
     print("Labrīt")
elif 12 <= laiks.hour < 18:
     print("Labdien")
else:
     print("Labvakar")