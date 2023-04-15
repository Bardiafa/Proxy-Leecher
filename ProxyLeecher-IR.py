import asyncio
import aiohttp
import re
from concurrent.futures import ThreadPoolExecutor
import os
import base64

proxys = []

async def sorce1():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("http://free-proxy.cz/en/proxylist/country/IR/all/ping/all") as response:
            html = await response.text()
        for tr in re.findall(r'<tr.*?>(.*?)</tr>', html, re.DOTALL):
            ip_address_b64_match = re.search(r'Base64\.decode\("(.*?)"\)', tr)
            if ip_address_b64_match:
                ip_address_b64 = ip_address_b64_match.group(1)
                ip_address = base64.b64decode(ip_address_b64).decode('utf-8')
                port = re.search(r'<span class="fport".*?>(.*?)</span>', tr).group(1)
                proxys.append(f"{ip_address}:{port}")
    return "s1:ok"

async def sorce2():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("http://free-proxy.cz/en/proxylist/country/IR/all/ping/all/2") as response:
            html = await response.text()
        for tr in re.findall(r'<tr.*?>(.*?)</tr>', html, re.DOTALL):
            ip_address_b64_match = re.search(r'Base64\.decode\("(.*?)"\)', tr)
            if ip_address_b64_match:
                ip_address_b64 = ip_address_b64_match.group(1)
                ip_address = base64.b64decode(ip_address_b64).decode('utf-8')
                port = re.search(r'<span class="fport".*?>(.*?)</span>', tr).group(1)
                proxys.append(f"{ip_address}:{port}")
    return "s2:ok"

async def sorce3():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("http://free-proxy.cz/en/proxylist/country/IR/all/ping/all/3") as response:
            html = await response.text()
        for tr in re.findall(r'<tr.*?>(.*?)</tr>', html, re.DOTALL):
            ip_address_b64_match = re.search(r'Base64\.decode\("(.*?)"\)', tr)
            if ip_address_b64_match:
                ip_address_b64 = ip_address_b64_match.group(1)
                ip_address = base64.b64decode(ip_address_b64).decode('utf-8')
                port = re.search(r'<span class="fport".*?>(.*?)</span>', tr).group(1)
                proxys.append(f"{ip_address}:{port}")
    return "s3:ok"

async def sorce4():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://hidemy.name/en/proxy-list/countries/iran/", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}) as response:
            html = await response.content.read()
            html = html.decode('iso-8859-1')
            matches = re.findall(r"<tr><td>(?P<ip>\b(?:[0-9]{1,3}\.){3}[0-9]{1,3})<\/td><td>(?P<port>\d+)<\/td>" , html)
            for line in matches:
                proxys.append(f"{line[0]}:{line[1]}")
    return "s4:ok"

async def sorce5():
    global proxys
    async with aiohttp.ClientSession() as session:
        for page in range(304):
            async with session.get(f"https://www.freeproxy.world/?type=&anonymity=&country=IR&speed=&port=&page={page}") as response:
                html = await response.text()
                ip_pattern = r"<td class=\"show-ip-div\">\s*(?P<ip>(?:\d{1,3}\.){3}\d{1,3})\s*<\/td>"
                port_pattern = r"<a href=\"\/\?port=(?P<port>\d+)\">"

                ip_match = re.findall(ip_pattern, html)
                port_match = re.findall(port_pattern, html)
                for ip, port in zip(ip_match, port_match):
                    proxys.append(f"{ip}:{port}")

    return "s5:ok"

async def main():
    global proxys
    with ThreadPoolExecutor(max_workers=8) as executor:
        tasks = []
        tasks.append(asyncio.ensure_future(sorce1()))
        tasks.append(asyncio.ensure_future(sorce2()))
        tasks.append(asyncio.ensure_future(sorce3()))
        tasks.append(asyncio.ensure_future(sorce4()))
        tasks.append(asyncio.ensure_future(sorce5()))

        # Wait for all tasks to complete before continuing
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

    count = len(proxys)
    print(str(count) + " proxies scraped")

if __name__ == "__main__":
    pt = os.path.dirname(__file__)
    good = os.path.join(pt, "good.txt")
    asyncio.run(main())
    
    # save the results to the file
    with open(good, "w") as f:
        for proxy in proxys:
            f.write(proxy + "\n")
    
    count = len(proxys)
    print(f"{count} proxies scraped and written to {good}")
