def search_for(number_to_seek , array) :
    left_pointer = 0
    right_pointer = len(array)-1
    while left_pointer < right_pointer  :
        mil = (left_pointer + right_pointer) // 2
        if number_to_seek == array[mil] :
            return True , mil
        elif number_to_seek < array[mil] :
            right_pointer = mil - 1
        else:
            left_pointer = mil + 1
        print(f" l = {left_pointer}, r={right_pointer} , mil = {mil}")

    return False

a = [-10,1,1.3,2,3,4]
print(search_for(1.3,a))