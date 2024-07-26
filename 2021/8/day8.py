file = open('day8.txt', 'r')
input = file.read()
lines = input.split("\n")


input = []
for entry in lines :
    input.append(entry.split(" | "))

def filter(length,num,words):
    for word in words:
        if len(word) == length:
            count = 0
            for letters in num :
                if letters in word:
                    count +=1
                if count == len(num):
                    for letters2 in word:
                        if letters2 not in num:
                            return letters2
                        
def unique(line_number):
    unique_segment= []
    digits = 0
    entry = input[line_number]
    length = 2,3,4,7
    for segment in (entry[0].split(" ")):
        if (len(segment)) in length:
            digits += 1
            # print(segment)
            unique_segment.append(segment)
    # for segment in (entry[1].split(" ")):
    #     if (len(segment)) in length:
    #         digits += 1
    
    return (sorted(unique_segment, key=len))
    # print(digits)

# (unique(1)

def decode(entry) : 
    a = ""
    unique_words = unique(entry)
    output = input[entry][1].split(" ")
    words = input[entry][0].split(" ")
    one = unique_words[0]
    four = unique_words[2]
    seven = unique_words[1]
    eight = unique_words[3]

    # get a
    for segments in seven :
        if segments not in one:
            a = segments
    
    nine = seven
    for letters in four:
        if letters not in seven:
            nine += letters
    # get g
    g = filter(6,nine,words)

    three = one + g + a
    # get d
    d = filter(5,three,words)

    four = one + d
    # get b
    b = filter(4,four,words)

    five = d + g + b + a
    # get f
    f = filter(5,five,words)

    one = f
    #get c
    c = filter(2, one,words)

    eight = a + b + c + d + f + g
    #get e
    e = filter(7,eight,words)

    key = [a,b,c,d,e,f,g]
    key2 = ["a","b","c","d","e","f","g"]
    # key = [["a",a],["b",b],["c",c],["d",d],["e",e],["f",f],["g",g]]

    result = []
    for niggas in output:
        code = ""
        for letter in niggas:
            if letter in key:
                i = key.index(letter)
                code += key2[i]
        result.append(code)

    values = ["abcefg","cf","acdeg","acdfg","bdcf","abdfg","abdefg","acf","abcdefg","abcdfg"]

    answer = ""
    for word in result :
        for word2 in values:
            if sorted(word) == sorted(word2):
                num = values.index(word2)
                answer += str(num)

    # print(result)
    # print(values)

    return(answer)



# def transform(key,input):
sum = 0
for i in range(len(lines)):
    sum += (int(decode(i)))

print(sum)

    




