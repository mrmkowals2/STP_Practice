list = ["The Walking Dead","Entourage","The Sopranos","The Vampire Diaries"]

for name in list:
    print(str(list.index(name)) + " - " + name)

'''
Better solution:

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for index, show in enumerate(shows):
    print(index)
    print(show)
'''
