def except_handle_gene(num):
    for i in range(num):
        yield i
        
n=except_handle_gene(20)
while True:
    try:
        print(next(n))
    except StopIteration:
        break