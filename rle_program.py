
# Method 1
def to_hex_string(data):
    str = ""
    for i in data:
        h = hex(i)
        str += h[2:]

    return str

if __name__ == '__main__':
# printing the output
    print(to_hex_string([3, 15, 6, 4]))




# Method 2
def count_runs(flat_data):
    i = 0
    loop_count = 0
    while i < len(flat_data):
        j = i + 1
        count = 1
        while j < len(flat_data) and flat_data[i] == flat_data[j]:
            j += 1
            count += 1
            if count == 15:
                count = 1
                i =+ 1
        i = j
        loop_count += 1
    return loop_count

if __name__ == '__main__':
# printing the output
    print(count_runs([15, 15, 15, 4, 4, 4, 4, 4, 4]))




# Method 3
def encode_rle(flat_data):
    encode_lst = []
    i = 0
    while i < len(flat_data):
        j = i + 1
        count = 1
        while j < len(flat_data) and flat_data[i] == flat_data[j] and count < 15:
            j += 1
            count += 1
        encode_lst.append(count)
        encode_lst.append(flat_data[i])
        i = j
    return encode_lst


# testing code
print(encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]))



# Method 4
     # method that needs to be implemented
def get_decoded_length(rle_data):
    length = 0
    for i in range(0, len(rle_data), 2):
        length += rle_data[i]
    return length

if __name__ == '__main__':
# testing code
    print(get_decoded_length([3, 15, 6, 4]))






# Method 5
'''''def decode_rle(rle_data):
    # creating a new list to append the data
    newList = []
    # looping through the list and using step over parameter to access alternate numbers in the list
    for i in range(0, len(rle_data), 2):
        # appending the value to the list by duplicating it n times according the rel
        newList += [rle_data[i + 1]] * rle_data[i]
    print(newList)

decode_rle([3, 15, 6, 4])
'''''

def decode_rle(rle_data):
    decoded_rle = [0]*(len(rle_data))
    num_happens = 0
    decoded_rle = [] * (len(rle_data))
    for i in range(0, len(rle_data), 2):
        num_happens = rle_data[i]
        number = rle_data[i+1]
        decoded_rle.extend(number for g in range(num_happens))

    return decoded_rle

print(decode_rle([3, 15, 6, 4]))



# Method 6
def string_to_data(data_string):
    # Convert the string to a list of individual characters
    data = list(data_string)

    # Loop over each character, converting it to a numeric value
    i = 0
    while i < len(data):
        # Convert hex to int, 16 denotes the data[i] is in hex
        data[i] = int(data[i], 16)
        i = i + 1

    return data
if __name__ == '__main__':
    print(string_to_data("3f64"))