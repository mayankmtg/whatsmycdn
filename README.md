# [WhatsMyCDN]

WhatsMyCdn is a online utility to find out the name of the CDN provider of a domain name.

# This Project

This project is a CLI for whatsmycdn to determine if a website is CDN hosted or not

  - Sends GET request to the top 1000 [Alexa] domain names and websites
  - Finds if they have their content on any CDN platform.
  - Reports and saves to foundcdn.txt page.
  - The requests are multithreaded to optimise performance.
  - It involves many discrepencies since the website is not that accurate.

### Ongoing Task

Determine from multiple TOR exits if they have different domain name resolutions and if yes then report CDN else NOT_CDN

   [whatsmycdn]: <http://www.whatsmycdn.com>
   [alexa]: <https://www.alexa.com/topsites>
