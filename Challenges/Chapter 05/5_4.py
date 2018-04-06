michael = { 'height':'187cm',
            'favourite colour':'yellow',
            'favourite movie':'the matrix'}

user_input = input("Would you like to know Michael's height, favourite colour, or favourite movie? ")

if user_input.lower() in michael:
    print(michael[user_input.lower()])
else:
    print('Invalid input.')
            
