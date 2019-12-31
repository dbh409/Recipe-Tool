from time import sleep

import random
import numpy as np
import DB_Util as db

meals = ['meatballs', 'meatloaf', 'tuna casserole',
   'lumberjack casserole', 'scalloped potatoes', 'egg salad',
   'mushroom potato soup', 'something fancy', 'chicken bake',
   'goulash (sp?)', 'fajitas', 'hamburgers',
   'hotdogs', 'grilled pork', 'pork tenderloin (schlemertopf)',
   'ham & broccolli alfredo', 'Aldi pizza', 'mushroom tacos',
   'shepherd\'s pie']

go_on = True
list = []
while(go_on == True):
   guess = str(random.choice(meals))
   meals.remove(guess)
   y_n = input('How about ' + guess + ' (y/n/"stop")')

   while((y_n != 'y') & (y_n != 'n') & (y_n != 'stop')):
      y_n = input('Sorry, I didn\'t recognize ' + y_n + 
         ', please type "y", "n", or "stop" to making ' + guess)

   if((y_n == "stop") | (len(meals) == 0)):
      if(len(meals) == 0):
         print('\n\nThat\'s all of the recipes I\'ve got for you!  Ask Dave to add some more!!\n')
         sleep(2)
      go_on = False
      if(len(list) != 0):
         print('OK, here\'s your list:')
         for recipe in list:
            print(recipe)
         dmy = input('Type any key to exit')
      print('OK, catch ya later!!')
      sleep(2)
   elif(y_n == 'y'):
      print('Great! I\'ll add ' + guess + ' to the list!')
      list.append(guess)
      sleep(1)
   elif(y_n == 'n'):
      print('No problem, let\'s try something else')
      sleep(1)
