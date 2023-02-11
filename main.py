from asyncio import run, set_event_loop_policy, WindowsSelectorEventLoopPolicy, sleep as asleep

async def main():
    from obs_websocket import OBSWebSocket, RecordRequests

    obs = OBSWebSocket(passwd="PRr6ilrwl3q8mw8J")
    await obs.connect()

    status = await RecordRequests.GetRecordStatus(obs)
    if status:
        await RecordRequests.StopRecord(obs)
    await RecordRequests.StartRecord(obs)
    await asleep(3)
    print(await RecordRequests.StopRecord(obs))
    input("End...")

    await obs.close()

if __name__ == "__main__":
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())

    run(main())