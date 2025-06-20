# Async Example:

import asyncio

async def pani_ubalo():
    print("Pani Ubalna Shuru...")
    await asyncio.sleep(1)
    print("Pani Ubal Gaya.")

async def roti_banao():
    print("Roti Banana Shuru...")
    await asyncio.sleep(2)
    print("Roti Ban Gayi.")

async def main():
    await asyncio.gather(
        pani_ubalo(),
        roti_banao()
    )

asyncio.run(main())
