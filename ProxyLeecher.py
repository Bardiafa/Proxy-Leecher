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

async def source26():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s26:ok"
    except:
        return "s26:fail"
    
async def source27():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=2&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s27:ok"
    except:
        return "s27:fail"
    

async def source28():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=3&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s28:ok"
    except:
        return "s28:fail"
    
async def source29():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=4&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s29:ok"
    except:
        return "s29:fail"
    
async def source30():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=5&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s30:ok"
    except:
        return "s30:fail"
    
async def source31():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=6&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s31:ok"
    except:
        return "s31:fail"
    
async def source32():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=7&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s32:ok"
    except:
        return "s32:fail"
    
async def source33():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=8&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s33:ok"
    except:
        return "s33:fail"
    
async def source34():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=9&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s34:ok"
    except:
        return "s34:fail"
    
async def source35():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=10&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s35:ok"
    except:
        return "s35:fail"
    
async def source36():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=11&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s36:ok"
    except:
        return "s36:fail"
    
async def source37():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=12&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s37:ok"
    except:
        return "s37:fail"
    
async def source38():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=13&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s38:ok"
    except:
        return "s38:fail"
    
async def source39():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=14&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s39:ok"
    except:
        return "s39:fail"
    
async def source40():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=15&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s40:ok"
    except:
        return "s40:fail"
    
async def source41():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=16&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s41:ok"
    except:
        return "s41:fail"
    
async def source42():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=17&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s42:ok"
    except:
        return "s42:fail"
  
async def source43():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
            async with session.get(f"https://proxylist.geonode.com/api/proxy-list?limit=500&page=18&sort_by=lastChecked&sort_type=desc", headers=headers) as response:
                data = await response.json()
                for item in data["data"]:
                    proxys.add(f"{item['ip']}:{item['port']}")
        return "s43:ok"
    except:
        return "s43:fail"
    
async def source44():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s44:ok"
    except:
        return "s44:fail"
    
async def source45():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s45:ok"
    except:
        return "s45:fail"
    
async def source46():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s46:ok"
    except:
        return "s46:fail"
    

async def source47():
    global proxys
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt") as response:
                lines = await response.text()
                for line in lines.split("\n"):
                    if line.strip():
                        proxys.add(line.strip())
        return "s47:ok"
    except:
        return "s47:fail"


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
        tasks.append(asyncio.ensure_future(source26()))
        tasks.append(asyncio.ensure_future(source27()))
        tasks.append(asyncio.ensure_future(source28()))
        tasks.append(asyncio.ensure_future(source29()))
        tasks.append(asyncio.ensure_future(source30()))
        tasks.append(asyncio.ensure_future(source31()))
        tasks.append(asyncio.ensure_future(source32()))
        tasks.append(asyncio.ensure_future(source33()))
        tasks.append(asyncio.ensure_future(source34()))
        tasks.append(asyncio.ensure_future(source35()))
        tasks.append(asyncio.ensure_future(source36()))
        tasks.append(asyncio.ensure_future(source37()))
        tasks.append(asyncio.ensure_future(source38()))
        tasks.append(asyncio.ensure_future(source39()))
        tasks.append(asyncio.ensure_future(source40()))
        tasks.append(asyncio.ensure_future(source41()))
        tasks.append(asyncio.ensure_future(source42()))
        tasks.append(asyncio.ensure_future(source43()))
        tasks.append(asyncio.ensure_future(source44()))
        tasks.append(asyncio.ensure_future(source45()))
        tasks.append(asyncio.ensure_future(source46()))
        tasks.append(asyncio.ensure_future(source47()))

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
