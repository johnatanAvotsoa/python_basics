from xmlrpc.client import FastMarshaller


def search_for(number_to_seek , array) :
    mil = len(array) // 2
    left_pointer = array[0]
    right_pointer = array[len(array)-1]
    while left_pointer < right_pointer  :
        if number_to_seek == mil :
            return True
        elif number_to_seek < mil :
            right_pointer = array[mil]
        else :
            left_pointer = array[mil]
        print(f" l = {left_pointer}, r={right_pointer} , mil = {mil}")

    return False

a = [-10,1,1.3,2,3,4]
print(search_for(2,a))
