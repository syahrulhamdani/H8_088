"Module about naming."


TEXT = "Hacktiv8 - Intro Python for Data Science"


def show_names(names):
    print("function from hacktivate")
    for name in names:
        print(name)


def combine_names(names, sep=", "):
    print("function from hacktivate")
    combination = sep.join(names)
    return combination