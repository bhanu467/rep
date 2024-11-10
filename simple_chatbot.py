def coffee_bot():
  print("Welcome to th()e cafe!")
  size=get_size()
  drink_type=get_drink_type()
  cup=cup_type()
  temp=temp_type()
  #print(size)
  #print(drink_type)
  print("alright, that's a {} {}!".format(size,drink_type))
  name=input("can i get ur name?\n")
  print("Thanks, {}! your {} drink will be ready shortly in a {} cup.".format(name,temp,cup))
  
def get_size():
  res=input("What size drink can i get for u? \n[a] small\n[b] medium \n[c] large \n")
  if res=='a':
    return 'small'
  elif res=='b':
    return 'medium'
  elif res=='c':
    return 'large'
  else:
    print_message()
    return get_size()
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
def get_drink_type():
  res=input("What type of drink would you like?\n[a] Brewed Coffee\n[b] Mocha\n[c] Latte\n")
  if res=='a':
     return 'brewed coffee'
  elif res=='b':
    return 'mocha'
  elif res=='c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
def order_latte():
  res=input("and what kind of milk for your latte\n[a] 2% milk\n[b] non-fat milk\n[c] soy milk\n")
  if res=='a':
   return 'latte'
  elif res=='b':
    return 'non-fat latte'
  elif res=='c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()
def cup_type():
  res=input("what kind of a cup would you like?\n[a] plastic\n[b] reusable\n")
  if res=='a':
   return 'plastic'
  elif res=='b':
    return 'reusable'
  else:
    print_message()
    return cup_type()
def temp_type():
  res=input("how would u like your coffe?\n[a] hot\n[b] iced\n")
  if res=='a':
   return 'hot'
  elif res=='b':
    return 'iced'
  else:
    print_message()
    return temp_type()



# Call coffee_bot()!
coffee_bot()

