# 装饰器工具库

一个 Python 装饰器工具库，包含两个常用装饰器：

1. **计时装饰器**：统计函数运行耗时
2. **缓存装饰器**：带有效期的缓存，过期自动重新计算

## 环境

- Python 3.8+
- 无第三方依赖

## 功能一：计时装饰器

统计函数运行耗时，并捕获异常。

```python
import time
from decorators import timer_decorator

@timer_decorator
def slow_add(a, b):
    time.sleep(1)
    return a + b

slow_add(1, 2)
# 输出：slow_add 耗时 1.0002 秒
```

## 功能二：缓存装饰器

带有效期的缓存，过期自动重新计算。

```python
import time
from decorators import cache

@cache(expire=5)
def slow_add(a, b):
    print("正在计算...")
    time.sleep(0.5)
    return a + b

slow_add(1, 2)   # 计算，输出：正在计算...
slow_add(1, 2)   # 读取缓存，不计算
time.sleep(6)
slow_add(1, 2)   # 缓存过期，重新计算
```

## 运行测试

```bash
python -m pytest
```

预期输出：

```
所有测试通过
```

## 项目结构

```
装饰器工具库/
├── decorators.py          # 核心代码
├── test_decorators.py     # 测试代码
└── README.md              # 项目说明
```

## 作者

GitHub: [https://github.com/seqse2022-create]