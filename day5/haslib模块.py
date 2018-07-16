import hashlib

m = hashlib.md5()
m.update(b"I love study")
print(m.hexdigest())
m.update(b"i like coding")

print(m.hexdigest())
m2 = hashlib.md5()
m2.update(b"I love studyi like coding")

print(m2.hexdigest())

