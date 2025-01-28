from hashlib import sha1

text = b'abrakadabra'
text2 = b'abrakadabr'
my_hash = sha1(text)
my_hash2 = sha1(text2)
# print(help(my_hash))

# print(my_hash.digest())
print(my_hash.hexdigest())
print(my_hash2.hexdigest())


