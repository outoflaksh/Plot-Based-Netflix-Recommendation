from main import recommendations
from datasets import DATASET_FULL

while True:
    target = input("Enter movies/tv-show you want similar stuff for!: ")
    print("\n")
    recom = recommendations(target)

    if type(recom) == str:
        print(recom)
    else:
        for index, title in recom:
            print(title + " (" + DATASET_FULL.loc[index]['type'] + ")")
            print(DATASET_FULL.loc[index]['description'])
            print('\n')

    ch = input("\nMore?: ")
    if ch == 'n':
        break