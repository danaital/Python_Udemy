# Challenge 4
# menu = []
# menu.append(["egg", "spam", "bacon"])
# menu.append(["egg", "sausage", "bacon"])
# menu.append(["egg", "spam"])
# menu.append(["egg", "bacon", "spam"])
# menu.append(["egg", "bacon", "sausage", "spam"])
# menu.append(["spam", "bacon", "sausage", "spam"])
# menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
# menu.append(["spam", "egg", "sausage", "spam"])
#
# for meal in  menu:
#     if not "spam" in meal:
#         for ingredient in meal:
#             print(ingredient)
#
#
#


# Challenge 5
# list1 = ["egg", "sausage", "bacon", "milk", "cheese", "salami"]
# iterator = iter(list1)
# for i in range(0,len(list1)):
#     item = next(iterator)
#     print(item)
#
# Challenge 6
# o = range(0, 100, 4)
# print(o)
# p =ackNum, o[::5]
# print(p)
# r = o[::2]
# print(r)
# for i in p:
#     print(i)

# Challenge 7
imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling The Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    print('\t', song)
for song1 in tracks:
    songNum, songName = song1;
    print('\tTrack Number {}, Title: {}', songNum, songName)
for songNum, songName in tracks:
    print('\tTrack Number {}, Title: {}', songNum, songName)


