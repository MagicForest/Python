import time
import exercise_11_8

def timeit(func, *nkwargs, **kwargs):
   start_time = time.time()
   try:
       result = func(*nkwargs, **kwargs)
   except Exception, e:
       result =  str(e)
   cost_time = time.time() - start_time
   return cost_time, result

if __name__ == '__main__':
    print timeit(exercise_11_8.filter_leap_year, (i for i in range(1, 2001)))
