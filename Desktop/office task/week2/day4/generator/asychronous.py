# asynchronous simple example
import asyncio
async def asy_gene(num):
    for i in range(num):
        await asyncio.sleep(1)
        yield i
async def main():
    async for item in asy_gene(20):
        print(item)
asyncio.run(main())

# asynchronous fibonacci example
async def fibonacci(num):
    fib=[]
    a,b=0,1
    while True:
        c=a+b
        a,b=b,c
        await asyncio.sleep(1)
        yield c
        
async def main():
    f=fibonacci(20)
    async for i in f:
        print(i)
asyncio.run(main())    

    