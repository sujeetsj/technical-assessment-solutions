# Technical Assessment Solutions

This repository contains solutions to a technical assessment for a Software Engineer position. The assessment covers various aspects of Python programming, including web scraping, data cleaning, Django, concurrency, and algorithms.

## Solutions

1. **Web Scraper** (q1_web_scraper.py): A script that scrapes article titles and URLs from a news website using BeautifulSoup and requests.

2. **CSV Cleaner** (q2_csv_cleaner.py): A script that cleans CSV data by removing duplicates and filtering out invalid entries.

3. **Django Top Customers** (q3_django_top_customers/): A Django application that implements a method to get the top 5 customers who have spent the most in the last 6 months.

4. **Rate Limiter** (q4_rate_limiter.py): A thread-safe implementation of a rate limiter that limits the number of requests a user can make within a given time window.

5. **Data Aggregator** (q5_data_aggregator.py): A custom function that aggregates data from a list of dictionaries based on a specified key and aggregator function.

6. **Find Duplicate** (q6_find_duplicate.py): An algorithm to find a duplicate number in an array with O(1) extra space complexity.

## Setup and Usage

1. Clone the repository:
   ```
   git clone https://github.com/your-username/technical-assessment-solutions.git
   cd technical-assessment-solutions
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run individual scripts as needed, for example:
   ```
   python q1_web_scraper.py
   ```

5. For the Django application (q3), additional setup may be required. Refer to the Django documentation for more information.

## Note

This code is part of a technical assessment and is provided for demonstration purposes. Some scripts may require additional configuration or dependencies to run properly in your environment.
