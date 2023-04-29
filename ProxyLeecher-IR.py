import asyncio
import aiohttp
import re
from concurrent.futures import ThreadPoolExecutor
import os
import base64
import requests

proxys = set()

async def source1():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://free-proxy.cz/en/proxylist/country/IR/all/ping/all") as response:
                html = await response.text()
            for tr in re.findall(r'<tr.*?>(.*?)</tr>', html, re.DOTALL):
                ip_address_b64_match = re.search(r'Base64\.decode\("(.*?)"\)', tr)
                if ip_address_b64_match:
                    ip_address_b64 = ip_address_b64_match.group(1)
                    ip_address = base64.b64decode(ip_address_b64).decode('utf-8')
                    port = re.search(r'<span class="fport".*?>(.*?)</span>', tr).group(1)
                    proxys.add(f"{ip_address}:{port}")
        return "s1:ok"
    except:
        return "s1:fail"
    
async def source2():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://free-proxy.cz/en/proxylist/country/IR/all/ping/all/2") as response:
                html = await response.text()
            for tr in re.findall(r'<tr.*?>(.*?)</tr>', html, re.DOTALL):
                ip_address_b64_match = re.search(r'Base64\.decode\("(.*?)"\)', tr)
                if ip_address_b64_match:
                    ip_address_b64 = ip_address_b64_match.group(1)
                    ip_address = base64.b64decode(ip_address_b64).decode('utf-8')
                    port = re.search(r'<span class="fport".*?>(.*?)</span>', tr).group(1)
                    proxys.add(f"{ip_address}:{port}")
        return "s2:ok"
    except:
        return "s2:fail"

async def source3():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://free-proxy.cz/en/proxylist/country/IR/all/ping/all/3") as response:
                html = await response.text()
            for tr in re.findall(r'<tr.*?>(.*?)</tr>', html, re.DOTALL):
                ip_address_b64_match = re.search(r'Base64\.decode\("(.*?)"\)', tr)
                if ip_address_b64_match:
                    ip_address_b64 = ip_address_b64_match.group(1)
                    ip_address = base64.b64decode(ip_address_b64).decode('utf-8')
                    port = re.search(r'<span class="fport".*?>(.*?)</span>', tr).group(1)
                    proxys.add(f"{ip_address}:{port}")
        return "s3:ok"
    except:
        return "s3:fail"

async def source4():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://hidemy.name/en/proxy-list/countries/iran/", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}) as response:
                html = await response.content.read()
                html = html.decode('iso-8859-1')
                matches = re.findall(r"<tr><td>(?P<ip>\b(?:[0-9]{1,3}\.){3}[0-9]{1,3})<\/td><td>(?P<port>\d+)<\/td>" , html)
                for line in matches:
                    proxys.add(f"{line[0]}:{line[1]}")
        return "s4:ok"
    except:
        return "s4:fail"

async def source5():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            for page in range(304):
                async with session.get(f"https://www.freeproxy.world/?type=&anonymity=&country=IR&speed=&port=&page={page}") as response:
                    html = await response.text()
                    ip_pattern = r"<td class=\"show-ip-div\">\s*(?P<ip>(?:\d{1,3}\.){3}\d{1,3})\s*<\/td>"
                    port_pattern = r"<a href=\"\/\?port=(?P<port>\d+)\">" 
                    ip_match = re.findall(ip_pattern, html)
                    port_match = re.findall(port_pattern, html)
                    for ip, port in zip(ip_match, port_match):
                        proxys.add(f"{ip}:{port}")
        return "s5:ok"
    except:
        return "s5:fail"

async def source6():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://freeproxylist.cc/online/Iran/") as response:
                html = await response.text()
                pattern = r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\D+(\d+)\b'
                ip_port_list = re.findall(pattern, html)
    
                for ip_port in ip_port_list:
                    proxys.add(':'.join(ip_port))
        return "s6:ok"
    except:
        return "s6:fail"
    
async def source7():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.freeproxy.world/?country=IR") as response:
                html = await response.text()
                pattern = r'<td class="show-ip-div">\s*(\d+\.\d+\.\d+\.\d+)\s*</td>\s*<td>\s*<a href="/\?port=(\d+)">'
                ip_port_list = re.findall(pattern, html)
                for ip_port in ip_port_list:
                    proxys.add(f"{ip_port[0]}:{ip_port[1]}")
        return "s7:ok"
    except:
        return "s7:fail"

async def source8():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.freeproxy.world/?type=&anonymity=&country=IR&speed=&port=&page=2") as response:
                html = await response.text()
                pattern = r'<td class="show-ip-div">\s*(\d+\.\d+\.\d+\.\d+)\s*</td>\s*<td>\s*<a href="/\?port=(\d+)">'
                ip_port_list = re.findall(pattern, html)
                for ip_port in ip_port_list:
                    proxys.add(f"{ip_port[0]}:{ip_port[1]}")
        return "s8:ok"
    except:
        return "s8:fail"
    
async def source9():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.freeproxy.world/?type=&anonymity=&country=IR&speed=&port=&page=3") as response:
                html = await response.text()
                pattern = r'<td class="show-ip-div">\s*(\d+\.\d+\.\d+\.\d+)\s*</td>\s*<td>\s*<a href="/\?port=(\d+)">'
                ip_port_list = re.findall(pattern, html)
                for ip_port in ip_port_list:
                    proxys.add(f"{ip_port[0]}:{ip_port[1]}")
        return "s9:ok"
    except:
        return "s9:fail"

async def source10():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.freeproxy.world/?type=&anonymity=&country=IR&speed=&port=&page=4") as response:
                html = await response.text()
                pattern = r'<td class="show-ip-div">\s*(\d+\.\d+\.\d+\.\d+)\s*</td>\s*<td>\s*<a href="/\?port=(\d+)">'
                ip_port_list = re.findall(pattern, html)
                for ip_port in ip_port_list:
                    proxys.add(f"{ip_port[0]}:{ip_port[1]}")
        return "s10:ok"
    except:
        return "s10:fail"
    
async def source11():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.freeproxy.world/?type=&anonymity=&country=IR&speed=&port=&page=5") as response:
                html = await response.text()
                pattern = r'<td class="show-ip-div">\s*(\d+\.\d+\.\d+\.\d+)\s*</td>\s*<td>\s*<a href="/\?port=(\d+)">'
                ip_port_list = re.findall(pattern, html)
                for ip_port in ip_port_list:
                    proxys.add(f"{ip_port[0]}:{ip_port[1]}")
        return "s11:ok"
    except:
        return "s11:fail"
    
async def source12():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.freeproxy.world/?type=&anonymity=&country=IR&speed=&port=&page=6") as response:
                html = await response.text()
                pattern = r'<td class="show-ip-div">\s*(\d+\.\d+\.\d+\.\d+)\s*</td>\s*<td>\s*<a href="/\?port=(\d+)">'
                ip_port_list = re.findall(pattern, html)
                for ip_port in ip_port_list:
                    proxys.add(f"{ip_port[0]}:{ip_port[1]}")
        return "s12:ok"
    except:
        return "s12:fail"

async def source13():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://proxyhub.me/en/ir-http-proxy-list.html") as response:
                html = await response.text()
                regex = r'<td>(\d+\.\d+\.\d+\.\d+)</td><td>(\d+)</td>'
                matches = re.findall(regex, html)
                result = [f"{match[0]}:{match[1]}" for match in matches]              
                proxys.add('\n'.join(result))
        return "s13:ok"
    except:
        return "s13:fail"

async def source14():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://proxyhub.me/en/ir-https-proxy-list.html") as response:
                html = await response.text()
                regex = r'<td>(\d+\.\d+\.\d+\.\d+)</td><td>(\d+)</td>'
                matches = re.findall(regex, html)
                result = [f"{match[0]}:{match[1]}" for match in matches]              
                proxys.add('\n'.join(result))
        return "s14:ok"
    except:
        return "s14:fail"
    
async def source15():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://proxyranker.com/iran_islamic_republic_of/") as response:
                html = await response.text()
                pattern = r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})<\/td><td><span title="Proxy port">(\d+)<\/span><\/td>'
                matches = re.findall(pattern, html)

                for match in matches:
                    proxys.add(f'{match[0]}:{match[1]}')
        return "s15:ok"
    except:
        return "s15:fail"
    
async def source16():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&country=IR", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s16:ok"
    except:
        return "s16:fail"

async def source17():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=2&sort_by=lastChecked&sort_type=desc&country=IR", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s17:ok"
    except:
        return "s17:fail"
  
async def main():
    global proxys
    with ThreadPoolExecutor(max_workers=8) as executor:
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
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for result in results:
            if isinstance(result, Exception):
                print("Error:", result)
            else:
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