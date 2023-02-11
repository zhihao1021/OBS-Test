from asyncio import sleep, new_event_loop, set_event_loop_policy, WindowsSelectorEventLoopPolicy

async def main(i):
    for _ in range(i + 2):
        print(i)
        await sleep(1)

if __name__ == "__main__":
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())
    loop = new_event_loop()
    tasks = [
        loop.create_task(main(i))
        for i in range(5)
    ]
    for task in tasks:
        loop.run_until_complete(task)
