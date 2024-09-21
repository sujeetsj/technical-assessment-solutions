from typing import List, Dict, Callable

def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    grouped_data = {}

    for item in data:
        group_key = item.get(key)
        if group_key not in grouped_data:
            grouped_data[group_key] = []
        grouped_data[group_key].append(item)

    result = {}
    for group_key, group_items in grouped_data.items():
        result[group_key] = aggregator(group_items)

    return result

if __name__ == "__main__":
    data = [
        {"name": "Rahul", "age": 30, "city": "Mumbai"},
        {"name": "Priya", "age": 25, "city": "Delhi"},
        {"name": "Amit", "age": 35, "city": "Mumbai"},
        {"name": "Sneha", "age": 28, "city": "Bangalore"},
        {"name": "Vikram", "age": 32, "city": "Delhi"},
        {"name": "Neha", "age": 27, "city": "Bangalore"},
        {"name": "Rajesh", "age": 40, "city": "Mumbai"},
        {"name": "Anita", "age": 33, "city": "Delhi"},
    ]

    def average_age(items):
        return sum(item['age'] for item in items) / len(items)

    result = aggregate_data(data, "city", average_age)

    for city, avg_age in result.items():
        print(f"Average age in {city}: {avg_age:.2f}")