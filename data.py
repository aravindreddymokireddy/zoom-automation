import time
import datetime

timetable={
    1:['AI','LP','ADB'],
    2:['LP','AI','IOT'],
    3:['DMDW','AI','LP'],
    4:['DMDW','IOT','SC'],
    5:['SS','DMDW','IOT'],
    6:['SC','SS','ADB']
}

zoomlinks={
    'ADB' : '',
    'LP'  : 'https://iare-ac-in.zoom.us/w/98425928051?tk=lHeR50ZdwIx09_Udp2EP6WLg7AaPCy7eJ5ZxGSJU6I4.DQIAAAAW6qR5cxZ0RmVnZ3Vib1EzYVNIRDhfOFdEWjhRAAAAAAAAAAAAAAAAAAAAAAAAAAAA&pwd=OFl4Qk1rVzBQZnZMNnRZTTJLeG0rQT09',
    'IOT' : 'https://iare-ac-in.zoom.us/w/95945210804?tk=lWwtxTqmy1oWiXDkq3GmbENhRZtTIXIc8QMgGnz0hVM.DQIAAAAWVse7tBZOMkpsZHV5TlJHdVZ0Qkd6aktDTkh3AAAAAAAAAAAAAAAAAAAAAAAAAAAA&pwd=TjJhVFJ2NFprVzRnWElKeVh0aktPQT09',
    'DMDW': 'https://iare-ac-in.zoom.us/w/96924410873?tk=HLGv3pQM0bBF_vhnQnR2yry9kbhGKV3eXLm5lyiKcxU.DQIAAAAWkSUj-RZJRDJ1ZlFiMFFuLTdfSlNBUzRFYmNRAAAAAAAAAAAAAAAAAAAAAAAAAAAA&pwd=QmF2a2xWSXAyWjFtUFhvaVYyUUR0UT09',
    'SC'  : 'https://iare-ac-in.zoom.us/w/99029418973?tk=KOBufO65sM74u0SzT4Rg8FRRjpJ8xwzsYYho74DRxwA.DQIAAAAXDp0D3RZKUllnSVRGN1NQcUpFMnR3Zk5zMmd3AAAAAAAAAAAAAAAAAAAAAAAAAAAA&pwd=dHo5YWxYNXVjS1pXcmY2RFVadVZOUT09',
    'SS'  : 'https://iare-ac-in.zoom.us/w/95189208348?tk=y4B2WqaFrrghJCVOOwDxZs7MiTzehN0IG6DZq9-uB_Y.DQIAAAAWKbgNHBZyUndlS2QzWlFfU1FENzhXWmM0eV9nAAAAAAAAAAAAAAAAAAAAAAAAAAAA&pwd=Vi9sUXlIVFNkVnBIcEYxV21FeXdZdz09',
    'AI'  : 'https://iare-ac-in.zoom.us/w/92836158713?tk=EseZX0zTzxambNb7vZfQ4l6ObVD05fNKn8_6tzKN2AE.DQIAAAAVnXdc-RZGNjBGRUw0a1RCZUlvbWdUNzBXN0F3AAAAAAAAAAAAAAAAAAAAAAAAAAAA&pwd=NnZTZkVremRvd0pLUGNpdTZqZ1M1UT09',
}

x = datetime.datetime.now()

day=int(x.strftime("%w"))
hour=int(x.strftime("%I"))-1


lst=[
    [zoomlinks[timetable[day][hour]], "13:30", "14:19"],
    [zoomlinks[timetable[day][hour]], "14:20", "15:09"],
    [zoomlinks[timetable[day][hour]], "15:10", "16:00"]
]
# print(hour)
# print(day)
# print(zoomlinks[timetable[day][hour]])