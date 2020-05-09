def spam():
    global eggs
    eggs = 'spam'  # this is the global

def bacon():
    eggs = 'bacon'  # this is a local

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)
