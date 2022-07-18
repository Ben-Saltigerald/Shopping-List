visual_lst = ['1) apples', '2) bananas', '3) strawberries', '4) spinach', '5) broccoli', '6) sweet potatoes', '7) cucumber', '8) bread',
            '9) feta cheese', '10) eggs', '11) greek yogurt', '12) whole milk', '13) almond milk', '14) chicken', '15) rice',
            '16) nuts', '17) croutons', '18) granola']

appnd_lst = ['apples', 'bananas', 'strawberries', 'spinach', 'broccoli', 'sweet potatoes', 'cucumber', 'bread',
            'feta cheese', 'eggs', 'greek yogurt', 'whole milk', 'almond milk', 'chicken', 'rice',
            'nuts', 'croutons', 'granola']

items = []
quantity = []

for i in visual_lst:
    print(i)

def lst_appender():
    for x in appnd_lst:
        select = input("\n Type in the number of the item you wish to select: (Type stop if you are done) ")
        if select == "1": items.append(appnd_lst[0])
        elif select == "2": items.append(appnd_lst[1])
        elif select == "3": items.append(appnd_lst[2])
        elif select == "4": items.append(appnd_lst[3])
        elif select == "5": items.append(appnd_lst[4])
        elif select == "6": items.append(appnd_lst[5])
        elif select == "7": items.append(appnd_lst[6])
        elif select == "8": items.append(appnd_lst[7])
        elif select == "9": items.append(appnd_lst[8])
        elif select == "10": items.append(appnd_lst[9])
        elif select == "11": items.append(appnd_lst[10])
        elif select == "12": items.append(appnd_lst[11])
        elif select == "13": items.append(appnd_lst[12])
        elif select == "14": items.append(appnd_lst[13])
        elif select == "15": items.append(appnd_lst[14])
        elif select == "16": items.append(appnd_lst[15])
        elif select == "17": items.append(appnd_lst[16])
        elif select == "18": items.append(appnd_lst[17])
        else: break

def add_items():
    question = input('\n Are there any items not included on the list you would like to add? (Type Y or N) ')
    if question =='Y':
        add = input("\n Add an item to the list: (Type stop if you are done) ")
        items.append(add)
        while add != 'stop':
            add = input("\n Add an item to the list: (Type stop if you are done) ")
            items.append(add)


response = input("\n Are there any items that you need from this list? (Type Y or N) ")

for x in response:
     if response == 'Y':
          lst_appender()
          add_items()
     elif response == 'N':
         add_items()

print('\n')
if len(items) <= 1: print("\nyou did not select any items for your shopping list")

elif len(items) > 1:
    try: items.remove('stop')
    except: pass

    for i in items:
            print("\nSelect the quantity for the following item:")
            print(i)
            value = input()
            quantity.append(value)

final_list = dict(zip(items, quantity))

if len(final_list) >= 1:
    print('\nyour list contains the following items and their quantity: ')
    for key,value in final_list.items():
        print(key, ':', value)
