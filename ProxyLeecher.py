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

async def source1():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.proxy-daily.com/") as response:
            html = await response.text()
        lines = str(html).split('</script><br><div class="centeredProxyList">Free Http/Https Proxy List:</div><br><div class="centeredProxyList freeProxyStyle">')[1].split('</div><br><br><divclass="centeredProxyList">Free Socks4 Proxy List:</div><br><div class="centeredProxyList freeProxyStyle">')[0]
        match = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]+\b",lines)
        lines = [line for line in match]
        proxys.extend(lines)
    return "s1:ok"

async def source2():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.sslproxies.org/") as response:
            html = await response.text()
        lines = str(html).split('<tbody>')[1].split('</tbody>')[0]
        match = re.findall(r"<tr><td>(?P<ip>\b(?:[0-9]{1,3}\.){3}[0-9]{1,3})<\/td><td>(?P<port>\d+)<\/td><td>\w+<\/td><td class='hm'>(?P<country>\w+|\w+ \w+)<\/td><td>",lines)
        for line in match:
            proxys.append(f"{line[0]}:{line[1]}")
    return "s2:ok"

async def source3():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all") as response:
            html = str(await response.text()).splitlines()
        for line in html:
            proxys.append(line)
    return "s3:ok"

async def source4():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://hidemy.name/en/proxy-list/", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}) as response:
            html = await response.content.read()
            html = html.decode('iso-8859-1')
            matches = re.findall(r"<tr><td>(?P<ip>\b(?:[0-9]{1,3}\.){3}[0-9]{1,3})<\/td><td>(?P<port>\d+)<\/td>" , html)
            for line in matches:
                proxys.append(f"{line[0]}:{line[1]}")
    return "s4:ok"

async def source5():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.proxy-list.download/HTTP", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}) as response:
            html = await response.text()
            matches = re.findall(r"<tr>\s+<td>\s+(?P<ip>.*?)\s+<\/td>\s+<td>\s+(?P<port>\d+)\s+<\/td>" , html)
            for line in matches:
                proxys.append(f"{line[0]}:{line[1]}")
    return "s5:ok"

async def source6():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://us-proxy.org/") as response:
            html = await response.text()
            lines = str(html).split('<tbody>')[1].split('</tbody>')[0]
            match = re.findall(r"<tr><td>(?P<ip>\b(?:[0-9]{1,3}\.){3}[0-9]{1,3})<\/td><td>(?P<port>\d+)<\/td><td>\w+<\/td><td class='hm'>(?P<country>\w+|\w+ \w+)<\/td><td>",lines)
            for line in match:
                proxys.append(f"{line[0]}:{line[1]}")
        return "s6:ok"

async def source7():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.proxy-list.download/api/v2/get?l=en&t=https") as response:
            html = await response.text()
            lines = json.loads(html)['LISTA']
            for i in lines:
                proxys.append(f"{i['IP']}:{i['PORT']}")
    return "s7:ok"

async def source8():
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

async def source9():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt") as response:
            lines = await response.text()
            for line in lines.split("\n"):
                if line.strip():
                    proxys.append(line.strip())
    return "s9:ok"

async def source10():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt") as response:
            lines = await response.text()
            for line in lines.split("\n"):
                if line.strip():
                    proxys.append(line.strip())
    return "s10:ok"

async def source11():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt") as response:
            lines = await response.text()
            for line in lines.split("\n"):
                if line.strip():
                    proxys.append(line.strip())
    return "s11:ok"

async def source12():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://raw.githubusercontent.com/fahimscirex/proxybd/master/anonymous-proxylist/http.txt") as response:
            lines = await response.text()
            for line in lines.split("\n"):
                if line.strip():
                    proxys.append(line.strip())
    return "s12:ok"


async def source13():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt") as response:
            lines = await response.text()
            for line in lines.split("\n"):
                if line.strip():
                    proxys.append(line.strip())
    return "s13:ok"

async def source14():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt") as response:
            lines = await response.text()
            for line in lines.split("\n"):
                if line.strip():
                    proxys.append(line.strip())
    return "s14:ok"


async def source15():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://raw.githubusercontent.com/tahaluindo/Free-Proxies/main/proxies/http.txt") as response:
            lines = await response.text()
            for line in lines.split("\n"):
                if line.strip():
                    proxys.append(line.strip())
    return "s15:ok"

async def source16():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://github.com/Zaeem20/FREE_PROXIES_LIST/blob/master/http.txt") as response:
            lines = await response.text()
            for line in lines.split("\n"):
                if line.strip():
                    proxys.append(line.strip())
    return "s16:ok"

async def source17():
    global proxys
    async with aiohttp.ClientSession() as session:
        async with session.get("https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt") as response:
            lines = await response.text()
            for line in lines.split("\n"):
                if line.strip():
                    proxys.append(line.strip())
    return "s17:ok"

async def main():
    global proxys
    with ThreadPoolExecutor(max_workers=20) as executor:
        tasks = []
        tasks.append(asyncio.ensure_future(source1()))
        tasks.append(asyncio.ensure_future(source2()))
        tasks.append(asyncio.ensure_future(source3()))
        tasks.append(asyncio.ensure_future(source4()))
        tasks.append(asyncio.ensure_future(source5()))
        tasks.append(asyncio.ensure_future(source6()))
        tasks.append(asyncio.ensure_future(source7()))
        tasks.append(asyncio.ensure_future(source8()))
        tasks.append(asyncio.ensure_future(source9()))
        tasks.append(asyncio.ensure_future(source10()))
        tasks.append(asyncio.ensure_future(source11()))
        tasks.append(asyncio.ensure_future(source12()))
        tasks.append(asyncio.ensure_future(source13()))
        tasks.append(asyncio.ensure_future(source14()))
        tasks.append(asyncio.ensure_future(source15()))
        tasks.append(asyncio.ensure_future(source16()))
        tasks.append(asyncio.ensure_future(source17()))

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
