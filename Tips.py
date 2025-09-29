import csv
from collections import defaultdict

CSV_PATH = r"c:\Users\Aissatou Ndiaye\Downloads\tips.csv"

def compute_time_percentages(csv_path):
    counts = defaultdict(int)
    total = 0

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            t = row.get('time')
            if t is None:
                continue
            counts[t] += 1
            total += 1

    percentages = {}
    for k, v in counts.items():
        percentages[k] = (v / total) * 100 if total > 0 else 0.0
    return counts, percentages, total

if __name__ == '__main__':
    counts, percentages, total = compute_time_percentages(CSV_PATH)

    print(f"Total responses: {total}")
    for k in sorted(counts.keys()):
        print(f"{k}: count = {counts[k]}, percent = {percentages[k]:.2f}%")

    # Also print only Dinner and Lunch explicitly
    for key in ['Dinner', 'Lunch']:
        c = counts.get(key, 0)
        p = percentages.get(key, 0.0)
        print(f"\n{key} -> count: {c}, percent: {p:.2f}%")

Total responses: 244
Dinner: count = 176, percent = 72.13%
Lunch: count = 68, percent = 27.87%

Dinner -> count: 176, percent: 72.13%

Lunch -> count: 68, percent: 27.87%
