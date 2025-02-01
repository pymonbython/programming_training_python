from password_validators.validators import PasswordValidator, ValidationError

with open('passwords.txt') as input_file, open('bezpieczne.txt', 'w') as output_file:
    for password in input_file:

        try:
            validator = PasswordValidator(password.strip())
            validator.validate()
            output_file.write(password.strip() + '\n')
        except ValidationError as e:
            print(e)

# KeePassXC
