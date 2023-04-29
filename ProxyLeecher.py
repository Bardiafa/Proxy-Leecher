import asyncio
import aiohttp
import re
import json
from concurrent.futures import ThreadPoolExecutor
import os

proxys = set()

async def source1():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.proxy-daily.com/") as response:
                html = await response.text()
            lines = str(html).split('</script><br><div class="centeredProxyList">Free Http/Https Proxy List:</div><br><div class="centeredProxyList freeProxyStyle">')[1].split('</div><br><br><divclass="centeredProxyList">Free Socks4 Proxy List:</div><br><div class="centeredProxyList freeProxyStyle">')[0]
            match = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]+\b",lines)
            lines = [line for line in match]
            proxys.update(lines)
        return "s1:ok"
    except:
        return "s1:error"

async def source2():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.sslproxies.org/") as response:
                html = await response.text()
            lines = str(html).split('<tbody>')[1].split('</tbody>')[0]
            match = re.findall(r"<tr><td>(?P<ip>\b(?:[0-9]{1,3}\.){3}[0-9]{1,3})<\/td><td>(?P<port>\d+)<\/td><td>\w+<\/td><td class='hm'>(?P<country>\w+|\w+ \w+)<\/td><td>",lines)
            for line in match:
                proxys.add(f"{line[0]}:{line[1]}")
        return "s2:ok"
    except:
        return "s2:error"

async def source3():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all") as response:
                html = str(await response.text()).splitlines()
            for line in html:
                proxys.add(line)
        return "s3:ok"
    except:
        return "s3:error"

async def source4():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://hidemy.name/en/proxy-list/", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}) as response:
                html = await response.content.read()
                html = html.decode('iso-8859-1')
                matches = re.findall(r"<tr><td>(?P<ip>\b(?:[0-9]{1,3}\.){3}[0-9]{1,3})<\/td><td>(?P<port>\d+)<\/td>" , html)
                for line in matches:
                    proxys.add(f"{line[0]}:{line[1]}")
        return "s4:ok"
    except:
        return "s4:error"

async def source5():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.proxy-list.download/HTTP", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}) as response:
                html = await response.text()
                matches = re.findall(r"<tr>\s+<td>\s+(?P<ip>.*?)\s+<\/td>\s+<td>\s+(?P<port>\d+)\s+<\/td>" , html)
                for line in matches:
                    proxys.add(f"{line[0]}:{line[1]}")
        return "s5:ok"
    except:
        return "s5:error"

async def source6():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://us-proxy.org/") as response:
                html = await response.text()
                lines = str(html).split('<tbody>')[1].split('</tbody>')[0]
                match = re.findall(r"<tr><td>(?P<ip>\b(?:[0-9]{1,3}\.){3}[0-9]{1,3})<\/td><td>(?P<port>\d+)<\/td><td>\w+<\/td><td class='hm'>(?P<country>\w+|\w+ \w+)<\/td><td>",lines)
                for line in match:
                    proxys.add(f"{line[0]}:{line[1]}")
        return "s6:ok"
    except:
        return "s6:error"

async def source7():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.proxy-list.download/api/v2/get?l=en&t=https") as response:
                html = await response.text()
                lines = json.loads(html)['LISTA']
                for i in lines:
                    proxys.add(f"{i['IP']}:{i['PORT']}")
        return "s7:ok"
    except:
        return "s7:error"

async def source8():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            for page in range(500):
                async with session.get(f"https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page={page}") as response:
                    html = await response.text()
                    ip_pattern = r"<td class=\"show-ip-div\">\s*(?P<ip>(?:\d{1,3}\.){3}\d{1,3})\s*<\/td>"
                    port_pattern = r"<a href=\"\/\?port=(?P<port>\d+)\">"

                    ip_match = re.findall(ip_pattern, html)
                    port_match = re.findall(port_pattern, html)
                    for ip, port in zip(ip_match, port_match):
                        proxys.add(f"{ip}:{port}")
        return "s8:ok"
    except:
        return "s8:fail"

async def source9():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s9:ok"
    except:
        return "s9:fail"

async def source10():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s10:ok"
    except:
        return "s10:fail"

async def source11():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s11:ok"
    except:
        return "s11:fail"

async def source12():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/fahimscirex/proxybd/master/anonymous-proxylist/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s12:ok"
    except:
        return "s12:fail"


async def source13():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s13:ok"
    except:
        return "s13:fail"

async def source14():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s14:ok"
    except:
        return "s14:fail"


async def source15():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/tahaluindo/Free-Proxies/main/proxies/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s15:ok"
    except:
        return "s15:fail"

async def source16():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s16:ok"
    except:
        return "s16:fail"


async def source17():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s17:ok"
    except:
        return "s17:fail"

async def source18():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s18:ok"
    except:
        return "s18:fail"

async def source19():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s19:ok"
    except:
        return "s19:fail"
    
async def source20():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s20:ok"
    except:
        return "s20:fail"
async def source21():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s21:ok"
    except:
        return "s21:fail"
    
async def source22():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s22:ok"
    except:
        return "s22:fail"
async def source23():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s23:ok"
    except:
        return "s23:fail"

async def source24():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s24:ok"
    except:
        return "s24:fail"

async def source25():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s25:ok"
    except:
        return "s25:fail"

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
        tasks.append(asyncio.ensure_future(source18()))
        tasks.append(asyncio.ensure_future(source19()))
        tasks.append(asyncio.ensure_future(source20()))
        tasks.append(asyncio.ensure_future(source21()))
        tasks.append(asyncio.ensure_future(source22()))
        tasks.append(asyncio.ensure_future(source23()))
        tasks.append(asyncio.ensure_future(source24()))
        tasks.append(asyncio.ensure_future(source25()))

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
