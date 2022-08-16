print('Welcome to the movies!')

child_tix_price = 7.25
adult_tix_price = 11.50
tax_rate = .075


choice = "y"
# while loop starts here: menu system
# only continue while choice == 'y'
while choice == "y": # boolean expression evaluated to T or F
    print('Movie List:') # tab key interpreted as 4 spaces
    print('1 - Star Wars')
    print('2 - Top Gun Maverick')
    print('3 - Megamind')

    # snake_case, camelCase, PascalCase
    movie_choice = int(input('Which movie do you want to see? '))
    adult_tix = int(input('How many adult tickets would you like to purchase? '))
    child_tix = int(input('How many child tickets would you like to purchase? '))

    # total price = (adult tix * adult price + child tix * child price) * (1 + tax rate)
    total_price = ((adult_tix * adult_tix_price) + (child_tix * child_tix_price)) * (1 + tax_rate)
    # total_price_str = str(total_price)
    print('Thanks for your purchase! Your total is: $' + "{:.2f}".format(total_price))
    choice = input('Do you want more tickets? ')

# same as -> print(f"Thanks for your purchase! Your total is: {total_price}")
# end of while loop

print('Bye')