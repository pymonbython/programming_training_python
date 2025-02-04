from string import Template

message = Template('$first_name zjadł dziś $count pączków.')

info = [
    ('Ania', 10),
    ('Hubert', 30)
]

for first_name, count in info:
    text =message.substitute(first_name=first_name, count=count)

    print(text)