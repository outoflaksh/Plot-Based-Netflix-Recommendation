from main import recommendations
import pandas as pd


dataset = pd.read_csv('./dataset/netflix_titles.csv')

while True:
    target = input("Enter movies/tv-show you want similar stuff for!: ")
    print("\n")
    recom = recommendations(target)
    if type(recom) == str:
        print(recom)
    else:
        for index, title in recom:
            print(title + " (" + dataset.loc[index]['type'] + ")")
            print(dataset.loc[index]['description'])
            print('\n')

    ch = input("\nMore?: ")
    if ch == 'n':
        break