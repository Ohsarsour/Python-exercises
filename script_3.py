def get_comm_dict(string):
    # Converting the string to lowercase
    string = string.lower()
    # Remove whitespace from the string
    string = string.replace(" ", "")

    comm_dict = {}  
    # common dict with loops
    for i in string:
        if i in comm_dict:
            comm_dict[i] += 1
        else:
            comm_dict[i] = 1
    return comm_dict


string = input("Enter a string: ")

print(get_comm_dict(string))