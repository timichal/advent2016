import hashlib
doorid = "ffykfhsq"
password = ["_"]*8

def md5(code):
	return 

index = 0
while "_" in password:
	mdhash = hashlib.md5(bytes(doorid + str(index), 'utf-8')).hexdigest()
	if mdhash.startswith("00000") and mdhash[5] in "01234567":
		if password[int(mdhash[5])] == "_":
			password[int(mdhash[5])] = mdhash[6]
		print(password)
	index += 1
print("".join(password))