file = open('4.txt', 'r')
input = file.read()
lines = input.split("\n")

def check_real(chars, checksum, id):
    output = ""
    chars2 = chars.copy()
    for i in range(len(chars)):
        max_let = (max(chars, key=chars.get))
        output += max_let
        del chars[max_let]

    real = True

    new_output = check_equal(output, chars2, checksum, id)

    for i in checksum :
        if i not in new_output :
            real = False

    return real

def check_equal(order, char, check_sum,id):
    dups = {}
    for i in order:
        num = char[str(i)]
        if num not in dups:
            dups[num] = [i]
        else:
            dups[num].append(i)

    new_output = ""
    values = ""
    for n in dups :
        values += str(n)

    if len(dups) <= 5 :
        for j in dups:
            for letters in dups[j] :
                new_output += letters
    else:
        for l in values[:5]:
            for letters in dups[int(l)] :
                new_output += letters

    print(dups, ''.join(sorted(new_output)), ''.join(sorted(check_sum)), id)
    return(new_output)

def main():
    c = 0
    sum = 0
    for name in lines:
        chars = {}
        split_name = name.split("-")
        checksum = split_name[-1].split("[")[1].split("]")[0]
        id = split_name[-1].split("[")[0]

        for letters in split_name[:-1]:
            for char in letters:
                if char not in chars :
                    chars[char] = 1
                else:
                    chars[char] += 1

        if check_real(chars,checksum, id) :
            c += 1
            sum += int(id)
            # print(checksum)

    # print(sum)
    # print(c)

main()

