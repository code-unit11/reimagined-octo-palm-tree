# Career Guidance Chatbot Logic

career_data = {

    "coding": {
        "field": "Technology & Computer Science",

        "careers": [
            "Software Developer",
            "Full Stack Developer",
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist",
            "Cyber Security Analyst",
            "Cloud Engineer",
            "Game Developer"
        ],

        "skills": [
            "Python",
            "Java",
            "C++",
            "Data Structures",
            "Algorithms",
            "Database (SQL)",
            "Git & GitHub",
            "Problem Solving"
        ],

        "details":
        """
Technology field focuses on creating software, websites, AI systems and applications.

Roadmap:
1. Learn Programming Language
2. Learn Data Structures & Algorithms
3. Learn Database
4. Build Real Projects
5. Learn Development Tools
6. Apply for Internships

Career Growth:
Beginner → Developer → Senior Developer → Tech Lead → Architect
"""
    },


    "data science": {

        "field": "Data Science & Analytics",

        "careers": [
            "Data Scientist",
            "Data Analyst",
            "Business Analyst",
            "Machine Learning Engineer"
        ],

        "skills": [
            "Python",
            "Statistics",
            "Machine Learning",
            "SQL",
            "Power BI",
            "Data Visualization"
        ],

        "details":
        """
Data Science uses data to find patterns and make predictions.

Roadmap:
1. Python Programming
2. Statistics & Mathematics
3. SQL Database
4. Machine Learning
5. Deep Learning
6. Build Data Projects

Career Growth:
Data Analyst → Data Scientist → AI Specialist
"""
    },


    "mathematics": {

        "field": "Mathematics & Research",

        "careers": [
            "Mathematician",
            "Statistician",
            "Actuary",
            "Data Scientist",
            "Financial Analyst",
            "Engineer"
        ],

        "skills": [
            "Advanced Mathematics",
            "Statistics",
            "Logical Thinking",
            "Problem Solving",
            "Analytics"
        ],

        "details":
        """
Mathematics careers use logical thinking and calculations.

Roadmap:
1. Strong Maths Foundation
2. Learn Statistics
3. Learn Programming
4. Practice Analytical Problems

Career Growth:
Analyst → Specialist → Researcher
"""
    },


    "biology": {

        "field": "Medical & Life Science",

        "careers": [
            "Doctor",
            "Pharmacist",
            "Biotechnologist",
            "Microbiologist",
            "Research Scientist"
        ],

        "skills": [
            "Biology",
            "Chemistry",
            "Research Skills",
            "Laboratory Skills",
            "Medical Knowledge"
        ],

        "details":
        """
Biology field focuses on living organisms, medicine and research.

Roadmap:
1. Study Biology Basics
2. Learn Laboratory Techniques
3. Research Skills
4. Specialization

Career Growth:
Student → Researcher → Scientist
"""
    },


    "commerce": {

        "field": "Business & Finance",

        "careers": [
            "Chartered Accountant",
            "Financial Analyst",
            "Investment Banker",
            "Business Manager",
            "Entrepreneur"
        ],

        "skills": [
            "Accounting",
            "Finance",
            "Excel",
            "Business Analysis",
            "Communication"
        ],

        "details":
        """
Commerce careers focus on money, business and management.

Roadmap:
1. Learn Accounting
2. Understand Finance
3. Learn Business Tools
4. Develop Communication

Career Growth:
Analyst → Manager → Business Leader
"""
    },


    "design": {

        "field": "Creative Design",

        "careers": [
            "Graphic Designer",
            "UI/UX Designer",
            "Animator",
            "Product Designer"
        ],

        "skills": [
            "Creativity",
            "Figma",
            "Photoshop",
            "Design Thinking",
            "User Experience"
        ],

        "details":
        """
Design combines creativity and technology.

Roadmap:
1. Learn Design Principles
2. Practice Tools
3. Create Portfolio
4. Work on Projects

Career Growth:
Designer → Senior Designer → Creative Director
"""
    },


    "mechanical": {

        "field": "Mechanical Engineering",

        "careers": [
            "Mechanical Engineer",
            "Automobile Engineer",
            "CAD Designer",
            "Production Engineer"
        ],

        "skills": [
            "CAD",
            "Thermodynamics",
            "Manufacturing",
            "Machine Design"
        ],

        "details":
        """
Mechanical field deals with machines and manufacturing.

Roadmap:
1. Engineering Basics
2. Learn CAD Software
3. Machine Design
4. Industrial Training
"""
    }

}



def get_response(user_input):
    
    print("LOGIC RECEIVED :", user_input)

    user_input = user_input.lower()


    if any(x in user_input for x in ["hi","hello","hey"]):

        return """
Hello 👋<br>
I am your Career Guidance Chatbot.

Tell me your interest:
Coding, Data Science, Mathematics,
Biology, Commerce, Design or Mechanical.
"""


    for key in career_data:

        if key in user_input:

            data = career_data[key]

            return f"""
<b>Field:</b> {data['field']} <br><br>

<b>Recommended Careers:</b><br>
• {'<br>• '.join(data['careers'])}

<br><br>

<b>Required Skills:</b><br>
• {'<br>• '.join(data['skills'])}

<br><br>

<b>Career Information:</b><br>
{data['details']}
"""


    if "career" in user_input:

        return """
Tell me your interests and I will suggest careers.

Example:
I like coding
I like biology
I like business
"""


    return """
I can guide you about careers.

Try:
coding
data science
mathematics
biology
commerce
design
mechanical
"""