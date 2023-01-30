def is_cat_here(text):
    if 'cat' in text.lower():
        return True
    else:
        return False
print(is_cat_here('is Cat here'))


def is_item_here(text, *args):
    if 'item' in text.lower():
        return True
    else:
        return False
print(is_item_here('is item here'))


def is_item_here(item, *args):
    if item in args:
        return True
    else:
        return False
print(is_item_here('is item here'))

def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is ' + str(my_color) +
              ', but ' + kwargs['color'] + ' is also pretty good!')
    else:
        print('My favorite color is ' + str(my_color) +
              ', what is your favorite color?')


#def your_favorite_color( *kwargs):
#    if 'my_color' in kwargs:
#        print('My favorite color is {}, what is your favorite color?')
#your_favorite_color(bdfdf='fghf')