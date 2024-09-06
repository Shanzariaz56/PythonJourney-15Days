"""zip function return a zip value object which is an iterator of tuples,
where first items in each pass iterator is paiedx together,
like, we have two tuple, one tuple contain more items,
so these items are ignored """

a=("shanzy","saira","ayesha")
b=("Backend","javascript","articles","django")
c=zip(a,b)
c_list=list(c)
print(c_list)