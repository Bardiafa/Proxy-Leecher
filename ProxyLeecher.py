import asyncio
import aiohttp
import re
from bs4 import BeautifulSoup
from typing import List
import argparse
import json
import requests


class ProxyScraper:
    def __init__(self):
        self.total = 0

    async def scrape_proxies_async(self, url: str) -> List[str]:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            html = await response.text()
        lines = str(html).split('</script><br><div class="centeredProxyList">Free Http/Https Proxy List:</div><br><div class="centeredProxyList freeProxyStyle">')[1].split('</div><br><br><div class="centeredProxyList">Free Socks4 Proxy List:</div><br><div class="centeredProxyList freeProxyStyle">')[0]
        match = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]+\b",lines)
        lines = [line for line in match]
        return lines

    async def scrape_proxies_async2(self, url: str) -> List[str]:
     async with aiohttp.ClientSession() as session:
         response = await session.get(url)
         try:
             data = json.loads(await response.text())
         except json.JSONDecodeError:
             return []
     proxies = []
     for item in data["LISTA"]:
         ip = item["IP"]
         port = item["PORT"]
         loc = item["COUNTRY"]
         proxy = f"{ip}:{port}"
         proxies.append(proxy)
     return proxies

    async def scrape_proxies_async3(self, url: str) -> List[str]:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            html = await response.text()
        pattern = r"Free Http/Https Proxy List:</div><br><div class=\"centeredProxyList freeProxyStyle\">([\s\S]*?)</div><br><br><div class=\"centeredProxyList\">Free Socks4 Proxy List:</div>"
        match = re.search(pattern, html)
        proxies = []
        if match:
            proxy_list = match.group(1)
            pattern1 = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]+\b"
            matches = re.findall(pattern1, proxy_list)
            proxies = [matchh for matchh in matches]
        return proxies



    async def scrape_proxies_async4(self, url: str) -> List[str]:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            proxies = []
            regex = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}</td><td>\d+")
            for match in regex.findall(await response.text()):
                proxy = match.replace("</td><td>", ":")
                proxies.append(proxy)
            return proxies

    async def scrape_proxies_async5(self, self_, url: str) -> List[str]:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            soup = BeautifulSoup(await response.text(), "html.parser")
        script = soup.find("script", string=re.compile("document\.write\(Base64\.decode\("))
        proxies = []
        if script:
            ip_list = re.findall(r"document\.write\(Base64\.decode\(\"(.+?)\"\)", script.text)
            port_list = [str(span.text) for span in soup.select("span.fport")]
            proxy_list = [f"{bytes.fromhex(ip).decode('utf-8')}:{port_list[i]}" for i, ip in enumerate(ip_list)]
            proxies = proxy_list
        return proxies

    async def scrape_proxies(self, urls: List[str]) -> List[str]:
        proxies = []
        for url in urls:
            try:
                if "proxy-daily" in url:
                    new_proxies = await self.scrape_proxies_async(url)
                elif "spys.one" in url:
                    new_proxies = await self.scrape_proxies_async2(url)
                elif "premproxy.com" in url:
                    new_proxies = await self.scrape_proxies_async3(url)
                elif "sslproxies.org" in url:
                    new_proxies = await self.scrape_proxies_async4(url)
                elif "socks-proxy.net" in url:
                    new_proxies = await self.scrape_proxies_async5(self, url)                 
                else:
                    continue
                proxies.extend(new_proxies)
            except Exception as e:
                print(f"Error occurred while scraping {url}: {e}")
        return [proxy for proxy in proxies if proxy not in ('', None)]


    def run(self):
        parser = argparse.ArgumentParser(description="Scrape proxies from multiple websites.")
        parser.add_argument("output_file", type=str, help="File to save scraped proxies to.")
        parser.add_argument("--urls", nargs="+", type=str, default=[
        "https://www.proxy-daily.com/", "http://spys.one/en/anonymous-proxy-list/",
        "https://premproxy.com/list/free-https-ssl-proxy.htm", "https://www.sslproxies.org/",
        "https://www.socks-proxy.net/"], help="List of urls to scrape proxies from. Default: five proxy websites")
        args = parser.parse_args()
        loop = asyncio.get_event_loop()
        proxies = loop.run_until_complete(self.scrape_proxies(args.urls))
        with open(args.output_file, "w") as f:
            for proxy in proxies:
                f.write(proxy + "\n")
        print(f"Collected {len(proxies)} proxies and Saved them to {args.output_file} in /root")


if __name__ == "__main__":
    scraper = ProxyScraper()
    scraper.run()
