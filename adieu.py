def adieu(names):
  if len(names) == 1:
    print('Adieu, adieu, to ' +names[0])
  elif len(names) == 2:
    print('Adieu, adieu, to ' +names[0]+ ' and '+ names[1])
  elif len(names) == 3:
    print('Adieu, adieu, to ' +names[0]+ ' ,'+ names[1]+ 'and'+names[2])
  else:
    i = ' ,'.join(names[:-1]) +' '+ ' and '+' ' +names[-1]
    print('Adieu, adieu, to ' + ' ,'.join(names[:-1]) +' and '+names[-1])

if __name__ == '__main__':
  names= []
    
  try:
    while True:
        name = input('name: ')
        names.append(name)
  except EOFError:
    pass
  
  adieu(names)