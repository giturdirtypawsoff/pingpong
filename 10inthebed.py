def ten_in_the_bed(count):
    if count > 1:
        print(f'There were {count} in the bed\n And the little one said,\n "Roll over! Roll over!"\n So they all rolled over and\n One fell out.\n')
        return ten_in_the_bed(count - 1)
    elif count == 2:
        print(f'There were {count} in the bed\n And the little one said,\n "Roll over! Roll over!"\n So they all rolled over and\n One fell out')
        return ten_in_the_bed(count - 1)
    else:
        print('\nThere was 1 in the bed\n And the little one said,\n "Alone at last!"\n "Good Night!" \n')
        choice = input('Do you want to wake up the last one in the bed? [yes/no]: ')
        def wake_up_decision(decision):
            if decision == "yes" or decision == "y":
                print('\nThat isnt a very nice thing to do!')
            else:
                print('\n Ahhh, lets leave them to sleep')
        return wake_up_decision(choice)

ten_in_the_bed(10)
