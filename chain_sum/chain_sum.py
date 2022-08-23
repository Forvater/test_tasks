# chain_sum(5)()         5
# chain_sum(10)(3)()     13
# chain_sum(10)(3)(-7)()   6

def chain_sum(*num):
    class Counter:
        def __init__(self, *accum):
            self._accum = accum[0]

        def __call__(self, *num):
            if len(num) != 0 :
                return Counter(self._accum + num[0])
            else :
                return self._accum

    if len(num) != 0 :
        return Counter(num[0])
    else :
        return 0 


print(chain_sum(5)())
print(chain_sum(10)(3)())
print(chain_sum(10)(3)(-7)())


print('------------------------------')


def chain_sum2(number):
    result = number

    def wrapper(number2 = None):
        nonlocal result
        if number2:
            result += number2
            return wrapper
        return result

    return wrapper


print(chain_sum2(5)())
print(chain_sum2(10)(3)())
print(chain_sum2(10)(3)(-7)())


print('------------------------------')


def chain_sum3(*num):
    class Counter:
        def __init__(self, *accum):
            self._accum = accum[0]

        def __call__(self, *num):
            if len(num) != 0 :
                return Counter(self._accum + num[0])
            else :
                return self._accum

        def __str__(self):
            return str(self._accum)

    if len(num) != 0 :
        return Counter(num[0])
    else :
        return 0 


print(chain_sum3(5))
print(chain_sum3(10)(3))
print(chain_sum3(10)(3)(-7))


print('------------------------------')


def chain_sum4(*num):
    class Counter(int):
        def __init__(self, *accum):
            self._accum = accum[0]

        def __call__(self, *num):
            if len(num) != 0 :
                return Counter(self._accum + num[0])
            else :
                return self._accum

    if len(num) != 0 :
        return Counter(num[0])
    else :
        return 0 


print(1 + chain_sum4(5))
print(1 + chain_sum4(10)(3))
print(1 + chain_sum4(10)(3)(-7))

