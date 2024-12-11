mlist = [4,3,5]

print(sorted(mlist)) # does not affect original list
print(mlist)
# mlist.clear()
print(mlist)

mlist.append(4)
print(mlist)

print(mlist.count(4))

# mlist.extend({10,15})
# print(mlist)

# print(type(mlist))

mlist.insert(0,6) # first : index : second : value
print(mlist)

print(mlist.index(4)) # provides index of the given vlaue
mlist.remove(4)       # remove first occurence 


mlist.reverse()
print(mlist)


secondlist = mlist.copy()

secondlist.clear()

print(secondlist)


print(min(mlist))
print(max(mlist))




print(mlist)
print(mlist)




