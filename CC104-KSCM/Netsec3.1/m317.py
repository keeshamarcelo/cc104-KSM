def go_for_a_walk():
    print("Going for a walk")


def go_to_the_theater():
    print("Going to the theater")


def go_for_lunch():
    print("Going for lunch")


def play_chess_at_home():
    print("Playing chess at home")


the_weather_is_good = True
tickets_are_available = False
table_is_available = False

if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

