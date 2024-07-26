import hashlib as h
# file = open('5.txt', 'r')
# input = file.read()
# lines = input.split("\n")



def main ():
    input : str = "abc"
    password : str = ""
    index : int = 3231928

    while len(password) < 8 :

        id = input + str(index)
        hash = h.md5(id.encode()).hexdigest()

        if str(hash).startswith("00000") :
            password += str(hash)[5]

        index += 1
        print(index, password)

    print(password)

main()