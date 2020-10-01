import base64

print("Python Base64 Program")
print("===== Choose tools ======")
print("1. Base64                ")
print("2. Base16                ")
print("3. Coming soon ....      ")
print("=========================")
userInput = input("Choose number: ")

if(userInput == "1"):
	print("==================")
	print("1. Encode")
	print("2. Decode")
	print("==================")
	userInput = input("Choose number: ")
	if(userInput == "1"):
		text = input("Input text you want to encode: ")
		b64text = base64.b64encode(text.encode("utf-8"))
		b64text = str(b64text, "utf-8")
		print("Encoded text: " + b64text)
	if(userInput == "2"):
		text = input("Input base64 you want to decode: ")
		plain = base64.b64decode(text)
		print("Decoded text: "+ str(plain, "utf-8"))
elif(userInput == "2"):
	print("==================")
	print("1. Encode")
	print("2. Decode")
	print("==================")
	userInput = input("Choose number: ")
	if(userInput == "1"):
		text = input("Input text you want to encode: ")
		b16text = base64.b16encode(text.encode("utf-8"))
		b16text = str(b16text, "utf-8")
		print("Encoded text: " + b16text)
	if(userInput == "2"):
		text = input("Input base16 you want to decode: ")
		plain = base64.b16decode(text)
		print("Decoded text: "+ str(plain, "utf-8"))
