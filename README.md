# Technical Assessment Solutions

This repository contains my solutions to the Software Engineer Technical Assessment. The assessment covers various aspects of Python programming, including web scraping, data cleaning, Django, concurrency, and algorithms.

## Project Structure

```
technical-assessment-solutions/
├── q1_web_scraper.py
├── q2_csv_cleaner.py
├── q3_django_top_customers/
│   ├── manage.py
│   ├── top_customers_project/
│   └── top_customers_app/
├── q4_rate_limiter.py
├── q5_data_aggregator.py
├── q6_find_duplicate.py
├── input_data.csv
├── README.md
└── requirements.txt
```

## Solutions Overview

1. **Web Scraper** (q1_web_scraper.py): 
   - Scrapes article titles, URLs, and dates from Indian Express.
   - Uses BeautifulSoup and requests libraries.

2. **CSV Cleaner** (q2_csv_cleaner.py):
   - Cleans CSV data by removing duplicates and filtering out invalid entries.
   - Handles email validation and timestamp-based selection.

3. **Django Top Customers** (q3_django_top_customers/):
   - Django application that implements a method to get the top 5 customers who have spent the most in the last 6 months.

4. **Rate Limiter** (q4_rate_limiter.py):
   - Implements a thread-safe rate limiter that limits the number of requests a user can make within a given time window.

5. **Data Aggregator** (q5_data_aggregator.py):
   - Custom function that aggregates data from a list of dictionaries based on a specified key and aggregator function.

6. **Find Duplicate** (q6_find_duplicate.py):
   - Algorithm to find a duplicate number in an array with O(1) extra space complexity.

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/sujeetsj/technical-assessment-solutions.git
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

## Running the Solutions

1. Web Scraper:
   ```
   python q1_web_scraper.py
   ```

2. CSV Cleaner:
   ```
   python q2_csv_cleaner.py
   ```

3. Django Top Customers:
   ```
   cd q3_django_top_customers
   python manage.py migrate
   python manage.py runserver
   ```
   Then visit `http://127.0.0.1:8000/` in your web browser.

4. Rate Limiter:
   ```
   python q4_rate_limiter.py
   ```

5. Data Aggregator:
   ```
   python q5_data_aggregator.py
   ```

6. Find Duplicate:
   ```
   python q6_find_duplicate.py
   ```

## Notes

- Make sure you have Python 3.7+ installed on your system.
- The Django project (Q3) may require additional setup. Please refer to the Django documentation for more information.
- The `input_data.csv` file is provided for testing the CSV cleaner (Q2).

## Contact

If you have any questions or need further clarification, please feel free to contact me at sujeetyadav02222@gmail.com.

Thank you for reviewing my technical assessment solutions!
