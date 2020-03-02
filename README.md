# fetch-bduss-baiduid ![Python package](https://github.com/ffreemt/fetch-bduss-baiduid/workflows/Python3.6|3.7%20package/badge.svg) [![codecov](https://codecov.io/gh/ffreemt/fetch-bduss-baiduid/branch/master/graph/badge.svg)](https://codecov.io/gh/ffreemt/fetch-bduss-baiduid)
��ȡ BDUSS �� BAIDUID

### Installation
Not available yet
```pip install fetch-bduss-baiduid```

Validate installation
```
python -c "import fetch_bduss_id; print(fetch_bduss_id.__version__)"
0.0.1
```

### Usage

```
import asyncio
from fetch_bduss_id import fetch_bduss_id

asyncio.get_event_loop().run_until_complete(fetch_bduss_id('test this and that'))
# '测试这个和那个'
```

### Acknowledgments

* Thanks to everyone whose code was used
