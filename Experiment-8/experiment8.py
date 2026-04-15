import re

doc = input("DOC (DD/MM/YY): ")

passphrase = "one brown bear up let brown drop tame"
id = "sk_jfcwokheru 8408vgr"

pattern = "brown"

# match
r = re.match("sk", id)
if r:
    print("valid key")
else:
    print("key invalid")

# search
r = re.search("brown", passphrase)
if r:
    print("passphrase valid case 1")
else:
    print("passphrase invalid")

# findall
r = re.findall(pattern, passphrase)
if r:
    print("passphrase valid case 2")
else:
    print("invalid passphrase")

# replace
v = re.sub("bear", "cat", passphrase)
print(v)

# extract numbers
r = re.findall("[0-9]+", id)
print(r)

# date validation
r = r"\d{2}/\d{2}/\d{2}$"
v = re.match(r, doc)

if v:
    print("valid DOC")
else:
    print("invalid DOC")
