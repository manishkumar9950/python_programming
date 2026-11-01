# 🐍 Python Fundamentals & Problem-Solving Mastery

A structured repository showcasing fundamental-to-advanced Python programming, data structures implementation, algorithmic problem solving, and hands-on coding challenges.

---

## 📌 Repository Overview

This repository documents my journey and solutions in Python programming, covering foundational concepts, core collection methods, competitive coding practice, and university test problems.

### 🎯 Key Focus Areas
- **Core Fundamentals:** Variables, data types, type casting, arithmetic & logical operators, operator precedence.
- **Control Flow:** `if-elif-else` branching, nested conditionals, boundary test evaluations.
- **Iteration & Loops:** `for` and `while` loops, range generation, loop-else clauses, jumping statements (`break`, `continue`).
- **Data Collections & Methods:** 
  - `List`: Slicing, mutation, searching, nested list matrix operations.
  - `Tuple`: Packing, unpacking, immutability, coordinates/record modeling.
  - `Set`: Mathematical operations (union, intersection, difference, symmetric difference), uniqueness filters.
  - `Dictionary`: Key-value hashing, lookups, aggregation with `setdefault()`, manipulation.
- **Algorithmic Problem Solving:** Standard interview & algorithmic challenges (Two Sum, Stock Buy & Sell, Roman to Integer, Palindrome check, FizzBuzz).

---

## 📂 Repository Structure

```text
├── 01_Fundamentals/
│   ├── basic_io_and_operators.py
│   ├── type_casting.py
│   └── operator_precedence.py
│
├── 02_Conditionals/
│   ├── grade_evaluator.py
│   ├── leap_year_check.py
│   └── triangle_classifier.py
│
├── 03_Loops_and_Patterns/
│   ├── number_patterns.py
│   ├── fibonacci_series.py
│   ├── prime_hcf_lcm.py
│   └── digit_manipulations.py
│
├── 04_Data_Structures/
│   ├── lists_operations.py
│   ├── tuples_records.py
│   ├── sets_operations.py
│   └── dictionary_mapping.py
│
└── 05_Problem_Solving_Challenges/
    ├── fizz_buzz.py
    ├── palindrome_number.py
    ├── contains_duplicate.py
    ├── two_sum.py
    ├── best_time_to_buy_sell_stock.py
    └── roman_to_integer.py
```

---

## 🚀 Featured Problem-Solving Challenges

| # | Problem | Key Concept | Time Complexity |
|---|---|---|:---:|
| 01 | **FizzBuzz** | Conditional evaluation, modulo arithmetic | $O(n)$ |
| 02 | **Palindrome Number** | Integer arithmetic without full string casting | $O(\log_{10} n)$ |
| 03 | **Contains Duplicate** | Hash sets vs list traversal | $O(n)$ |
| 04 | **Two Sum** | Hash mapping / single-pass lookup | $O(n)$ |
| 05 | **Best Time to Buy & Sell Stock** | Greedy one-pass tracking minimum buy price | $O(n)$ |
| 06 | **Roman to Integer** | Reverse traversal / value subtraction logic | $O(n)$ |

---

## 🛠️ How to Run Locally

### Prerequisites
- Python 3.8 or higher installed on your machine.

### Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### Run Any Script
```bash
python 05_Problem_Solving_Challenges/two_sum.py
```

---

## 📈 Key Takeaways & Best Practices Learned

1. **Object References & Mutability:** Understanding in-place alterations vs slicing/shallow copy (`b = a` vs `b = a.copy()` / `b = a[:]`).
2. **Lookup Efficiency:** Leveraging dictionaries and sets for $O(1)$ average time lookups over linear list scans ($O(n)$).
3. **Clean Code Principles:** Avoiding unnecessary nested loops and writing readable, idiomatic Python solutions.

---

## 👤 Author

- **GitHub:** [@your-username](https://github.com/your-username)
- **Profile:** CS & Python Enthusiast

---

## 📝 License

This project is licensed under the MIT License - feel free to use it for practice and learning.