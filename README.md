# Gale-Shapley Residency Matching Algorithm with MySQL and Python

## Overview

This project implements the Gale-Shapley algorithm to solve the Stable Marriage Problem, specifically applied to match medical students with residency programs. It uses Python for the backend logic and MySQL for data storage and retrieval.

## Features

* Utilizes the Gale-Shapley algorithm for stable matching.
* Customizable criteria for student and residency program rankings.
* Efficient MySQL database schema for easy data manipulation.
* Flexible Python codebase that can be adapted to other matching problems.

## Prerequisites

* Python 3.x
* MySQL
* Python libraries: mysql-connector-python
* Faker Library (if you're adding fake data)

## Installation

1. Clone the repository to your local machine.
2. Install the required Python libraries.

`pip install -r requirements.txt`

3. Set up the MySQL database and tables using the provided SQL scripts.

## How to Run

1. Fill the students and residency_programs tables in the MySQL database with your data.
2. Update database connection information in config.py.
3. Run the main script to start the matching process.

`python main.py`

## Database Schema

### Students Table

* student_id
* student_name
* specialty_interest

### Residency_Programs Table

* program_id
* program_name
* location
* specialty

### Rankings Table

* rank_id
* student_id
* program_id
* rank

## Usage Example

After running the program, you can query the MySQL database to see the final stable matches. Example:

`SELECT * FROM final_matches;`