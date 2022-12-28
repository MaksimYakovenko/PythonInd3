import math

def only_kwargs(f):
 def _only_kwargs(*args, **kwargs):
  if args:
    raise RuntimeError("Функції не містить ключові параметри")
  return f(*args, **kwargs)
 return _only_kwargs

@only_kwargs
def sin(x):
 return math.sin(x)


if __name__ == '__main__':
  print(sin(x=math.pi/6))
try:
    print(sin(-math.pi / 2))
except Exception as e:
    print(e)