# Not a fancy search logic just simple list iterate through and compare initial
# list value with the rest and keep replacing it with the greatest value
# THE LIST IS NOT SORTED so iterating through it is a must! trivial solution for# loop and a buffer variable for greatest number

the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1495785517,
    1858250798,
    1693786723,
    1871655963,
    374455497,
    430158267,
]

max = the_list[0]

for i in the_list:
    if i >= max:
        max = i

print(max)
