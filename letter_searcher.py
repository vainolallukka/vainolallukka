def main():
    import random
    
    #opening the file with the list of alphabets#
    open_file = open("alphabets.txt", "r")
    list_file = []

    #saving all letters to a list#
    for line in open_file:
        strip_lines = line.strip()
        list_file.append(strip_lines)

    alphabets_amount = len(list_file)

    random_list = []

    #creating a list with a set amount of letters chosen randomly#
    for i in range(100):
        rand_int = random.randint(0, len(list_file)-1)
        random_list.append(list_file[rand_int])
    
    print("Find letter:")
    letter = str(input())

    count = 0

    #finding how many times the letter is in the list#
    for i in random_list:
        if i == letter:
            count += 1

    print("Letter {:s} is found in list {:d} times".format(letter, count))
    
main()