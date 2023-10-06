from faker import Faker
import random
import json
import mysql.connector

# Initialize Faker and data
fake = Faker()
students = []
residency_programs_final = []
rankings = []
matches = []

# Don't forget to run mysql.server start before running this script.

# Connect to MySQL.
mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password"
)

# Create a "cursor" to run SQL commands
my_cursor = mydb.cursor()

# Create a new database if it doesn't already exist.
# my_cursor.execute("CREATE DATABASE mydatabase")

# Use the new database
my_cursor.execute("USE mydatabase")

# Delete a table if it already exists.
my_cursor.execute("DROP TABLE IF EXISTS Students")
my_cursor.execute("DROP TABLE IF EXISTS Residency_Programs")
my_cursor.execute("DROP TABLE IF EXISTS Rankings")
my_cursor.execute("DROP TABLE IF EXISTS Matches")

# Create a new table if it doesn't already exist.
my_cursor.execute(
    """
                    CREATE TABLE Students (
                        student_id INT AUTO_INCREMENT,
                        first_name VARCHAR(255),
                        last_name VARCHAR(255),
                        email VARCHAR(255),
                        gpa FLOAT,
                        specialty VARCHAR(255),
                        PRIMARY KEY (student_id)
                    );
    """
)

my_cursor.execute(
    """
                    CREATE TABLE Residency_Programs (
                        program_id INT AUTO_INCREMENT,
                        program_name VARCHAR(255),
                        specialty VARCHAR(255),
                        location VARCHAR(255),
                        capacity INT,
                        PRIMARY KEY (program_id)
                    );
    """
)

my_cursor.execute(
    """
                    CREATE TABLE Rankings (
                        rank_id INT AUTO_INCREMENT,
                        student_id INT,
                        program_id INT,
                        ranking INT,
                        PRIMARY KEY (rank_id)
                    );
    """
)

my_cursor.execute(
    """
                    CREATE TABLE Matches (
                        match_id INT AUTO_INCREMENT,
                        student_id INT,
                        program_id INT,
                        PRIMARY KEY (match_id)
                    );
    """
)

# List of medical specialties
medical_specialties = [
    "Anesthesiology",
    "Cardiology",
    "Dermatology",
    "Emergency Medicine",
    "Endocrinology",
    "Family Medicine",
    "Gastroenterology",
    "General Surgery",
    "Geriatrics",
    "Hematology",
    "Infectious Disease",
    "Internal Medicine",
    "Nephrology",
    "Neurology",
    "Neurosurgery",
    "Obstetrics and Gynecology",
    "Oncology",
    "Ophthalmology",
    "Orthopedic Surgery",
    "Otolaryngology",
    "Pathology",
    "Pediatrics",
    "Plastic Surgery",
    "Psychiatry",
    "Pulmonology",
    "Radiology",
    "Rheumatology",
    "Urology",
    "Vascular Surgery",
    "Allergy and Immunology",
    "Critical Care Medicine",
    "Physical Medicine and Rehabilitation",
    "Addiction Medicine",
    "Nuclear Medicine",
    "Palliative Care",
    "Pain Medicine",
    "Sports Medicine",
    "Thoracic Surgery",
    "Transplant Surgery",
    "Trauma Surgery",
    "Occupational Medicine",
    "Forensic Medicine",
    "Sleep Medicine",
    "Neonatology",
    "Child and Adolescent Psychiatry",
    "Maternal-Fetal Medicine",
    "Reproductive Endocrinology and Infertility",
    "Interventional Radiology",
    "Hand Surgery",
    "Oral and Maxillofacial Surgery",
    "Colorectal Surgery",
    "Cardiothoracic Surgery"
]

residency_programs = [
    {
        "program_name": "Harborview Medical Center",
        "location": "Seattle, WA",
        "specialty": "Emergency Medicine"
    },
    {
        "program_name": "Johns Hopkins Hospital",
        "location": "Baltimore, MD",
        "specialty": "Cardiology"
    },
    {
        "program_name": "Mayo Clinic",
        "location": "Rochester, MN",
        "specialty": "Gastroenterology"
    },
    {
        "program_name": "Massachusetts General Hospital",
        "location": "Boston, MA",
        "specialty": "Neurosurgery"
    },
    {
        "program_name": "Cleveland Clinic",
        "location": "Cleveland, OH",
        "specialty": "Orthopedic Surgery"
    },
    {
        "program_name": "Brigham and Women's Hospital",
        "location": "Boston, MA",
        "specialty": "Internal Medicine"
    },
    {
        "program_name": "Stanford Health Care",
        "location": "Stanford, CA",
        "specialty": "Anesthesiology"
    },
    {
        "program_name": "UCLA Medical Center",
        "location": "Los Angeles, CA",
        "specialty": "Psychiatry"
    },
    {
        "program_name": "Mount Sinai Hospital",
        "location": "New York, NY",
        "specialty": "Pathology"
    },
    {
        "program_name": "UCSF Medical Center",
        "location": "San Francisco, CA",
        "specialty": "Radiology"
    },
    {
        "program_name": "NewYork-Presbyterian",
        "location": "New York, NY",
        "specialty": "Oncology"
    },
    {
        "program_name": "Northwestern Memorial Hospital",
        "location": "Chicago, IL",
        "specialty": "Nephrology"
    },
    {
        "program_name": "Vanderbilt University Medical Center",
        "location": "Nashville, TN",
        "specialty": "Otolaryngology"
    },
    {
        "program_name": "Houston Methodist Hospital",
        "location": "Houston, TX",
        "specialty": "Urology"
    },
    {
        "program_name": "University of Michigan Hospitals",
        "location": "Ann Arbor, MI",
        "specialty": "Pulmonology"
    },
    {
        "program_name": "Duke University Hospital",
        "location": "Durham, NC",
        "specialty": "Plastic Surgery"
    },
    {
        "program_name": "UPMC Presbyterian Shadyside",
        "location": "Pittsburgh, PA",
        "specialty": "Rheumatology"
    },
    {
        "program_name": "Yale New Haven Hospital",
        "location": "New Haven, CT",
        "specialty": "Endocrinology"
    },
    {
        "program_name": "Barnes-Jewish Hospital",
        "location": "St. Louis, MO",
        "specialty": "Vascular Surgery"
    },
    {
        "program_name": "University of Colorado Hospital",
        "location": "Aurora, CO",
        "specialty": "Family Medicine"
    },
    {
        "program_name": "Mercy General Hospital",
        "location": "Sacramento, CA",
        "specialty": "Geriatrics"
    },
    {
        "program_name": "Georgetown University Hospital",
        "location": "Washington, D.C.",
        "specialty": "Obstetrics and Gynecology"
    },
    {
        "program_name": "Baylor University Medical Center",
        "location": "Dallas, TX",
        "specialty": "Hematology"
    },
    {
        "program_name": "Children's Hospital of Philadelphia",
        "location": "Philadelphia, PA",
        "specialty": "Pediatrics"
    },
    {
        "program_name": "Boston Children's Hospital",
        "location": "Boston, MA",
        "specialty": "Pediatrics"
    },
    {
        "program_name": "Emory University Hospital",
        "location": "Atlanta, GA",
        "specialty": "Infectious Disease"
    },
    {
        "program_name": "Virginia Mason Medical Center",
        "location": "Seattle, WA",
        "specialty": "Gastroenterology"
    },
    {
        "program_name": "Scripps Mercy Hospital",
        "location": "San Diego, CA",
        "specialty": "Family Medicine"
    },
    {
        "program_name": "Orlando Health",
        "location": "Orlando, FL",
        "specialty": "Emergency Medicine"
    },
    {
        "program_name": "University of Wisconsin Hospital",
        "location": "Madison, WI",
        "specialty": "Endocrinology"
    },
    {
        "program_name": "Henry Ford Hospital",
        "location": "Detroit, MI",
        "specialty": "Pulmonology"
    },
    {
        "program_name": "Cedars-Sinai Medical Center",
        "location": "Los Angeles, CA",
        "specialty": "Cardiology"
    },
    {
        "program_name": "Indiana University Health",
        "location": "Indianapolis, IN",
        "specialty": "Nephrology"
    },
    {
        "program_name": "Beth Israel Deaconess Medical Center",
        "location": "Boston, MA",
        "specialty": "Rheumatology"
    },
    {
        "program_name": "Rush University Medical Center",
        "location": "Chicago, IL",
        "specialty": "Orthopedic Surgery"
    },
    {
        "program_name": "University of Florida Health",
        "location": "Gainesville, FL",
        "specialty": "Urology"
    },
    {
        "program_name": "Thomas Jefferson University Hospitals",
        "location": "Philadelphia, PA",
        "specialty": "Ophthalmology"
    },
    {
        "program_name": "Banner University Medical Center",
        "location": "Phoenix, AZ",
        "specialty": "Psychiatry"
    },
    {
        "program_name": "Wake Forest Baptist Medical Center",
        "location": "Winston-Salem, NC",
        "specialty": "Plastic Surgery"
    },
    {
        "program_name": "Tufts Medical Center",
        "location": "Boston, MA",
        "specialty": "Dermatology"
    },
    {
        "program_name": "Southern Memorial Hospital",
        "location": "Atlanta, GA",
        "specialty": "Oncology"
    },
    {
        "program_name": "Rocky Mountain Health Center",
        "location": "Denver, CO",
        "specialty": "Emergency Medicine"
    },
    {
        "program_name": "Riverside General Hospital",
        "location": "Riverside, CA",
        "specialty": "General Surgery"
    },
    {
        "program_name": "Lakeshore University Hospital",
        "location": "Chicago, IL",
        "specialty": "Anesthesiology"
    },
    {
        "program_name": "Gulf Coast Medical Center",
        "location": "Houston, TX",
        "specialty": "Cardiology"
    },
    {
        "program_name": "Twin Cities Medical Center",
        "location": "Minneapolis, MN",
        "specialty": "Endocrinology"
    },
    {
        "program_name": "Golden Gate Healthcare",
        "location": "San Francisco, CA",
        "specialty": "Psychiatry"
    },
    {
        "program_name": "Liberty Medical University",
        "location": "Philadelphia, PA",
        "specialty": "Orthopedic Surgery"
    },
    {
        "program_name": "Pacific Northwest Health Institute",
        "location": "Portland, OR",
        "specialty": "Radiology"
    },
    {
        "program_name": "Coral Gables Hospital",
        "location": "Miami, FL",
        "specialty": "Dermatology"
    },
    {
        "program_name": "Peachtree Medical Center",
        "location": "Atlanta, GA",
        "specialty": "Rheumatology"
    },
    {
        "program_name": "Midwest Regional Hospital",
        "location": "St. Louis, MO",
        "specialty": "Gastroenterology"
    },
    {
        "program_name": "Queen City Medical University",
        "location": "Charlotte, NC",
        "specialty": "Urology"
    },
    {
        "program_name": "Sunrise Health Institute",
        "location": "Phoenix, AZ",
        "specialty": "Ophthalmology"
    },
    {
        "program_name": "Alamo Medical Center",
        "location": "San Antonio, TX",
        "specialty": "Pulmonology"
    },
    {
        "program_name": "Evergreen Health Center",
        "location": "Seattle, WA",
        "specialty": "Nephrology"
    },
    {
        "program_name": "Summit Health University",
        "location": "Denver, CO",
        "specialty": "Pathology"
    },
    {
        "program_name": "Hawkeye Medical Center",
        "location": "Des Moines, IA",
        "specialty": "Hematology"
    },
    {
        "program_name": "Bayside Health Institute",
        "location": "Tampa, FL",
        "specialty": "Otolaryngology"
    },
    {
        "program_name": "Aspen Grove Medical University",
        "location": "Salt Lake City, UT",
        "specialty": "Vascular Surgery"
    },
    {
        "program_name": "Rehabilitation Institute of Chicago",
        "location": "Chicago, IL",
        "specialty": "Physical Medicine and Rehabilitation"
    },
    {
        "program_name": "Hazelden Betty Ford Foundation",
        "location": "Center City, MN",
        "specialty": "Addiction Medicine"
    },
    {
        "program_name": "Mallinckrodt Institute of Radiology",
        "location": "St. Louis, MO",
        "specialty": "Nuclear Medicine"
    },
    {
        "program_name": "Dana-Farber Cancer Institute",
        "location": "Boston, MA",
        "specialty": "Palliative Care"
    },
    {
        "program_name": "Steadman Clinic",
        "location": "Vail, CO",
        "specialty": "Sports Medicine"
    },
    {
        "program_name": "University of Pittsburgh Medical Center",
        "location": "Pittsburgh, PA",
        "specialty": "Thoracic Surgery"
    },
    {
        "program_name": "National Jewish Health",
        "location": "Denver, CO",
        "specialty": "Allergy and Immunology"
    },
    {
        "program_name": "Children's Hospital of Philadelphia",
        "location": "Philadelphia, PA",
        "specialty": "Neonatal-Perinatal Medicine"
    },
    {
        "program_name": "Baylor College of Medicine",
        "location": "Houston, TX",
        "specialty": "Medical Genetics"
    },
    {
        "program_name": "Columbia University Medical Center",
        "location": "New York, NY",
        "specialty": "Neurology"
    },
    {
        "program_name": "Harborview Medical Center",
        "specialty": "Cardiology",
        "location": "Seattle, WA"
    },
    {
        "program_name": "Pinegrove Health System",
        "specialty": "Neurology",
        "location": "San Francisco, CA"
    },
    {
        "program_name": "Lakeside University Hospital",
        "specialty": "Orthopedic Surgery",
        "location": "Chicago, IL"
    },
    {
        "program_name": "Greenfield Children's Hospital",
        "specialty": "Pediatrics",
        "location": "New York, NY"
    },
    {
        "program_name": "Meadowbrook Radiology Clinic",
        "specialty": "Radiology",
        "location": "Boston, MA"
    },
    {
        "program_name": "Sunrise Medical Institute",
        "specialty": "Cardiology",
        "location": "Los Angeles, CA"
    },
    {
        "program_name": "Clearview Neurological Center",
        "specialty": "Neurology",
        "location": "Houston, TX"
    },
    {
        "program_name": "Bayside Orthopedic Clinic",
        "specialty": "Orthopedic Surgery",
        "location": "Miami, FL"
    },
    {
        "program_name": "Little Stars Pediatric Center",
        "specialty": "Pediatrics",
        "location": "Dallas, TX"
    },
    {
        "program_name": "Radiant Radiology Associates",
        "specialty": "Radiology",
        "location": "Denver, CO"
    }
]

# Students Table: Generate 1000 fake students.
for i in range(0, 1000):

    record = {
        'id': i,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'gpa': round(random.uniform(2.9, 4.0), 2),
        'specialty': random.choice(medical_specialties)
    }

    students.append(record)

# Residency Programs Table: Generate residency programs based on the dictionary above.
for i in range(0, len(residency_programs)):

    record = {
        'id': i,
        'program_name': residency_programs[i]['program_name'],
        'location': residency_programs[i]['location'],
        'specialty': residency_programs[i]['specialty'],
        'capacity': random.randint(1, 50)
    }

    residency_programs_final.append(record)

residency_ids = [residency['id'] for residency in residency_programs_final]

# Rankings Table: Generate random rankings for each student.
for i in range(0, len(students)):

    for j in range(1, 11):
        record = {
            'id': i,
            'student_id': students[i]['id'],
            'program_id': random.choice(residency_ids),
            # 'rank': random.randint(1,10)
            'ranking': j
        }

        rankings.append(record)


# Initialize all students and programs as unmatched.
unmatched_students = set(student['id'] for student in students)
program_capacity = {program['id']: program['capacity']
                    for program in residency_programs_final}
program_match = {program['id']: [] for program in residency_programs_final}

# Now we iterate over unmatched students to make proposals.
while unmatched_students:
    for student_id in list(unmatched_students):
        # Choose the highest-ranked program that the student has not yet proposed to.
        preferred_program_id = next(
            (ranking['program_id'] for ranking in rankings if ranking['student_id'] == student_id), None)

        # If the student has proposed to all programs, remove them from the list of unmatched students.
        if preferred_program_id is None:
            # Student has proposed to all programs and remains unmatched.
            unmatched_students.remove(student_id)
            continue

        # Remove this option from rankings so the student won't pick it again.
        rankings = [r for r in rankings if not (
            r['student_id'] == student_id and r['program_id'] == preferred_program_id)]

        # If the program has available capacity, accept the student.
        if len(program_match[preferred_program_id]) < program_capacity[preferred_program_id]:
            program_match[preferred_program_id].append(student_id)
            unmatched_students.remove(student_id)
        else:
            # Check if the program prefers this student over its current least preferred match.
            least_preferred_student = min(program_match[preferred_program_id], key=lambda x: next(
                (r['ranking'] for r in rankings if r['student_id'] == x and r['program_id'] == preferred_program_id), float('inf')))
            
            new_student_rank = next((r['ranking'] for r in rankings if r['student_id'] ==
                                     student_id and r['program_id'] == preferred_program_id), float('inf'))
            
            least_preferred_student_rank = next((r['ranking'] for r in rankings if r['student_id'] ==
                                                 least_preferred_student and r['program_id'] == preferred_program_id), float('inf'))

            if new_student_rank < least_preferred_student_rank:
                # Replace the least preferred student with the new student.
                program_match[preferred_program_id].remove(
                    least_preferred_student)
                program_match[preferred_program_id].append(student_id)
                unmatched_students.add(least_preferred_student)
                unmatched_students.remove(student_id)

# Insert data for residency_programs table.
for program in residency_programs:
    sql = "INSERT INTO Residency_Programs (program_name, location, specialty) VALUES (%s, %s, %s)"
    val = (program['program_name'], program['location'], program['specialty'])
    my_cursor.execute(sql, val)
    mydb.commit()

# Insert data for students table.
for student in students:
    sql = "INSERT INTO Students (first_name, last_name, email, gpa, specialty) VALUES (%s, %s, %s, %s, %s)"
    val = (student['first_name'], student['last_name'],
           student['email'], student['gpa'], student['specialty'])
    my_cursor.execute(sql, val)
    mydb.commit()

# Insert data for rankings table.
for ranking in rankings:
    sql = "INSERT INTO Rankings (student_id, program_id, ranking) VALUES (%s, %s, %s)"
    val = (ranking['student_id'], ranking['program_id'], ranking['ranking'])
    my_cursor.execute(sql, val)
    mydb.commit()

# Insert data for matches table.
for program in program_match:
    for student in program_match[program]:
        sql = "INSERT INTO Matches (student_id, program_id) VALUES (%s, %s)"
        val = (student, program)
        my_cursor.execute(sql, val)
        mydb.commit()