choice = None

def do_job(choice):
    print(choice)

while choice != 0:
    if choice := int(input('Twój wybór: ')):
        do_job(choice)
