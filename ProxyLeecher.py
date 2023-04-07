import asyncio
import aiohttp
import aiohttp_socks
import re
from bs4 import BeautifulSoup
from typing import List
import argparse
import json
from concurrent.futures import ThreadPoolExecutor
import os

proxys = []

async def sorce1():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.proxy-daily.com/") as response:
            html = await response.text()
        lines = str(html).split('</script><br><div class="centeredProxyList">Free Http/Https Proxy List:</div><br><div class="centeredProxyList freeProxyStyle">')[1].split('</div><br><br><divclass="centeredProxyList">Free Socks4 Proxy List:</div><br><div class="centeredProxyList freeProxyStyle">')[0]
        match = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]+\b",lines)
        lines = [line for line in match]
        proxys.extend(lines)
    return "s1:ok"

async def sorce2():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.sslproxies.org/") as response:
            html = await response.text()
        lines = str(html).split('<tbody>')[1].split('</tbody>')[0]
        match = re.findall(r"<tr><td>(?P<ip>\b(?:[0-9]{1,3}\.){3}[0-9]{1,3})<\/td><td>(?P<port>\d+)<\/td><td>\w+<\/td><td class='hm'>(?P<country>\w+|\w+ \w+)<\/td><td>",lines)
        for line in match:
            proxys.append(f"{line[0]}:{line[1]}")
    return "s2:ok"

async def sorce3():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all") as response:
            html = str(await response.text()).splitlines()
        for line in html:
            proxys.append(line)
    return "s3:ok"

async def sorce4():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://hidemy.name/en/proxy-list/", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}) as response:
            html = await response.content.read()
            html = html.decode('iso-8859-1')
            matches = re.findall(r"<tr><td>(?P<ip>\b(?:[0-9]{1,3}\.){3}[0-9]{1,3})<\/td><td>(?P<port>\d+)<\/td>" , html)
            for line in matches:
                proxys.append(f"{line[0]}:{line[1]}")
    return "s4:ok"

async def sorce5():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.proxy-list.download/HTTP", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}) as response:
            html = await response.text()
            matches = re.findall(r"<tr>\s+<td>\s+(?P<ip>.*?)\s+<\/td>\s+<td>\s+(?P<port>\d+)\s+<\/td>" , html)
            for line in matches:
                proxys.append(f"{line[0]}:{line[1]}")
    return "s5:ok"

async def sorce6():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://us-proxy.org/") as response:
            html = await response.text()
            lines = str(html).split('<tbody>')[1].split('</tbody>')[0]
            match = re.findall(r"<tr><td>(?P<ip>\b(?:[0-9]{1,3}\.){3}[0-9]{1,3})<\/td><td>(?P<port>\d+)<\/td><td>\w+<\/td><td class='hm'>(?P<country>\w+|\w+ \w+)<\/td><td>",lines)
            for line in match:
                proxys.append(f"{line[0]}:{line[1]}")
        return "s6:ok"

async def sorce7():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.proxy-list.download/api/v2/get?l=en&t=https") as response:
            html = await response.text()
            lines = json.loads(html)['LISTA']
            for i in lines:
                proxys.append(f"{i['IP']}:{i['PORT']}")
    return "s7:ok"

async def sorce8():
    global proxys
    async with aiohttp.ClientSession() as session:
        for page in range(500):
            async with session.get(f"https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page={page}") as response:
                html = await response.text()
                ip_pattern = r"<td class=\"show-ip-div\">\s*(?P<ip>(?:\d{1,3}\.){3}\d{1,3})\s*<\/td>"
                port_pattern = r"<a href=\"\/\?port=(?P<port>\d+)\">"

                ip_match = re.findall(ip_pattern, html)
                port_match = re.findall(port_pattern, html)
                for ip, port in zip(ip_match, port_match):
                    proxys.append(f"{ip}:{port}")

    return "s8:ok"

async def main():
    global proxys
    with ThreadPoolExecutor(max_workers=20) as executor:
        tasks = []
        tasks.append(asyncio.ensure_future(sorce1()))
        tasks.append(asyncio.ensure_future(sorce2()))
        tasks.append(asyncio.ensure_future(sorce3()))
        tasks.append(asyncio.ensure_future(sorce4()))
        tasks.append(asyncio.ensure_future(sorce5()))
        tasks.append(asyncio.ensure_future(sorce6()))
        tasks.append(asyncio.ensure_future(sorce7()))
        tasks.append(asyncio.ensure_future(sorce8()))

        # Wait for all tasks to complete before continuing
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

    count = len(proxys)
    print(str(count) + " proxies scraped")

if __name__ == "__main__":
    pt = os.path.dirname(__file__)
    good = os.path.join(pt, "proxies.txt")
    asyncio.run(main())
    
    # save the results to the file
    with open(good, "w") as f:
        for proxy in proxys:
            f.write(proxy + "\n")
    
    count = len(proxys)
    print(f"{count} proxies scraped and written to {good}")
