import psycopg2
from psycopg2.extras import execute_values
import bcrypt
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection string
db_url = os.getenv("DATABASE_URL")

# Connect to PostgreSQL database
conn = psycopg2.connect(db_url)
cursor = conn.cursor()

####################################### TABLE CREATION ########################################
# Create the `relevant_experience` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS relevant_experience (
    id SERIAL PRIMARY KEY,
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
    id SERIAL PRIMARY KEY,
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
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    role TEXT NOT NULL,
    year TEXT NOT NULL,
    description TEXT,
    image_path TEXT
)
''')

# Create the `licenses_and_certifications` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS licenses_and_certifications (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    issuer TEXT NOT NULL,
    issue_date TEXT NOT NULL,
    expiration_date TEXT,
    icon_path TEXT
)
''')

# Create the `other_experience` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS other_experience (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT,
    location TEXT,
    description TEXT
)
''')

# Create the `projects` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    technologies TEXT NOT NULL,
    github_link TEXT
)
''')

# Create the `blog_posts` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS blog_posts (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    visibility TEXT CHECK(visibility IN ('public', 'unlisted', 'private')) DEFAULT 'private',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    slug TEXT
)
''')

# Create the `password` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS password (
    password TEXT NOT NULL
)
''')

# Insert data into `relevant_experience`
relevant_experiences = [
    ("Machine Learning Engineering Intern", "SLAC National Accelerator Laboratory (Stanford University)", 
     "June 2023", "August 2023", "Menlo Park, CA", 
     "Optimized water-cooling systems using Python, PyTorch, numPy, and data from FAST particle accelerator injector at Fermilab by implementing a long short-term memory (LSTM) neural network.\nImproved speed of normalization of temperature by up to five times using model predictive control rather than traditional proportional-integral-derivative (PID) controller or other feed-forward neural network solutions.\nPrepared findings and gave a lecture at the laboratory on the benefits of utilizing machine learning in optimizing particle accelerators."),
    
    ("Machine Learning and DevOps Intern", "SLAC National Accelerator Laboratory (Stanford University)", 
     "June 2024", "August 2024", "Menlo Park, CA", 
     "Developed ML models to predict beam properties and quantify the accuracy and robustness of these predictive models over time for the FACET-II injector.\nReplaced older simulation softwares for FACET-II, specifically using Impact-T in place of the General Particle Tracer (GPT) and using Bmad in place of Lucretia.\nRan start-to-end simulations of the FACET-II beamline.")
]

execute_values(
    cursor,
    '''
    INSERT INTO relevant_experience (title, company, start_date, end_date, location, description)
    VALUES %s
    ''',
    relevant_experiences
)

# Insert data into `coursework`
coursework_entries = [
    ("AP Computer Science Principles", "Advanced Placement", 
     "September 2019", "June 2020", 
     "A course exploring the breadth of topics in computer science, including programming, data analysis, the internet, cybersecurity, and the societal impacts of computing."),
    
    ("AP Computer Science A", "Advanced Placement", 
     "September 2020", "June 2021", 
     "An introductory Java programming course covering object-oriented design, algorithms, data structures, and problem-solving."),
    
    ("Web Development Bootcamp", "University of Pennsylvania", 
     "July 2021", "July 2021", 
     "A 3-week online bootcamp introducing front-end web development, covering HTML, CSS, JavaScript, and GitHub for collaborative coding."),
    
    ("IB Computer Science SL", "International Baccalaureate", 
     "September 2021", "May 2022", 
     "An introductory course in computer science, exploring fundamental concepts like programming, algorithms, data structures, system design, and computational thinking through the completion of a full-scale application for an actual client."),
    
    ("EECS 183: Elementary Programming Concepts", "University of Michigan", 
     "September 2022", "December 2022", 
     "An introductory course in programming and software development using C++ and Python, covering functions, loops, arrays, classes, file I/O, and team dynamics."),
    
    ("EECS 203: Discrete Mathematics", "University of Michigan", 
     "January 2023", "April 2023", 
     "An introduction to the mathematical foundations of computer science, exploring logic, proof techniques, set theory, functions, algorithms, asymptotic analysis, counting principles, relations, and an introduction to graph theory."),
    
    ("EECS 280: Programming and Introduction to Data Structures", "University of Michigan", 
     "January 2023", "April 2023", 
     "A foundational course in C++ programming and software development, covering machine models, data structures, memory management, recursion, error handling, and advanced topics like polymorphism and inheritance."),
    
    ("EECS 281: Data Structures and Algorithms", "University of Michigan", 
     "September 2023", "December 2023", 
     "A comprehensive dive into Data Structures and Algorithms, covering fundamental ADTs, complexity analysis, recursion, sorting algorithms, hashing, tree and graph structures, dynamic programming, and advanced algorithmic techniques."),
    
    ("EECS 370: Introduction to Computer Organization", "University of Michigan", 
     "January 2024", "April 2024", 
     "A course offering foundational knowledge of computer execution, hardware architecture, C-based hardware simulation, and Assembly programming."),
    
    ("Hands-On High Performance Computing", "Oak Ridge Leadership Computing Facility", 
     "November 2024", "November 2024", 
     "A seven-hour crash course designed for students attending the SuperComputing24 conference in Atlanta, GA. Offers hands-on experience with high-performance computing (HPC) systems, exploring their applications in machine learning and quantum computing."),
    
    ("EECS 376: Foundation of Computer Science", "University of Michigan", 
     "September 2024", "December 2024", 
     "An introduction to Computer Science theory, covering algorithmic analysis, computability, complexity, randomness, and applications of theoretical concepts in cryptography."),
    
    ("EECS 485: Web Systems", "University of Michigan", 
     "September 2024", "December 2024", 
     "A holistic course of modern web systems and technologies, covering static and dynamic web pages, web security, REST APIs, asynchronous programming, React, distributed systems like MapReduce and Google File System, scaling techniques, recommender systems, and emerging topics like blockchain and the dark web."),
    
    ("EECS 481: Software Engineering", "University of Michigan", 
     "January 2025", "April 2025", 
     "An practical course in Software Engineering, focusing on process, risk, scheduling, quality assurance, testing, measurement techniques, test coverage, mutation testing, code inspection, and continuous testing."),
    
    ("EECS 471: Applied Parallel Programming with GPUs", "University of Michigan", 
     "January 2025", "April 2025", 
     "An exploration of parallel computing with GPUs, focusing on CUDA programming, memory models, parallel algorithms, and GPU microarchitecture. Topics include convolution, reduction patterns, atomic operations, sparse methods, and case studies in deep learning.")
]

execute_values(
    cursor,
    '''
    INSERT INTO coursework (title, institution, start_date, end_date, description)
    VALUES %s
    ''',
    coursework_entries
)

# Save image files and insert data into `conference_management_experience`
conference_entries = [
    ("Society of Asian Scientists and Engineers 2024 Midwest Regional Conference", 
     "Conference Chairperson", 
     "March 30, 2024", 
     "Led the planning and execution of the Midwest Regional Conference, managing all aspects including scheduling, team coordination, and event logistics.",
     "sasemwrc2024.jpg"),
    ("Society of Asian Scientists and Engineers 2024 National Convention", 
     "Director of Workshops and Entertainment", 
     "October 10-12, 2024", 
     "Organized workshops and entertainment activities for the national convention, coordinating logistics and managing a diverse team to ensure smooth execution.",
     "sasenatcon2024.jpg")
]

execute_values(
    cursor,
    '''
    INSERT INTO conference_management_experience (title, role, year, description, image_path)
    VALUES %s
    ''',
    conference_entries
)

# Insert data into `licenses_and_certifications`
licenses_and_certifications_entries = [
    ("Lifeguard Certification", "Jeff Ellis and Associates, Inc.", "July 2021", "July 2022", "jeffellis.png"),
    ("Standard First Aid, CPR and AED", "Jeff Ellis and Associates, Inc.", "July 2021", "July 2022", "jeffellis.png"),
    ("Seal of Biliteracy - English and Spanish", "New York State Department of Education", "May 2022", None, "nysed.png"),
    ("Driver's License - Class D", "New York State Department of Motor Vehicles", "June 2022", "December 2025", "dmv.png"),
    ("IB Diploma", "International Baccalaureate Organization", "July 2022", None, "ib.png"),
    ("OLCF Hands-On HPC", "Oak Ridge National Laboratory", "December 2024", None, "ornl.png")
]

execute_values(
    cursor,
    '''
    INSERT INTO licenses_and_certifications (title, issuer, issue_date, expiration_date, icon_path)
    VALUES %s
    ''',
    licenses_and_certifications_entries
)

other_experiences = [
    ("Clerk (Volunteer)", "Stony Brook University Medical Center", "September 2019", "March 2020", "Calverton, NY", 
     "Assisted parents with completing and processing Social Security applications and birth certificates for newborns.\n"
     "Performed regular comfort rounding, checking in on patients to ensure their needs were met and their stay was as comfortable as possible.\n"
     "Ensured compliance by verifying that all newborns received required immunizations before discharge."),
    
    ("Lifeguard", "Palace Entertainment", "July 2021", "August 2021", "Calverton, NY", 
     "Monitored pool and surrounding areas to ensure safety, enforcing rules and regulations to prevent accidents and injuries.\n"
     "Responded promptly to emergencies, administering CPR, first aid, and life-saving techniques to individuals in need.\n"
     "Delivered clear and effective communication to patrons regarding pool policies and safety protocols."),
    
    ("Barista", "Sweetwaters Coffee & Tea", "November 2023", "April 2024", "Ann Arbor, MI", 
     "Prepared and served high-quality coffee, tea, and specialty beverages while adhering to standardized recipes and customer preferences.\n"
     "Managed inventory and restocked supplies, contributing to efficient operations and reducing downtime during peak hours.\n"
     "Delivered exceptional customer service by creating a welcoming environment and addressing guest needs promptly and courteously."),
    
    ("Judge/Mentor", "MHacks", "September 2024", None, "Ann Arbor, MI", 
     "Served as a judge for over 50 innovative tech projects, providing detailed feedback on technical complexity, creativity, and execution.\n"
     "Mentored 20+ teams of developers, guiding them through ideation, coding challenges, and project presentation.\n"
     "Provided real-time technical support to hackathon participants, ensuring efficient problem-solving in a high-pressure environment."),
    
    ("Information Assistant", "University of Michigan", "April 2024", "Present", "Ann Arbor, MI", 
     "Provided accurate and timely information to students, staff, and visitors regarding campus events, resources, and services.\n"
     "Addressed caller concerns with empathy and resourcefulness, escalating complex issues to supervisors when necessary.\n"
     "Conducted detailed audits of online campus maps for Big Ten universities, benchmarking their features and functionality against the University of Michigan’s online map system.")
]

execute_values(
    cursor,
    '''
        INSERT INTO other_experience (title, company, start_date, end_date, location, description)
        VALUES (?, ?, ?, ?, ?, ?)
    ''',
    other_experiences
)

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

####################################### PROJECTS ########################################
####################################### LOGIN ########################################
load_dotenv()
password = os.getenv('PASSWORD')
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
cursor.execute('''
CREATE TABLE IF NOT EXISTS password (
    password TEXT NOT NULL
)
''')

cursor.execute('''
INSERT INTO password (password)
VALUES (%s)
''', (hashed_password,))


####################################### LOGIN ########################################
####################################### BLOG AND PHILOSOPHY #######################################
cursor.execute('''
CREATE TABLE blog_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    visibility TEXT CHECK(visibility IN ('public', 'unlisted', 'private')) DEFAULT 'private',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    slug TEXT
)
''')

blog_posts_entries = [
    (
        "Welcome to a Brand New Experience of robinhwang.net!",
        "Welcome to my first-ever blog post on my personal website, robinhwang.net, V2! If you’ve stumbled upon this page, congratulations—you’ve found the beginning of something special.\n\n"
        "This site is a space where you can get to know me, explore my thoughts, and follow along on my journey. Here, I’ll be sharing updates about my life, my studies, my projects, and everything in between.\n\n"
        "For those who visited the previous version of robinhwang.net, this updated website offers a completely new experience—a treat for both returning and new visitors. It’s far more robustly developed than the first version, leveraging the Python Flask micro-web framework, Bulma, vanilla JavaScript, and SQLite3 (soon to be upgraded to PostgreSQL) with proper package management. Admittedly, the original version had its flaws, with a few buggy elements and shortcuts I chose to overlook. However, this new iteration is a polished reflection of a completed full-stack application, and I’m thrilled to share it with you.\n\n"
        "A little about me: I’m a student at the University of Michigan, pursuing my dream of becoming a software engineer. I love coding, exploring new places, and solving challenging problems. Through this blog, I hope to share my experiences, not only as a student but also as someone navigating the ups and downs of life and learning along the way. I also use it as a personal diary (you won't be able to see those blog posts though since I'm making them private) and a place to jot down my own opinions about not only technology, but the world at-large.\n\n"
        "Whether you’re here out of curiosity, because you know me personally, or because you’ve stumbled upon this site through the vastness of the internet, or because you're trying to recruit me for a coveted position on your ;) software development team, I’m so glad you’re here. I hope this blog becomes a place where ideas are shared, connections are made, and stories are told.\n\n"
        "Feel free to explore my website, check out my projects, and connect with me. And if you like what you see, don’t forget to bookmark this page or drop me a message on LinkedIn. I’d love to hear from you!\n\n"
        "Thank you for stopping by, and welcome to robinhwang.net. This is just the beginning, and I’m excited to see where this journey takes us.",
        "public",
        "how-to-build-a-simple-website-with-html-and-css-a68a17ea"
    )
]

execute_values(
    cursor,
    '''
    INSERT INTO blog_posts (title, content, visibility, slug)
    VALUES %s
    ''',
    blog_posts_entries
)   

# Commit changes and close connection
conn.commit()
conn.close()

print("Database has been populated successfully.")
