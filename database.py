import sqlite3

# Database file path
db_path = "robinhwang/data/experience.db"
images_dir = "robinhwang/static"

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the `relevant_experience` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS relevant_experience (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    start_date TEXT,
    end_date TEXT,
    location TEXT,
    description TEXT
)
''')

# Create the `coursework` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS coursework (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    institution TEXT NOT NULL,
    start_date TEXT,
    end_date TEXT,
    description TEXT
)
''')

# Create the `conference_management_experience` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS conference_management_experience (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    role TEXT NOT NULL,
    year INTEGER NOT NULL,
    description TEXT,
    image_path TEXT
)
''')

# Insert data into `relevant_experience`
relevant_experiences = [
    ("Machine Learning and DevOps Intern", "SLAC National Accelerator Laboratory (Stanford University)", 
     "June 2024", "August 2024", "Menlo Park, CA", 
     "Developed ML models to predict beam properties and quantify the accuracy and robustness of these predictive models over time for the FACET-II injector.\nReplaced older simulation softwares for FACET-II, specifically using Impact-T in place of the General Particle Tracer (GPT) and using Bmad in place of Lucretia.\nRan start-to-end simulations of the FACET-II beamline."),
    ("Machine Learning Engineering Intern", "SLAC National Accelerator Laboratory (Stanford University)", 
     "June 2023", "August 2023", "Menlo Park, CA", 
     "Optimized water-cooling systems using Python, PyTorch, numPy, and data from FAST particle accelerator injector at Fermilab by implementing a long short-term memory (LSTM) neural network.\nImproved speed of normalization of temperature by up to five times using model predictive control rather than traditional proportional-integral-derivative (PID) controller or other feed-forward neural network solutions.\nPrepared findings and gave a lecture at the laboratory on the benefits of utilizing machine learning in optimizing particle accelerators.")
]

for experience in relevant_experiences:
    cursor.execute('''
    INSERT INTO relevant_experience (title, company, start_date, end_date, location, description)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', experience)

# Insert data into `coursework`
coursework_entries = [
    ("EECS 471: Applied Parallel Programming with GPUs", "University of Michigan", 
     "January 2025", "April 2025", 
     "An exploration of parallel computing with GPUs, focusing on CUDA programming, memory models, parallel algorithms, and GPU microarchitecture. Topics include convolution, reduction patterns, atomic operations, sparse methods, and case studies in deep learning."),
    ("EECS 481: Software Engineering", "University of Michigan", 
     "January 2025", "April 2025", 
     "An practical course in Software Engineering, focusing on process, risk, scheduling, quality assurance, testing, measurement techniques, test coverage, mutation testing, code inspection, and continuous testing."),
    ("EECS 485: Web Systems", "University of Michigan", 
     "September 2024", "December 2024", 
     "A holistic course of modern web systems and technologies, covering static and dynamic web pages, web security, REST APIs, asynchronous programming, React, distributed systems like MapReduce and Google File System, scaling techniques, recommender systems, and emerging topics like blockchain and the dark web."),
    ("EECS 376: Foundation of Computer Science", "University of Michigan", 
     "September 2024", "December 2024", 
     "An introduction to Computer Science theory, covering algorithmic analysis, computability, complexity, randomness, and applications of theoretical concepts in cryptography."),
    ("Hands-On High Performance Computing", "Oak Ridge Leadership Computing Facility (SC24)", 
     "November 2024", "November 2024", 
     "A seven-hour crash course designed for students attending the SuperComputing24 conference in Atlanta, GA. Offers hands-on experience with high-performance computing (HPC) systems, exploring their applications in machine learning and quantum computing."),
    ("EECS 370: Introduction to Computer Organization", "University of Michigan", 
     "January 2024", "April 2024", 
     "A course offering foundational knowledge of computer execution, hardware architecture, C-based hardware simulation, and Assembly programming."),
    ("EECS 281: Data Structures and Algorithms", "University of Michigan", 
     "September 2023", "December 2023", 
     "A comprehensive dive into Data Structures and Algorithms, covering fundamental ADTs, complexity analysis, recursion, sorting algorithms, hashing, tree and graph structures, dynamic programming, and advanced algorithmic techniques."),
    ("EECS 280: Programming and Introduction to Data Structures", "University of Michigan", 
     "January 2023", "April 2023", 
     "A foundational course in C++ programming and software development, covering machine models, data structures, memory management, recursion, error handling, and advanced topics like polymorphism and inheritance."),
    ("EECS 203: Discrete Mathematics", "University of Michigan", 
     "January 2023", "April 2023", 
     "An introduction to the mathematical foundations of computer science, exploring logic, proof techniques, set theory, functions, algorithms, asymptotic analysis, counting principles, relations, and an introduction to graph theory."),
    ("EECS 183: Elementary Programming Concepts", "University of Michigan", 
     "September 2022", "December 2022", 
     "An introductory course in programming and software development using C++ and Python, covering functions, loops, arrays, classes, file I/O, and team dynamics."),
    ("IB Computer Science SL", "International Baccalaureate", 
     "September 2021", "May 2022", 
     "An introductory course in computer science, exploring fundamental concepts like programming, algorithms, data structures, system design, and computational thinking through the completion of a full-scale application for an actual client."),
    ("Web Development Bootcamp", "University of Pennsylvania", 
     "July 2021", "July 2021", 
     "A 3-week online bootcamp introducing front-end web development, covering HTML, CSS, JavaScript, and GitHub for collaborative coding."),
    ("AP Computer Science A", "Advanced Placement", 
     "September 2020", "June 2021", 
     "An introductory Java programming course covering object-oriented design, algorithms, data structures, and problem-solving."),
    ("AP Computer Science Principles", "Advanced Placement", 
     "September 2019", "June 2020", 
     "A course exploring the breadth of topics in computer science, including programming, data analysis, the internet, cybersecurity, and the societal impacts of computing.")
]


for course in coursework_entries:
    cursor.execute('''
    INSERT INTO coursework (title, institution, start_date, end_date, description)
    VALUES (?, ?, ?, ?, ?)
    ''', course)

# Save image files and insert data into `conference_management_experience`
conference_entries = [
    ("Society of Asian Scientists and Engineers 2024 National Convention", 
     "Director of Workshops and Entertainment", 
     2024, 
     "Organized workshops and entertainment activities for the national convention, coordinating logistics and managing a diverse team to ensure smooth execution.",
     "sasenatcon2024.jpg"),
    ("Society of Asian Scientists and Engineers 2024 Midwest Regional Conference", 
     "Conference Chairperson", 
     2024, 
     "Led the planning and execution of the Midwest Regional Conference, managing all aspects including scheduling, team coordination, and event logistics.",
     "sasemwrc2024.jpg")
]

for conference in conference_entries:
    # Insert data into the table
    cursor.execute('''
    INSERT INTO conference_management_experience (title, role, year, description, image_path)
    VALUES (?, ?, ?, ?, ?)
    ''', (conference[0], conference[1], conference[2], conference[3], conference[4]))

# Commit changes and close connection
conn.commit()
conn.close()

print("Database has been populated successfully.")
