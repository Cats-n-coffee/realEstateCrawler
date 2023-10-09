# Real Estate Crawler

This project is for learning purposes only. It provides a basic way to get listing information for certain pages.

## Crawler
Each page has its own crawler. To start we're only using Remax since they don't seem to detect bots, therefore there doesn't seem to be a need to hide Selenium.<br>
The proxy in use is found on [this page](https://free-proxy-list.net/).
<br>
At the time of writing this line, each crawler saves data to memory before writing to a file after the Selenium instance has quit.