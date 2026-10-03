# decorators.py
import time
import functools


def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"{func.__name__} 异常: {e}")
            return None
        finally:
            end = time.time()
            print(f"{func.__name__} 耗时 {end - start:.4f} 秒")
    return wrapper


def cache(expire):
    memo = {}
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))
            delete_list = []
            for k, (result, 秒数, 存入时间) in memo.items():
                if time.time() - 存入时间 > 秒数:
                    delete_list.append(k)
            for k in delete_list:
                del memo[k]
            if key in memo:
                print("读取缓存")
                return memo[key][0]
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                print(f"{func.__name__} 异常: {e}")
                return None
            print("正在纳入缓存")
            memo[key] = (result, expire, time.time())
            return result
        return wrapper
    return decorator