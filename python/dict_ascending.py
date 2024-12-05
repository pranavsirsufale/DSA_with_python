#Write a python script to sort (ascending and descending) a dictionary by value.

def sort_dict_by_value(d, ascending=True):
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))
    return sorted_dict


my_dict = {'apple': 5, 'banana': 2, 'cherry': 10, 'date': 7}

sorted_dict_asc = sort_dict_by_value(my_dict, ascending=True)
print("Sorted Dictionary (Ascending):", sorted_dict_asc)


sorted_dict_desc = sort_dict_by_value(my_dict, ascending=False)
print("Sorted Dictionary (Descending):", sorted_dict_desc)
