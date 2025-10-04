# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(__name__, template_folder='FRONTEND')
CORS(app)

# ============= ROUTES FOR HTML PAGES =============
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animation')
def animation():
    return render_template('animation.html')

@app.route('/ba')
def ba():
    return render_template('ba.html')

@app.route('/bba')
def bba():
    return render_template('bba.html')

@app.route('/bca')
def bca():
    return render_template('bca.html')

@app.route('/bsc')
def bsc():
    return render_template('bsc.html')

@app.route('/btech')
def btech():
    return render_template('btech.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/law')
def law():
    return render_template('law.html')

@app.route('/logic')
def logic():
    return render_template('logic.html')

@app.route('/mbbs')
def mbbs():
    return render_template('mbbs.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

# ============= CAREER DATA =============
CAREER_DATA = {
    "software_engineer": {
        "title": "Software Engineer",
        "skills": ["programming", "coding", "python", "java", "algorithms"],
        "description": "Design, develop, and maintain software applications",
        "education": "BTech/BCA in Computer Science",
        "salary": "Rs 5-15 LPA",
    },
    "data_scientist": {
        "title": "Data Scientist",
        "skills": ["statistics", "machine learning", "python", "data analysis"],
        "description": "Analyze complex data to help make decisions",
        "education": "BTech/MSc in Data Science or Computer Science",
        "salary": "Rs 8-20 LPA",
    },
    "doctor": {
        "title": "Medical Doctor",
        "skills": ["biology", "medicine", "patient care", "mbbs"],
        "description": "Diagnose and treat illnesses",
        "education": "MBBS + MD/MS",
        "salary": "Rs 10-50 LPA",
    },
    "lawyer": {
        "title": "Lawyer",
        "skills": ["law", "legal", "constitution", "advocacy"],
        "description": "Provide legal advice and represent clients",
        "education": "LLB/LLM",
        "salary": "Rs 5-30 LPA",
    },
    "business_analyst": {
        "title": "Business Analyst",
        "skills": ["business", "analysis", "bba", "mba", "management"],
        "description": "Analyze business processes and suggest improvements",
        "education": "BBA/MBA",
        "salary": "Rs 6-18 LPA",
    },
}

# ============= TEST ROUTE =============
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"status": True, "message": "Backend is running!"})

# ============= CHATBOT API =============
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data received"}), 400
            
        message = data.get('message', '').lower()
        
        response_text = ""
        suggestions = []
        
        if any(word in message for word in ['hello', 'hi', 'hey']):
            response_text = "Hello! I'm your Career Guidance AI. Ask me about different careers, courses like BTech, MBBS, BBA, Law, or get career suggestions!"
            suggestions = ["Tell me about BTech", "What is Data Science?", "MBBS career info", "Suggest careers for me"]
        
        elif any(word in message for word in ['btech', 'engineering', 'b.tech']):
            response_text = "BTech (Bachelor of Technology) is a 4-year engineering degree. Popular branches:\n\nComputer Science - Software/IT careers\nMechanical - Manufacturing/Automotive\nCivil - Construction/Infrastructure\nElectrical - Power/Electronics\n\nCareers: Software Engineer, Data Scientist, Mechanical Engineer\nSalary: Rs 4-20 LPA"
            suggestions = ["Software Engineering career", "Mechanical Engineering", "Which BTech branch?"]
        
        elif any(word in message for word in ['mbbs', 'doctor', 'medical']):
            response_text = "MBBS (Bachelor of Medicine, Bachelor of Surgery) is a 5.5 year medical degree.\n\nWhat you'll do:\nDiagnose diseases\nTreat patients\nPerform surgeries\nMedical research\n\nCareer Path: MBBS to MD/MS to Specialist Doctor\nSalary: Rs 10-50 LPA\nTop Colleges: AIIMS, JIPMER, CMC"
            suggestions = ["Doctor salary", "After MBBS what?", "Medical entrance exams"]
        
        elif any(word in message for word in ['bba', 'business', 'management']):
            response_text = "BBA (Bachelor of Business Administration) is a 3-year management degree.\n\nSubjects:\nMarketing\nFinance\nHR Management\nOperations\n\nCareers: Business Analyst, HR Manager, Marketing Manager\nSalary: Rs 3-15 LPA\nAfter BBA: MBA for better opportunities"
            suggestions = ["MBA after BBA?", "BBA career options", "Business Analyst info"]
        
        elif any(word in message for word in ['law', 'lawyer', 'llb', 'advocate']):
            response_text = "Law Degrees:\n\nBA LLB - 5 years integrated\nLLB - 3 years after graduation\n\nCareer Options:\nCorporate Lawyer\nCriminal Lawyer\nCivil Lawyer\nJudge\n\nSalary: Rs 5-30 LPA\nTop Colleges: NLSIU Bangalore, NALSAR Hyderabad"
            suggestions = ["Types of lawyers", "Law entrance exams", "Lawyer salary"]
        
        elif any(word in message for word in ['bca', 'computer application']):
            response_text = "BCA (Bachelor of Computer Applications) is a 3-year IT degree.\n\nWhat you'll learn:\nProgramming (C, C++, Java, Python)\nWeb Development\nDatabase Management\nNetworking\n\nCareers: Software Developer, Web Developer, System Analyst\nSalary: Rs 3-12 LPA\nAfter BCA: MCA recommended"
            suggestions = ["BCA vs BTech?", "After BCA options", "Web Developer career"]
        
        elif any(word in message for word in ['bsc', 'science']):
            response_text = "BSc (Bachelor of Science) is a 3-year science degree.\n\nPopular Streams:\nBSc Physics\nBSc Chemistry\nBSc Mathematics\nBSc Computer Science\nBSc Biology\n\nCareers: Scientist, Teacher, Researcher, Data Analyst\nSalary: Rs 3-10 LPA\nAfter BSc: MSc, MCA, MBA options"
            suggestions = ["BSc Computer Science", "Research career", "After BSc options"]
        
        elif any(word in message for word in ['software', 'programming', 'coding']):
            career = CAREER_DATA['software_engineer']
            response_text = f"{career['title']}\n\n{career['description']}\n\nSkills Needed: {', '.join(career['skills'])}\nEducation: {career['education']}\nSalary: {career['salary']}\n\nJob Roles: Full Stack Developer, Backend Developer, Frontend Developer, Mobile App Developer"
            suggestions = ["What programming language?", "BTech needed?", "Salary growth"]
        
        elif any(word in message for word in ['data scien', 'machine learning', 'ai']):
            career = CAREER_DATA['data_scientist']
            response_text = f"{career['title']}\n\n{career['description']}\n\nSkills Needed: {', '.join(career['skills'])}\nEducation: {career['education']}\nSalary: {career['salary']}\n\nHot Field: AI/ML is booming in India! Companies like Google, Microsoft, Amazon are hiring."
            suggestions = ["How to learn AI?", "Data Science courses", "BTech needed?"]
        
        elif any(word in message for word in ['salary', 'earn', 'income', 'package']):
            response_text = "Average Starting Salaries in India:\n\nBTech CSE: Rs 6-12 LPA\nMBBS: Rs 8-15 LPA\nBBA/MBA: Rs 4-10 LPA\nLaw: Rs 5-12 LPA\nBCA: Rs 3-8 LPA\n\nSalary increases with experience! After 5-10 years, it can be 2-3x more."
            suggestions = ["Highest paying jobs", "Software Engineer salary", "Doctor salary"]
        
        elif any(word in message for word in ['suggest', 'recommend', 'which career', 'confused']):
            response_text = "I can help you find the right career! Tell me:\n\n1. What subjects do you like?\n   (Science, Math, Commerce, Arts)\n\n2. What are you interested in?\n   (Technology, Medicine, Business, Law, Creative)\n\n3. What's your goal?\n   (High salary, Help people, Creative work, Research)"
            suggestions = ["I like computers", "I like biology", "I like business", "I like math"]
        
        elif any(word in message for word in ['computer', 'technology', 'tech']):
            response_text = "Technology Careers Perfect for You:\n\n1. Software Engineer - Build apps/websites\n2. Data Scientist - Work with data/AI\n3. Cyber Security - Protect systems\n4. Game Developer - Create games\n\nEducation: BTech CSE or BCA\nSalary: Rs 5-20 LPA"
            suggestions = ["BTech CSE info", "BCA details", "Software Engineer"]
        
        elif any(word in message for word in ['biology', 'medical', 'help people']):
            response_text = "Medical/Healthcare Careers:\n\n1. Doctor (MBBS) - Treat patients\n2. Pharmacist - Medicine expert\n3. Physiotherapist - Physical therapy\n4. Nursing - Patient care\n\nTop Choice: MBBS if you want to become a doctor\nSalary: Rs 8-50 LPA"
            suggestions = ["MBBS details", "NEET exam", "Doctor career"]
        
        elif any(word in message for word in ['business', 'commerce', 'management']):
            response_text = "Business/Management Careers:\n\n1. Business Analyst - Analyze business\n2. Marketing Manager - Promote products\n3. CA (Chartered Accountant) - Finance\n4. HR Manager - Manage people\n\nEducation: BBA to MBA\nSalary: Rs 4-20 LPA"
            suggestions = ["BBA details", "CA vs MBA?", "Business Analyst"]
        
        elif any(word in message for word in ['math', 'mathematics', 'calculation']):
            response_text = "Math-Based Careers:\n\n1. Data Scientist - Use statistics/ML\n2. Financial Analyst - Work with money\n3. Actuary - Calculate risks\n4. Research Scientist - Mathematical research\n\nEducation: BSc Math, BTech, or BCA\nSalary: Rs 5-18 LPA"
            suggestions = ["Data Science", "Financial careers", "BTech branches"]
        
        else:
            response_text = "I can help you with:\n\nCourses: BTech, MBBS, BBA, Law, BCA, BSc\nCareers: Software Engineer, Doctor, Lawyer, Business Analyst\nSalary Info\nCareer Suggestions\n\nWhat would you like to know?"
            suggestions = ["Tell me about BTech", "Career options", "Salary info"]
        
        return jsonify({
            "response": response_text,
            "suggestions": suggestions
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============= RUN APP =============
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)