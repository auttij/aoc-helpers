from time import perf_counter
def timer(func):
	'''Decorator that prints the execution time'''
	
	def wrap(*args, **kwargs):
		start = perf_counter()
		result = func(*args, **kwargs)
		end = perf_counter()

		print(f"{(end - start )* 1000} ms")
		
		return result
	return wrap

def log_result(func, log=print):
	'''Decorator that prints the result of the executed function'''
	def wrap(*args, **kwargs):
		result = func(*args, **kwargs)
		log(f"{func.__name__}:")
		log(f"{result = }")
		return result
	return wrap