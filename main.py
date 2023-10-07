import random
import json
import mysql.connector
from fakeData import fakeData

# Don't forget to run mysql.server start before running this script.

def mysql_connect():
    """
    Connect to MySQL and return a cursor.
    """

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
    my_cursor.execute("USE mydatabase")
    return mydb, my_cursor

def drop_mysql_tables(my_cursor):
    """
    Drop tables if they already exist.
    """

    # Use the new database, and drop tables if they already exist.
    my_cursor.execute("DROP TABLE IF EXISTS Students")
    my_cursor.execute("DROP TABLE IF EXISTS Residency_Programs")
    my_cursor.execute("DROP TABLE IF EXISTS Rankings")
    my_cursor.execute("DROP TABLE IF EXISTS Matches")

def create_mysql_students_table(my_cursor):
    """
    Create a new students table if it doesn't already exist.
    """

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

def create_mysql_residency_programs_table(my_cursor):
    """
    Create a new residency_programs table if it doesn't already exist.
    """

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

def create_mysql_rankings_table(my_cursor):
    """
    Create a new rankings table if it doesn't already exist.
    """

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

def create_mysql_matches_table(my_cursor):
    """
    Create a new matches table if it doesn't already exist.
    """

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

def insert_mysql_students_data(my_cursor, students):
    """
    Insert data for students table.
    """
    
    for student in students:
        sql = "INSERT INTO Students (first_name, last_name, email, gpa, specialty) VALUES (%s, %s, %s, %s, %s)"
        val = (student['first_name'], student['last_name'],
            student['email'], student['gpa'], student['specialty'])
        my_cursor.execute(sql, val)
        mydb.commit()

def insert_mysql_residency_programs_data(my_cursor, residency_programs):
    """
    Insert data for residency_programs table.
    """

    for program in residency_programs:
        sql = "INSERT INTO Residency_Programs (program_name, location, specialty) VALUES (%s, %s, %s)"
        val = (program['program_name'], program['location'], program['specialty'])
        my_cursor.execute(sql, val)
        mydb.commit()

def insert_mysql_rankings_data(my_cursor, rankings):
    """
    Insert data for rankings table.
    """

    for ranking in rankings:
        sql = "INSERT INTO Rankings (student_id, program_id, ranking) VALUES (%s, %s, %s)"
        val = (ranking['student_id'], ranking['program_id'], ranking['ranking'])
        my_cursor.execute(sql, val)
        mydb.commit()

def insert_mysql_matches_data(my_cursor, program_match):
    """
    Insert data for matches table.
    """

    for program in program_match:
        for student in program_match[program]:
            sql = "INSERT INTO Matches (student_id, program_id) VALUES (%s, %s)"
            val = (student, program)
            my_cursor.execute(sql, val)
            mydb.commit()

def gale_shapley_matching_algorithm(unmatched_students, program_capacity, program_match, rankings):
    """
    Run the Gale-Shapley matching algorithm to match students to residency programs.
    """

    for student_id in list(unmatched_students):
        # On the assumption of sorted rankings, choose the highest-ranked program
        # that the student has not yet proposed to.
        preferred_program_id = next(
            (ranking['program_id'] for ranking in rankings if ranking['student_id'] == student_id), None)

        # If the student has proposed to all programs, remove them from the list of unmatched students.
        if preferred_program_id is None:
            # Student has proposed to all programs and remains unmatched.
            unmatched_students.remove(student_id)
            continue

        # Remove the current student from the rankings so that they can't propose to the same program again. 
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
        

if __name__ == "__main__":
    # Connect to MySQL.
    mydb, my_cursor = mysql_connect()

    # Drop tables if they already exist.
    drop_mysql_tables(my_cursor)

    # Create tables.
    create_mysql_students_table(my_cursor)
    create_mysql_residency_programs_table(my_cursor)
    create_mysql_rankings_table(my_cursor)
    create_mysql_matches_table(my_cursor)

    # Generate all fake data using the fakeData class.
    fd = fakeData()
    medical_specialties = fd.get_medical_specialties()
    residency_programs = fd.get_residency_programs()
    students = fd.generate_student_data()
    residency_programs = fd.generate_residency_data()
    residency_ids = fd.generate_residency_ids()
    rankings = fd.generate_rankings_data()

    # Shuffle the students so that they don't propose in the same order every time.
    # This also ensures that the algorithm is stable.
    students_shuffled = students
    random.shuffle(students_shuffled)

    # Initialize all students as unmatched.
    unmatched_students = set(student['id'] for student in students_shuffled)
    
    # Create a dictionary of program capacities.
    program_capacity = {program['id']: program['capacity']
                        for program in residency_programs}
    
    # Create a dictionary of program matches, initialized to empty lists.
    program_match = {program['id']: [] for program in residency_programs}

    # Run the algorithm.
    gale_shapley_matching_algorithm(unmatched_students, program_capacity, program_match, rankings)

    # Insert data into MySQL.
    insert_mysql_students_data(my_cursor, students)
    insert_mysql_residency_programs_data(my_cursor, residency_programs)
    insert_mysql_rankings_data(my_cursor, rankings)
    insert_mysql_matches_data(my_cursor, program_match)