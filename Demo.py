
#using System.Random as Random
import random

def get_days():
    #python has no arrays -- it has something similar to C# lists
    #var days = new list<string>(); is the equivalent C# expression of what is below
    days = []
    days = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat' 'sun']
    return days



def get_random_weather_report():
    weather = ['sunny', 'rainy', 'hot', 'lovely']
    report = weather[random.randint(0, len(weather) - 1)]
    return report

def main():
    days  = get_days()
    for d in days: #really the only for loop concept in python
        r = get_random_weather_report()
        print("weather on {0} is {1}".format(d, r))

    print("last r = " + r) #notice that r is defined within the for loop but has scope in the main method!


if __name__ == "__main__":
    main()

