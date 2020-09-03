
"""
colors = ["red","orange", "green", "blue"]
sentence = "My Jacket is black"

Functions:

some functions: abs() sorted() sort() range() reversed() list() remove("item")

new = "This is a long sentence".split(" ")
print(new)


a_string = "apples, oranges, bananas"
new = a_string.find("a")
print(new)

Important: bei a_list = b_list , werden bei der Änderung einer Variable beide geänder.
Ändere ich bei a_List etwas, wird b_List ebenso geändert!
Lösung: kopiere den String: c_list = a_list.copy()

a_string = "Hello {0} and welcome to {1}".format("Robin", "python")
print(a_string)


def greet(name):
    print("Hello" +name)    
#greet(" Lukas")


def greet2(name):
    print("Hello, {0}".format(name))
#greet2("Lukas")

def product(numbers):
    p = 1
    for n in numbers:
        p *= n
    print(p)
    return p
    
#product([1,2,3,4,5,6,7,8,9,10])

def combine_and_sort(first, second):
    return sorted((first+second))

#print(combine_and_sort([4,8],[1,5,8,14]))

"""
# igpay: take a word and return the pig latin version, "pig" -> "igpay"
# "apple" -> "aplleway"
# Exercise1 :
"""
def übung(liste):

    if (liste[0] == "a") or (liste[0] == "e") or (liste[0] == "u") or (liste[0] == "o") or (liste[0] == "i"):
        
        print(liste + "way")
    else:
        print(liste[1:] + liste[0] + "ay")
                    
übung("apple")
"""
#Exercise2:
#fuction called numerous: take roman numerals and output arabic numbers
#zB "XiV" -> 14 oder "mmxlix" -> 2049

"""
def numerous(i):

    # deklaraton der initialen Variablen
    # input nimmt den eingegebenen Wert entgegen und wandelt ihn in eine Liste um
    # diese wird dann umgedreht da man so die arabische Zahl errechnen kann
    # alt speichert die letzte berechnete Arabische Zahl um zu prüfen ob die aktuelle größer oder kleiner ist

    input = list(i)
    input.reverse()
    alt = 0
    
    # Speicherung der römischen und arabischen Zahlen in Listen

    roman = ["i","v","x","l","c","m"]
    roman_numbers = [1, 5, 10, 50, 100, 1000]
    
    # in dieser for schleife werden die eingegebenene "Zahlen" (in umgekehrter Reihenfolge) 
    # nacheinander entweder Subtrahiert oder Addiert.

    for n in range(0, len(input)):

        index_r = input[n]
        index_rn = roman.index(input[n])
        zahl = roman_numbers[index_rn]
        
        if alt == 0:
            ergebnis = zahl
            alt = zahl
        else:
            
            if zahl < alt:
                ergebnis -= zahl
                alt = zahl
            else:
                ergebnis += zahl
                alt = zahl

    print(ergebnis)

numerous("mmxlix")

----------------------------------------------------------------------------------

new Datatype: None (like true or false)
- none leads to false
- if my_data is None: ... / if my_data is not None


dict/dictionary:
- keys to look up data
- cats = {}
- cats["Robin"] = 5 -> reuslt: {'Robin': 5}
- Robin is the Key and 5 is the Value
- Keys are paired with the Values
- other languages call this map or hashmap
- care for different writing of Keys
- u can use cats.get("Robin")
- "Robin" in cats -> true
- iterate over it: for name in cats: ... do something
- remove item: del cats["robin"] / cats.pop("robin")
- countries.items() gives the Key Value
- dictionary:    weather = {"Rainy": "rain.png", "Cloudy": "clouds.png"}
- 

def to_val(letter):
    test = {"i": "1", "v": "5", "x": "10", "l": "50", "c": "100", "m": "1000"}
    print(test[letter])

to_val("l")

------------------------------------------------------------
Chapter 2.8
------------------------------------------------------------

- threat String as Bytes: greeting = b"Hello World!"
- tuple instead of list: when data should not be modified , performance is better
                 fruits = ("Apple", "Orange")
- Tupels: (), Lists: [], Sets: with curly Brackets {}
- frozenset : a set you cant modify
- for (f,v) in zip(fruits, vegetables): print:(f,v)
        zip pairs up items from the two iterables
- 

------------------------------------------------------------
Chapter 2.9
------------------------------------------------------------
- User input: input() , name = input(), name = input("Enter your name: ")
- check valid input: if not num_inp.isdigit()
- Exception Handling:

    try:
        inp = input("Enter a number: ")
        inp_int = int(inp)
    except ValueError:
        inp_int = None
        print("That's not a numer i know about!")
    except NameError as e:
        print("Something went wrong with my Code")
        print(e)
        raise e
    except:
        print("I have no idea what went wrong")
        raise
    else:
        print("Somehow, everything went according to plan")
    finally:
            print("All done!")

- finally block: runs after either the code runs successfully or an exeption is raised
    under last Code:
        finally:
            print("All done!")

- else runs if no exception is raised
- finaly runs everytime (finally and else aren't used very often)

------------------------------------------------------------
READING FILES:

- with open("recipe.txt") as input_file:
    recipe = input_file.read()
    print(recipe)

- strip function on a string removes the extra new line at the end as well as any extra spaces if there were any
    word = xyphsdkjh\n"
    print(word) results in: xyphsdkjh mit Absatz
    print(word.strip()) results in: xyphsdkjh ohne Absatz
    Beispiel: "  How are you   " results in "how are you"

WRITING FILES:

with open('scrable.txt', 'w') as output_file:       // w for write, a for append
    for word in words:
        output_file.write(word + "\n")cat

- with binary files, add a rb when open a file:     // add wb when writing a file
    with open('guru-portfolio.zip', 'rb') as input_file:
            data = input_file.read()

EXERCISES:

def petauswahl():
        pets = {'bird':3.5, 'cat':5.0, 'dog':7.25, 'gerbil':1.5,}

        try:
            inp = input("Which pet u want to buy? : ")
            Price = str(pets[inp])
            print("The Price of the pet is: "+Price)
            
        except KeyError:
            print("This pet is not available, please choose another one: ")
            petauswahl()
        except:
            print("I have no idea what went wrong")
        
petauswahl()

------------------------------------------------------------
Chapter 2.10 Import and  the Standard Library
------------------------------------------------------------

- import math , random
- from random import shuffel   (use shuffel function directly)
- import itertools as iter     (rename Module)
- iter.chain  (zusammenfügen von Liste),    iter.combinations()    (Kombinationen von 2 Listen erstellen)
- import datetime ... etc etc -> see Library
- ZIP Files:    import gzip, bzip, zipfile

        ZIP File:   from zipfile import ZipFile
                    with ZipFile('files.zip') as files:
                    print(files.namelist())
                    files.exractall()

------------------------------------------------------------
Chapter 2.11 More of the Standard Library
------------------------------------------------------------

- import csv    read and write csv files
        with open('users.csv', 'w') as csvfile:
            write = csv.writer(csvfile)
            write.writerow(['id', 'email', 'name'])
            write.writerow([5, 'testqexample.com', 'robin norwood'])
            ... ...

- import os   //Details of operating system
    os.getenv('USER')
    os.path.abspath('.')

- import sys  //infos about system
    sys.argv
    sys.platform
    sys.version

- import re   //regular expression - see if parts of a string match the given pattern
    if re.search('tang', 'tangerines'): print("tang is in tangerines")
    if re.search('.ang', 'dangeries'): print("matched!")
    angs = re.search('(.ang)', 'dangeries')
        angs.groups()   results in: ('dang',)
    vowels_re = '[aeiou]'
        re.findall(vowels_re, 'dangeries')    results in: ['a', 'e', 'i', 'e']
    
        
------------------------------------------------------------
Chapter 2.12 Snakes and Meteors 1: Pip, PyPi, and Requests
------------------------------------------------------------
- Python package index: pypi.python.org
- import requests  //can request stuff from http websites - http request
- cmd: 'pip3 install requests'

    meteor_resp = requests.get('http://nasa.gov......json') //get data as json data
    meteor_data = meteor_resp.json()
        for meteor in meteor_data: print(type(meteor))




"""
import math

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

import requests
# holt die Daten von der Website
resp = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
# speichern unserer Position
my_loc = (51.767121, 8.709493)

#print(resp.status_code)
#print(resp.json())

# Formt die Daten ins json Format um
meteor_data = resp.json()

# geht durch das Dictionary und fügt die berechnete Distanz zu unserem Standort hinzu
for meteor in meteor_data:
    if not ('reklat' in meteor and 'reclong' in meteor): continue
    meteor['distance'] = calc_dist(float(meteor['reclat']), float(meteor['reclong']), my_loc[0], my_loc[1])

# gibt die distanz zurück
def get_dist(meteor):
    return meteor.get('distance', math.inf)

# sortiere Liste nach den Entfernungen
meteor_data.sort(key=get_dist)

print(meteor_data[0]) 

#for meteor in meteor_data: print(type(meteor))




