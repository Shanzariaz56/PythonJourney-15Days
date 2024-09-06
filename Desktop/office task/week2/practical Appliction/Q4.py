import time
def exe_log(func):
    def inner(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)
        end=time.time()
        execution_time=end-start
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return res
    return inner
@exe_log
def any_func():
    time.sleep(1)
any_func()
    