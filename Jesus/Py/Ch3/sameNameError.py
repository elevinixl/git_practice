def spam(): # fails due to exception handling
   print(eggs) # ERROR!
   eggs = 'spam local'

eggs = 'global'
spam()