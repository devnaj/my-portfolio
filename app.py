import sys
import pkgutil
import importlib.util
import os

# PYTHON 3.14 COMPATIBILITY FIXES
if not hasattr(pkgutil, 'get_loader'):
    def get_loader(name):
        return importlib.util.find_spec(name)
    pkgutil.get_loader = get_loader

if __name__ == '__main__' and sys.modules['__main__'].__spec__ is None:
    import importlib.machinery
    loader = importlib.machinery.SourceFileLoader('__main__', os.path.abspath(__file__))
    sys.modules['__main__'].__spec__ = importlib.util.spec_from_loader('__main__', loader)

from flask import Flask, render_template

app = Flask(__name__, instance_path=os.path.abspath(os.path.dirname(__file__)))

@app.route('/')
def home():
    user_info = {
        "name": "Devna J",
        "bio": "I am a highly motivated Mathematics graduate from St. Joseph's College (71.92%) with a deep passion for logical reasoning and algorithmic problem-solving. Currently pursuing my MCA at Rajagiri College of Social Sciences, I am leveraging my strong analytical foundation to build efficient, scalable software solutions. My background in Graph Theory allows me to approach coding challenges with a unique, optimization-first mindset. I am proficient in Python, Django, Java, and C++, and I am dedicated to continuous learning in the field of Web Application Development.",
        "linkedin": "https://linkedin.com/in/devna-j-2a54b5372"
    }
    
    education = [
        {"level": "MCA", "school": "Rajagiri College of Social Sciences", "score": "Pursuing"},
        {"level": "BSc Mathematics", "school": "St. Joseph's College (Autonomous), Devagiri", "score": "71.92%"},
        {"level": "Class 12 (AISSCE)", "school": "Toc H Public School", "score": "92%"},
        {"level": "Class 10 (AISSE)", "school": "Amrutha Public School", "score": "95.4%"}
    ]
    
    project = {
        "title": "Graph Coloring & Algorithmic Optimization",
        "details": "Applied Graph Theory to solve vertex coloring constraints for resource optimization. Analyzed NP-Complete complexity to design efficient algorithms for compiler and wireless communication applications."
    }

    return render_template('index.html', user=user_info, edu_list=education, proj=project)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)