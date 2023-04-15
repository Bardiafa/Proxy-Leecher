# 🔎🌐 Fastest-Proxy-Leecher

Proxy-Leecher is a Python script that scrapes and collects free HTTP/HTTPS proxies from multiple websites. 🕵️‍♂️ The scraped proxies are saved to a text file which can then be used with other tools.

## 💻 Usage
To use Proxy-Leecher, you need to have Python 3 installed on your system. You also need to install the required dependencies by running `pip install requests BeautifulSoup aiohttp `.

Then, run the script using the following command:

	python proxy-leecher.py output_file [--urls url1 url2 ...] 

Here, `output_file` is the path to the file where the scraped proxies will be saved. If not specified, the proxies will be saved to `proxies.txt` in the same directory as the script.

You can also specify a list of URLs to scrape proxies from using the `--urls` option. By default, the script scrapes proxies from five popular proxy websites.

## 📝 Example
To scrape proxies from the default list of websites and save them to a file named `my_proxies.txt`, run the following command:

	python proxy-leecher.py my_proxies.txt 

The scraped proxies will be saved to `my_proxies.txt` in the same directory as the script.

## 🤝 Disclaimer
Please note that using free public proxies comes with certain risks such as security vulnerabilities, slow speed, and unreliable connections. Use these proxies at your own risk and responsibility.

## 📄 License
This project is licensed under the [MIT License](https://github.com/Bardiafa/Proxy-Leecher/blob/main/LICENSE).

## 👨‍💻 Author

This script was created by [Me](https://github.com/Bardiafa) & [Hossein](https://github.com/hossein-mohseni) in Collaboration in our Wonderful Team [Mizegerd.tech](https://github.com/mizegerd-tech). If you have any questions or suggestions, please feel free to contact us in [Issues](https://github.com/Bardiafa/Proxy-Checker/issues) Part!

-------

So what are you waiting for? Start leeching those proxies today! 😎
