# https://www.youtube.com/playlist?list=PLyb_C2HpOQSBsygWeCYkJ7wjxXShIql43

import asyncio
from time import time


async def dur_disp():
    start = time()
    while True:
        dur = int(time()-start)

        if dur % 3 == 0:
            print(f"{dur} sec passed")

        await asyncio.sleep(1)


async def print_nums():
    num = 1

    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)


# * Python 3.6 -
# async def main():
#     task1 = asyncio.ensure_future(dur_disp())
#     task2 = asyncio.ensure_future(print_nums())
#     await asyncio.gather(task1, task2)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()


# * Python 3.7 +
# async def main():
#     task1 = asyncio.create_task(dur_disp())
#     task2 = asyncio.create_task(print_nums())
#     await asyncio.gather(task1, task2)

# asyncio.run(main())
