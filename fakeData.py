import random
from faker import Faker

class fakeData:
    def __init__(self):
        """
        Initialize the fakeData class.
        """
        # List of medical specialties to choose from.
        self.medical_specialties = [
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
        # Generate a list of residency programs based on the dictionaries below.
        self.residency_programs_base = [
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
        # self.residency_programs_by_specialty = residency_programs_by_specialty
        self.residency_ids = []
        self.students = []
        # Initialize Faker and data
        self.fake = Faker()
        self.residency_programs = []
        self.rankings = []
        self.matches = []


    def get_medical_specialties(self):
        """
        Returns the list of medical specialties.
        """
        return self.medical_specialties

    def get_residency_programs(self):
        """
        Returns the list of residency programs.
        """
        return self.residency_programs_base
    
    def generate_student_data(self):
        """
        Generates fake student data.
        """
        # Students Table: Generate 1000 fake students.
        for i in range(0, 1000):

            record = {
                'id': i,
                'first_name': self.fake.first_name(),
                'last_name': self.fake.last_name(),
                'email': self.fake.email(),
                'gpa': round(random.uniform(2.9, 4.0), 2),
                'specialty': random.choice(self.medical_specialties)
            }

            self.students.append(record)
        
        return self.students


    def generate_residency_data(self):
        """
        Generates fake residency data.
        """
        residency_programs_base = self.residency_programs_base
        # Residency Programs Table: Generate residency programs based on the dictionary above.
        for i in range(0, len(residency_programs_base)):

            record = {
                'id': i,
                'program_name': residency_programs_base[i]['program_name'],
                'location': residency_programs_base[i]['location'],
                'specialty': residency_programs_base[i]['specialty'],
                'capacity': random.randint(1, 50)
            }

            self.residency_programs.append(record)
        
        return self.residency_programs

    def generate_residency_ids(self):
        """
        Generates a list of residency IDs.
        """
        # Residency IDs: Create a list of residency IDs to choose from.
        self.residency_ids = [residency['id'] for residency in self.residency_programs]
        return self.residency_ids


    def generate_rankings_data(self):
        """
        Generates fake rankings data.
        """
        # Rankings Table: Generate random rankings for each student.
        for i in range(0, len(self.students)):

            for j in range(1, 11):
                record = {
                    'id': i,
                    'student_id': self.students[i]['id'],
                    'program_id': random.choice(self.residency_ids),
                    # 'rank': random.randint(1,10)
                    'ranking': j
                }

                self.rankings.append(record)
        
        return self.rankings