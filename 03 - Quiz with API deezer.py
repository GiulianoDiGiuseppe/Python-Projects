import requests
import json
import random

def main():
    print("\n ----EXERCICE ----")

    DEEZER_SEARCH_ARTIST_API = 'https://api.deezer.com/artist/'

    # example of artist
    # we have in a file the name of artists and their ID, we take ID of artists
    # by file and request the page at deezer
    to_be_searched_artits = ["Elio e le storie tese", "Queen", "Eminem", "Al Bano", "Mina", "Ghali", "Muse", "The Beatles", "The Rolling Stones", "Micheal Jackson"]


    # but we randomize the chose of artists
    artists=[]

    #Create random IDs and make request for every ID
    IDs= random.sample(range(200),20)

    for i in IDs:
        r = requests.get(DEEZER_SEARCH_ARTIST_API + str(i)).json()
        artists.append({'name': r['name'] , 'id' : r['id'], 'nb_album' :r['nb_album'] ,'nb_fan':r['nb_fan'] })
        #print(r)

    # we randomize the choise of artists
    #[name1,name2] = random.sample(f_j, 2)

    stop='N'
    while(stop!='Y'):
        double_quest(artists)
        stop=input(" Do you want stop? Y or N:")

    print(" Bye Bye")

def double_quest(artists):
    idx1,idx2=random.sample(range(20), 2)
    name1=artists[idx1]['name']
    name2=artists[idx2]['name']
    album1=artists[idx1]['nb_album']
    album2=artists[idx2]['nb_album']
    fans1=artists[idx1]['nb_fan']
    fans2=artists[idx2]['nb_fan']


    answer=input("which has Band/songer write more albums ? write 1 for {} and 2 for {}:".format(name1,name2))
    if (str(answer)=='1' and  album1>album2) or (str(answer)=='2' and  album1<album2):
        print(" you win, {} have been pubblish {} while {} only {}".format(name1,album1,name2,album2))
    elif (str(answer)=='2' and  album1>album2) or (str(answer)=='1' and  album1<album2):
        print(" you lose, because {} have been pubblish {} while {} only {}".format(name2,album2,name1,album1))
    else:
        print("why do not you write 1 or 2?")


    answer=input("which has Band/songer more fans ? write 1 for {} and 2 for {}:".format(name1,name2))
    if (str(answer)=='1' and  fans1>fans2) or (str(answer)=='2' and  fans1<fans2):
        print(" you win , {} have been pubblish {} while {} only {}".format(name1,fans1,name2,fans2))
    elif (str(answer)=='2' and  fans1>fans2) or (str(answer)=='1' and  fans1<fans2):
        print(" you lose , because {} have been pubblish {} while {} only {}".format(name2,fans1,name2,fans2))
    else:
        print("why do not you write 1 or 2?")

if __name__ == "__main__":
    main()