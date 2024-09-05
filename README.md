# LinkedIn Job Scraper and Data Extractor

This repository contains two Python scripts that work in tandem to scrape job listings from LinkedIn and extract detailed job information. These scripts are intended for educational purposes to demonstrate web scraping, data extraction, and automation skills in Python.

## Table of Contents

1. [Overview](#overview)
2. [How It Works](#how-it-works)
   - [Script 1: Job Links Scraper](#script-1-job-links-scraper)
   - [Script 2: Job Data Extractor](#script-2-job-data-extractor)
3. [Setup and Installation](#setup-and-installation)
4. [Usage](#usage)
   - [Running the Job Links Scraper](#running-the-job-links-scraper)
   - [Running the Job Data Extractor](#running-the-job-data-extractor)
5. [Compliance and Ethical Considerations](#compliance-and-ethical-considerations)

## Overview

This project consists of two scripts:

1. **Job Links Scraper (`job_links_scraper.py`)**: Scrapes job links from LinkedIn based on specified criteria.
2. **Job Data Extractor (`job_data_extractor.py`)**: Uses the scraped links to fetch job descriptions and other details, and saves the extracted data in JSON format.

## How It Works

### Script 1: Job Links Scraper

The `job_links_scraper.py` script uses Selenium WebDriver to automate the browsing of LinkedIn job search results. It collects job links based on specific search criteria such as job title, location, experience level, and more. These links are stored in a CSV file (`analystlinks.csv`) for later use.

#### Key Features:

- Uses Selenium WebDriver to navigate LinkedIn job search pages.
- Automatically scrolls through job listings to load more results.
- Collects job links and saves them to `analystlinks.csv`.

### Script 2: Job Data Extractor

The `job_data_extractor.py` script reads the list of job links from `analystlinks.csv` and uses the `requests` library along with `BeautifulSoup` to fetch and parse job details from each link. The extracted information includes the job title, company name, location, job description, seniority level, employment type, job function, and industries.

#### Key Features:

- Reads job links from `analystlinks.csv`.
- Fetches the HTML content of each job link and extracts relevant details using BeautifulSoup.
- Implements error handling and retry mechanisms to handle request failures.
- Saves the extracted job details to `job_data.json`.

## Compliance and Ethical Considerations

### Disclaimer

This project is intended for **educational purposes only**. Scraping LinkedIn or any website without explicit permission is against their [terms of service](https://www.linkedin.com/legal/user-agreement). Using this script in production environments or for real-world applications may lead to account bans, IP blocking, or legal actions.

### Ethical Scraping Practices

1. **Randomized Delays**: This script employs random delays between actions to mimic human browsing behavior, reducing the likelihood of being flagged as a bot.
2. **Respecting Privacy**: No personally identifiable information (PII) is collected or stored by this script.
3. **Rate Limiting**: The script is designed to limit the number of requests to avoid overwhelming LinkedIn’s servers.

### Conclusion

Please use this script responsibly and only in environments where you have explicit permission to scrape or collect data. The author does not encourage or endorse scraping any website in violation of its terms of service.

