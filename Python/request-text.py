# imports
import aiohttp
import asyncio

async def siesta(main_endpoint, sub_endpoint, response_type: 'text'):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://siesta.red/api/{main_endpoint}/{sub_endpoint}?type={response_type}') as r:
            text = await r.text()
            return str(text)
        
# print async environment
async def main():
    print(await siesta("gif", "cuddle"))

# create async environment
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
