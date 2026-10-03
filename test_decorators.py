
import time
from decorators import timer_decorator, cache


@timer_decorator
def timing_test():
    time.sleep(1)
    return "计时完成"


@cache(expire=5)
def cache_testing(a, b):
    time.sleep(0.5)
    print("正在计算")
    return a + b


if __name__ == "__main__":
    print("--- 计时装饰器测试 ---")
    timing_test()

    print("\n--- 缓存装饰器测试 ---")
    print(cache_testing(1, 2))
    print(cache_testing(1, 2))
    time.sleep(6)
    print(cache_testing(1, 2))