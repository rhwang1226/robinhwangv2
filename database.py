import sqlite3

# Database file path
db_path = "robinhwang/data/robinhwang.db"
images_dir = "robinhwang/static"

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

####################################### EDUCATION AND EXPERIENCE ########################################
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

# Create the `licenses_and_certifications` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS licenses_and_certifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    issuer TEXT NOT NULL,
    issue_date TEXT NOT NULL,
    expiration_date TEXT,
    icon_path TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS other_experience (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT,
    location TEXT,
    description TEXT
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
    ("Hands-On High Performance Computing", "Oak Ridge Leadership Computing Facility", 
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
     "October 10-12, 2024", 
     "Organized workshops and entertainment activities for the national convention, coordinating logistics and managing a diverse team to ensure smooth execution.",
     "sasenatcon2024.jpg"),
    ("Society of Asian Scientists and Engineers 2024 Midwest Regional Conference", 
     "Conference Chairperson", 
     "March 30, 2024", 
     "Led the planning and execution of the Midwest Regional Conference, managing all aspects including scheduling, team coordination, and event logistics.",
     "sasemwrc2024.jpg")
]

for conference in conference_entries:
    # Insert data into the table
    cursor.execute('''
    INSERT INTO conference_management_experience (title, role, year, description, image_path)
    VALUES (?, ?, ?, ?, ?)
    ''', (conference[0], conference[1], conference[2], conference[3], conference[4]))

# Insert data into `licenses_and_certifications`
licenses_and_certifications_entries = [
    ("OLCF Hands-On HPC", "Oak Ridge National Laboratory", "December 2024", None, "uploads/ornl.png"),
    ("IB Diploma", "International Baccalaureate Organization", "July 2022", None, "uploads/ib.png"),
    ("Driver's License - Class D", "New York State Department of Motor Vehicles", "June 2022", "December 2025", "uploads/dmv.png"),
    ("Seal of Biliteracy - English and Spanish", "New York State Department of Education", "May 2022", None, "uploads/nysed.png"),
    ("Standard First Aid, CPR and AED", "Jeff Ellis and Associates, Inc.", "July 2021", "July 2022", "uploads/jeffellis.png"),
    ("Lifeguard Certification", "Jeff Ellis and Associates, Inc.", "July 2021", "July 2022", "uploads/jeffellis.png")
]

for license in licenses_and_certifications_entries:
    cursor.execute('''
        INSERT INTO licenses_and_certifications (title, issuer, issue_date, expiration_date, icon_path)
        VALUES (?, ?, ?, ?, ?)
    ''', license)

other_experiences = [
    ("Information Assistant", "University of Michigan", "April 2024", "Present", "Ann Arbor, MI", 
     "Provided accurate and timely information to students, staff, and visitors regarding campus events, resources, and services.\n"
     "Addressed caller concerns with empathy and resourcefulness, escalating complex issues to supervisors when necessary.\n"
     "Conducted detailed audits of online campus maps for Big Ten universities, benchmarking their features and functionality against the University of Michigan’s online map system."),
    
    ("Judge/Mentor", "MHacks", "September 2024", None, "Ann Arbor, MI", 
     "Served as a judge for over 50 innovative tech projects, providing detailed feedback on technical complexity, creativity, and execution.\n"
     "Mentored 20+ teams of developers, guiding them through ideation, coding challenges, and project presentation.\n"
     "Provided real-time technical support to hackathon participants, ensuring efficient problem-solving in a high-pressure environment."),
    
    ("Barista", "Sweetwaters Coffee & Tea", "November 2023", "April 2024", "Ann Arbor, MI", 
     "Prepared and served high-quality coffee, tea, and specialty beverages while adhering to standardized recipes and customer preferences.\n"
     "Managed inventory and restocked supplies, contributing to efficient operations and reducing downtime during peak hours.\n"
     "Delivered exceptional customer service by creating a welcoming environment and addressing guest needs promptly and courteously."),
    
    ("Lifeguard", "Palace Entertainment", "July 2021", "August 2021", "Calverton, NY", 
     "Monitored pool and surrounding areas to ensure safety, enforcing rules and regulations to prevent accidents and injuries.\n"
     "Responded promptly to emergencies, administering CPR, first aid, and life-saving techniques to individuals in need.\n"
     "Delivered clear and effective communication to patrons regarding pool policies and safety protocols."),
    
    ("Clerk (Volunteer)", "Stony Brook University Medical Center", "September 2019", "March 2020", "Calverton, NY", 
     "Assisted parents with completing and processing Social Security applications and birth certificates for newborns.\n"
     "Performed regular comfort rounding, checking in on patients to ensure their needs were met and their stay was as comfortable as possible.\n"
     "Ensured compliance by verifying that all newborns received required immunizations before discharge.")
]

for experience in other_experiences:
    cursor.execute('''
        INSERT INTO other_experience (title, company, start_date, end_date, location, description)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', experience)

####################################### EDUCATION AND EXPERIENCE ########################################
####################################### PROJECTS ########################################
cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    technologies TEXT NOT NULL, -- Comma-separated list of technologies
    github_link TEXT -- Optional link to GitHub or demo
)
''')

projects = [
    ("Search485", 
     "Search engine that indexes Wikipedia pages with user-adjustable tf-idf and PageRank weights. Includes a MapReduce pipeline for parallel data processing of Wikipedia HTML archives.",
     "Python,HTML,CSS,Flask,SQLite,Bash,REST APIs,Jinja", 
     None),

    ("Insta485", 
     "A simplified clone of the social media app Instagram with like, comment, follow/unfollow, post, and infinite scroll features.",
     "JavaScript,React,HTML,CSS,Flask,SQLite,Bash,REST APIs,Jinja", 
     None),

    ("Bingo Card Generator", 
     "Generator that creates a set of random Bingo cards and saves the cards in a Microsoft Word (.docx) document.",
     "Python,Python-docx", 
     "https://github.com/rhwang1226/bingo-card-generator"),

    ("Apple Picking Route Assigner", 
     "A program that assigns drivers to riders given (x,y) coordinates of each person so that each driver can drive as little distance as possible (a variation of Dijkstra's shortest path algorithm). Inspired by the 2024 SASE Apple Picking Trip.",
     "Python", 
     "https://github.com/rhwang1226/sase-apple-picking"),

    ("Start-to-End Particle Accelerator Simulations", 
     "Simulation software of the FACET-II beamline at SLAC National Accelerator Laboratory with features to adjust accelerating cavity phase, amplitude, and electron source charge.",
     "Python,matplotlib,NumPy,Bmad,PyTao", 
     "https://github.com/rhwang1226/facetii-parameter-scan"),

    ("Tee Ninja", 
     "An automatic golf tee time reservation application that reserves a golf tee time in a given desired time frame at 7:00 PM every evening. Comes with a GUI for easy client use.",
     "Python,Selenium,Tkinter", 
     "https://github.com/rhwang1226/Tee-Ninja"),

    ("DishDash", 
     "An iOS application that allows students to sell leftover food items to other students instead of letting the food go to waste. Features Dockerization including all necessary dependencies.",
     "Swift,Docker", 
     "https://github.com/rhwang1226/DishDash"),

    ("Cache Simulator", 
     "A CPU cache simulator integrated into an LC2K ISA behavioral simulator. Features write-back, allocate-on-write, cache associativity, and placement/replacement policy integration.",
     "C++", 
     None),

    ("281Bank", 
     "A bank wire transfer simulator utilizing real-time gross settlement. Main objective was to learn about the evaluation of runtime and storage tradeoffs based on different data structures.",
     "C++", 
     None),

    ("Neural Network for Particle Accelerator", 
     "A long short-term neural network modeling a time series of the FAST gun at Fermilab. Completed under the supervision of staff at SLAC National Accelerator Laboratory.",
     "Python,PyTorch,Machine Learning", 
     "https://github.com/rhwang1226/lstm_lcls_water_cooling"),

    ("Piazza Post Classifier", 
     "A Piazza (an online forum) post classifier that is able to automatically identify the subject of posts based on its content.",
     "C++,Natural Language Processing,Machine Learning", 
     None, 
     None),

    ("COVInsight", 
     "A database with robust search and filter features for phylogenic analyses of SARS-CoV-2 (novel Coronavirus) strains. Includes a customized binary search algorithm and a desktop GUI in Java Swing.",
     "Java,Swing", 
     None),

    ("Classroom Reservation System", 
     "A classroom reservation system for Commack High School including feature-rich mechanisms such as administrative controls. Designed to operate on a school district local area network (LAN).",
     "Java,Swing", 
     None)
]

# Sample project data
projects = [
    ("robinhwang.net", 
     "Personal portfolio site with server-side dynamic rendering for a blog subpage. Hint: look at the address bar to see your current URL :)",
     "Python,HTML,CSS,Flask,SQLite,Bash,REST APIs,Jinja", 
     "https://github.com/rhwang1226/robinhwangv2"),

    ("Search485", 
     "Search engine that indexes Wikipedia pages with user-adjustable tf-idf and PageRank weights. Includes a MapReduce pipeline for parallel data processing of Wikipedia HTML archives.",
     "Python,HTML,CSS,Flask,SQLite,Bash,REST APIs,Jinja", 
     None),

    ("Insta485", 
     "A simplified clone of the social media app Instagram with like, comment, follow/unfollow, post, and infinite scroll features.",
     "JavaScript,React,HTML,CSS,Flask,SQLite,Bash,REST APIs,Jinja", 
     None),

    ("Bingo Card Generator", 
     "Generator that creates a set of random Bingo cards and saves the cards in a Microsoft Word (.docx) document.",
     "Python,Python-docx", 
     "https://github.com/rhwang1226/bingo-card-generator"),

    ("Apple Picking Route Assigner", 
     "A program that assigns drivers to riders given (x,y) coordinates of each person so that each driver can drive as little distance as possible (a variation of Dijkstra's shortest path algorithm). Inspired by the 2024 SASE Apple Picking Trip.",
     "Python", 
     "https://github.com/rhwang1226/sase-apple-picking"),

    ("Start-to-End Particle Accelerator Simulations", 
     "Simulation software of the FACET-II beamline at SLAC National Accelerator Laboratory with features to adjust accelerating cavity phase, amplitude, and electron source charge.",
     "Python,matplotlib,NumPy,Bmad,PyTao", 
     "https://github.com/rhwang1226/facetii-parameter-scan"),

    ("Tee Ninja", 
     "An automatic golf tee time reservation application that reserves a golf tee time in a given desired time frame at 7:00 PM every evening. Comes with a GUI for easy client use.",
     "Python,Selenium,Tkinter", 
     "https://github.com/rhwang1226/Tee-Ninja"),

    ("DishDash", 
     "An iOS application that allows students to sell leftover food items to other students instead of letting the food go to waste. Features Dockerization including all necessary dependencies.",
     "Swift,Docker", 
     "https://github.com/rhwang1226/DishDash"),

    ("Cache Simulator", 
     "A CPU cache simulator integrated into an LC2K ISA behavioral simulator. Features write-back, allocate-on-write, cache associativity, and placement/replacement policy integration.",
     "C++", 
     None),

    ("281Bank", 
     "A bank wire transfer simulator utilizing real-time gross settlement. Main objective was to learn about the evaluation of runtime and storage tradeoffs based on different data structures.",
     "C++", 
     None),

    ("Neural Network for Particle Accelerator", 
     "A long short-term neural network modeling a time series of the FAST gun at Fermilab. Completed under the supervision of staff at SLAC National Accelerator Laboratory.",
     "Python,PyTorch,Machine Learning", 
     "https://github.com/rhwang1226/lstm_lcls_water_cooling"),

    ("Piazza Post Classifier", 
     "A Piazza (an online forum) post classifier that is able to automatically identify the subject of posts based on its content.",
     "C++,Natural Language Processing,Machine Learning", 
     None),

    ("COVInsight", 
     "A database with robust search and filter features for phylogenic analyses of SARS-CoV-2 (novel Coronavirus) strains. Includes a customized binary search algorithm and a desktop GUI in Java Swing.",
     "Java,Swing", 
     "https://github.com/rhwang1226/COVInsight"),

    ("Classroom Reservation System", 
     "A classroom reservation system for Commack High School including feature-rich mechanisms such as administrative controls. Designed to operate on a school district local area network (LAN).",
     "Java,Swing", 
     "https://github.com/rhwang1226/Commack-Room-Reservation-System")
]

# Insert project data into the `projects` table
for project in projects:
    cursor.execute('''
        INSERT INTO projects (title, description, technologies, github_link)
        VALUES (?, ?, ?, ?)
    ''', project)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database has been populated successfully.")
