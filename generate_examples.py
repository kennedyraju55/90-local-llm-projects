"""
Script to generate examples/ directory with demo.py and README.md for all 90 projects.
Reads each project's core.py, extracts function signatures, and creates tailored demos.
"""
import ast
import os
import re
import textwrap

BASE = r"C:\Users\raguthik\projects\90-local-llm-projects"


def get_project_dirs():
    """Get all 90 project directories sorted."""
    dirs = []
    for name in sorted(os.listdir(BASE)):
        path = os.path.join(BASE, name)
        if os.path.isdir(path) and re.match(r'^\d{2}-', name):
            dirs.append((name, path))
    return dirs


def get_module_name(proj_path):
    """Get the Python module name from src/."""
    src_dir = os.path.join(proj_path, "src")
    if not os.path.isdir(src_dir):
        return None
    for item in sorted(os.listdir(src_dir)):
        item_path = os.path.join(src_dir, item)
        if os.path.isdir(item_path) and not item.startswith('__') and '.egg-info' not in item:
            return item
    return None


def get_project_title(dir_name):
    """Convert directory name to human-readable title."""
    # Remove number prefix
    name = re.sub(r'^\d{2}-', '', dir_name)
    return name.replace('-', ' ').title()


def extract_functions(core_path):
    """Extract function definitions from core.py using AST."""
    with open(core_path, 'r', encoding='utf-8') as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return [], source

    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Skip private functions
            if node.name.startswith('_'):
                continue
            params = []
            for arg in node.args.args:
                if arg.arg == 'self':
                    continue
                # Extract type annotation if present
                type_hint = None
                if arg.annotation:
                    try:
                        type_hint = ast.unparse(arg.annotation)
                    except Exception:
                        pass
                params.append((arg.arg, type_hint))
            # Get defaults
            defaults = node.args.defaults
            num_defaults = len(defaults)
            num_params = len(params)
            param_info = []
            for i, (p, th) in enumerate(params):
                has_default = i >= (num_params - num_defaults)
                param_info.append((p, has_default, th))

            docstring = ast.get_docstring(node) or ""
            functions.append({
                'name': node.name,
                'params': param_info,
                'docstring': docstring,
                'lineno': node.lineno,
            })

    return functions, source


def extract_classes(core_path):
    """Extract class definitions from core.py."""
    with open(core_path, 'r', encoding='utf-8') as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    classes = []
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef):
            methods = []
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and not item.name.startswith('_'):
                    params = []
                    for arg in item.args.args:
                        if arg.arg == 'self':
                            continue
                        type_hint = None
                        if arg.annotation:
                            try:
                                type_hint = ast.unparse(arg.annotation)
                            except Exception:
                                pass
                        params.append((arg.arg, False, type_hint))
                    methods.append({
                        'name': item.name,
                        'params': params,
                        'docstring': ast.get_docstring(item) or "",
                    })
            # Also grab __init__ params
            init_params = []
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == '__init__':
                    for arg in item.args.args:
                        if arg.arg == 'self':
                            continue
                        type_hint = None
                        if arg.annotation:
                            try:
                                type_hint = ast.unparse(arg.annotation)
                            except Exception:
                                pass
                        has_default = False
                        init_params.append((arg.arg, has_default, type_hint))

            classes.append({
                'name': node.name,
                'init_params': init_params,
                'methods': methods,
                'docstring': ast.get_docstring(node) or "",
            })
    return classes


# Sample data generators for different parameter names
SAMPLE_VALUES = {
    # Text/content
    'text': '"The quick brown fox jumps over the lazy dog. This is a sample text for demonstration purposes."',
    'content': '"The quick brown fox jumps over the lazy dog. This is sample content for demonstration."',
    'raw_content': '"Raw text content here for processing and analysis."',
    'message': '"Hello! I need help with a question about this project."',
    'query': '"What are the main features?"',
    'question': '"What are the key points in this document?"',
    'prompt': '"Explain the concept in simple terms."',
    'input_text': '"This is a sample input text for processing and analysis."',
    'user_input': '"I need help understanding this topic."',
    'user_message': '"Can you help me with this?"',
    'system_prompt': '"You are a helpful assistant."',

    # Code-related
    'code': '"def hello():\\n    return \'Hello, World!\'"',
    'source_code': '"def add(a, b):\\n    return a + b\\n\\nresult = add(1, 2)\\nprint(result)"',
    'snippet': '"for i in range(10):\\n    print(i)"',
    'source': '"def process(data):\\n    return [x * 2 for x in data]"',
    'code_info': '{"language": "python", "code": "def greet(name):\\n    return f\'Hello, {name}!\'"} ',
    'commit_diff': '"diff --git a/app.py b/app.py\\n--- a/app.py\\n+++ b/app.py\\n@@ -1,3 +1,5 @@\\n+import logging\\n def main():\\n-    print(\\"hello\\")\\n+    logging.info(\\"Starting app\\")"',
    'diff': '"--- a/utils.py\\n+++ b/utils.py\\n@@ -5,3 +5,6 @@\\n def process(data):\\n-    return data\\n+    return data.strip()"',
    'stack_trace': '"Traceback (most recent call last):\\n  File \\"app.py\\", line 10\\nZeroDivisionError: division by zero"',
    'trace': '"Traceback (most recent call last):\\n  File \\"main.py\\", line 5\\nValueError: invalid literal"',
    'error_text': '"TypeError: cannot unpack non-sequence NoneType"',
    'regex_description': '"Match email addresses"',
    'pattern': '"email addresses"',
    'sql_description': '"Find all users who signed up in the last 30 days"',
    'natural_language': '"Show me all orders from last month with total over $100"',
    'schema': '"users(id INT, name TEXT, email TEXT, created_at DATE); orders(id INT, user_id INT, total DECIMAL)"',
    'schema_text': '"CREATE TABLE users (id INT PRIMARY KEY, name TEXT, email TEXT);\\nCREATE TABLE orders (id INT, user_id INT, total DECIMAL);"',
    'dialect': '"postgresql"',
    'language': '"python"',
    'lang': '"python"',
    'target_language': '"javascript"',
    'source_language': '"python"',
    'target_lang': '"javascript"',
    'source_lang': '"python"',
    'pipeline_type': '"python"',

    # File paths
    'pdf_path': '"sample.pdf"',
    'pdf_paths': '["sample.pdf"]',
    'file_path': '"sample.txt"',
    'file_paths': '["sample.txt"]',
    'filepath': '"sample.txt"',
    'path': '"."',
    'source_path': '"."',
    'output_path': '"output.txt"',
    'config_path': '"config.yaml"',
    'csv_path': '"sample.csv"',
    'log_file': '"app.log"',
    'history_file': '"history.json"',
    'bookmarks_file': '"bookmarks.json"',
    'stories_file': '"stories.json"',
    'trends_file': '"trends.json"',
    'cache_path': '"cache.json"',
    'directory': '"."',

    # URLs/email
    'url': '"https://example.com"',
    'email': '"user@example.com"',
    'email_body': '"Thank you for your interest in our product. We would love to schedule a demo."',

    # Identity
    'name': '"John Doe"',
    'person': '"Alice Johnson"',
    'title': '"Sample Project Title"',
    'topic': '"artificial intelligence and machine learning"',
    'subject': '"Introduction to Python Programming"',
    'description': '"A comprehensive guide to building modern applications."',
    'summary': '"This document covers the basics of machine learning."',
    'company': '"TechCorp Inc."',
    'industry': '"technology"',
    'product': '"Smart Assistant Pro"',
    'product_name': '"Smart Water Bottle"',
    'product_features': '["temperature display", "hydration reminders", "BPA-free", "24-hour insulation"]',
    'service_name': '"web-app"',
    'app_name': '"my-awesome-app"',

    # Data structures
    'data': '{"name": "Sample", "value": 42, "items": ["a", "b", "c"]}',
    'config': 'None  # Uses default config',
    'cfg': 'None  # Uses default config',
    'config_data': '{"app_name": "myapp", "services": ["web", "api", "worker"]}',
    'csv_data': '"Name,Age,City\\nAlice,30,NYC\\nBob,25,LA\\nCharlie,35,Chicago"',
    'history': '[]',
    'conversation_history': '[]',
    'messages': '[]',
    'context': '"This is the context information for the query."',
    'chunks': '["Chunk 1: Important information here.", "Chunk 2: More relevant details."]',
    'documents': '["Document 1: First document content.", "Document 2: Second document content."]',
    'articles': '["Tech giant announces new AI model.", "Stock markets reach all-time high."]',
    'entries': '[]',
    'notes': '[]',
    'results': '[]',
    'items': '["item1", "item2", "item3"]',
    'tags': '["python", "tutorial"]',
    'keywords': '["machine learning", "AI", "data science"]',
    'categories': '["tech", "science", "health"]',
    'services': '["web", "api", "database", "cache"]',
    'files': '["file1.py", "file2.py"]',
    'members': '["Alice", "Bob", "Charlie"]',
    'words': '["serendipity", "ephemeral", "ubiquitous"]',
    'themes': '["innovation", "sustainability"]',
    'topics': '["AI", "cloud computing", "cybersecurity"]',
    'indicators': '[]',
    'sections': '[]',
    'slides': '[]',

    # LLM parameters
    'model': '"gemma4"',
    'temperature': '0.7',
    'top_k': '3',
    'num_results': '5',
    'max_tokens': '500',

    # Resume/job
    'resume_text': '"John Doe\\nSoftware Engineer\\n5 years experience in Python, Java, and cloud services."',
    'resume': '"John Doe\\nSoftware Engineer\\nExperience: 5 years Python, AWS"',
    'jd_text': '"Senior Python developer with 5+ years experience in cloud services."',
    'job_description': '"Looking for a senior software engineer with Python and cloud experience."',
    'skill_match': '{"matched": ["Python", "AWS"], "missing": ["Go"]}',

    # Medical
    'symptoms': '["headache", "fever", "fatigue"]',
    'medication': '"ibuprofen"',
    'medications': '["aspirin", "ibuprofen"]',
    'drug_name': '"aspirin"',
    'drug_a': '"aspirin"',
    'drug_b': '"ibuprofen"',
    'term': '"hypertension"',
    'medical_term': '"myocardial infarction"',
    'ehr_text': '"Patient John Smith (DOB: 01/15/1990, SSN: 123-45-6789) visited Dr. Jane Doe on 03/15/2024."',
    'health_goals': '"Improve cardiovascular health and reduce stress"',
    'nutrition_label': '"Calories: 250, Total Fat: 8g, Sodium: 480mg, Total Carbs: 35g, Protein: 12g"',
    'scan_data': '{"type": "blood_test", "results": {"glucose": 95, "cholesterol": 180}}',

    # Logs/Security
    'log_data': '"2024-01-15 10:30:00 ERROR Failed to connect to database\\n2024-01-15 10:30:01 INFO Retrying"',
    'log_content': '"2024-01-15 10:30:00 ERROR Failed to connect\\n2024-01-15 10:30:01 INFO Retry succeeded"',
    'logs': '"2024-01-15 10:30:00 ERROR Connection failed\\n2024-01-15 10:31:00 INFO Recovered"',
    'alert': '"CVE-2024-1234: Critical vulnerability in OpenSSL affecting versions < 3.0"',
    'alert_text': '"CRITICAL: Unauthorized access attempt detected from IP 192.168.1.100"',
    'incident': '"Database server became unresponsive at 14:30 UTC"',
    'incident_description': '"Web application returned 500 errors for 15 minutes during peak traffic"',
    'incident_type': '"outage"',
    'severity': '"HIGH"',
    'password': '"MyP@ssw0rd123!"',
    'vuln_data': '{"cve": "CVE-2024-1234", "severity": "HIGH", "affected": "OpenSSL < 3.0"}',
    'findings': '["SQL injection in login form", "XSS in search field"]',

    # Policy/Legal
    'policy_text': '"Our company collects user email addresses for marketing purposes."',
    'document_text': '"The parties agree to the following terms and conditions..."',
    'paper_text': '"This research paper explores the effects of machine learning on healthcare outcomes..."',

    # Mood/Journal/Personal
    'mood': '"feeling productive and optimistic today"',
    'mood_text': '"I felt really anxious this morning but better after lunch"',
    'entry': '"Today was a great day. I finished my project and went for a walk."',
    'journal_entry': '"Today I completed a major milestone at work. Feeling accomplished!"',
    'diary_entry': '"Dear diary, today was eventful. Had a great meeting and learned new things."',
    'budget_data': '{"income": 5000, "expenses": {"rent": 1500, "food": 600, "transport": 200}}',
    'expenses': '[{"category": "rent", "amount": 1500}, {"category": "food", "amount": 600}]',

    # Food/Fitness
    'recipe': '"pasta with tomato sauce"',
    'ingredients': '["chicken", "rice", "broccoli", "soy sauce"]',
    'preferences': '{"diet": "balanced", "allergies": [], "cuisine": "any"}',
    'dietary_preferences': '"vegetarian, no nuts"',
    'diet': '"balanced"',
    'fitness_goal': '"lose weight and build muscle"',
    'exercise': '"bench press"',
    'goal': '"improve overall fitness"',

    # Travel
    'destination': '"Tokyo, Japan"',
    'duration': '7',
    'duration_minutes': '60',
    'days': '7',
    'travelers': '2',
    'interests': '["technology", "history", "food"]',

    # Education
    'word': '"serendipity"',
    'grade_level': '"high school"',
    'level': '"intermediate"',
    'difficulty': '"medium"',
    'essay': '"Climate change is one of the most pressing issues of our time..."',
    'essay_text': '"The impact of social media on modern communication has been profound..."',
    'rubric': '"Content: 40%, Organization: 30%, Grammar: 20%, Style: 10%"',
    'category': '"general knowledge"',
    'quiz_data': '{"topic": "Python basics", "questions": []}',
    'num_questions': '5',
    'num_topics': '3',
    'user_answers': '[]',
    'flashcard_topic': '"Spanish vocabulary for beginners"',
    'num_cards': '5',
    'curriculum_subject': '"Introduction to Data Science"',
    'experiment_topic': '"photosynthesis"',
    'math_problem': '"Solve for x: 2x + 5 = 15"',
    'historical_topic': '"The Renaissance period in Europe"',
    'debate_topic': '"Should artificial intelligence be regulated?"',
    'reading_passage': '"The development of renewable energy sources has accelerated in recent years..."',
    'chapters': '["Introduction", "Methods", "Results", "Conclusion"]',
    'deck': '[]',
    'deck_name': '"Python Basics"',
    'card': '{"front": "What is a list?", "back": "An ordered collection of items"}',
    'progress': '{}',

    # Gift/Shopping
    'occasion': '"birthday"',
    'recipient': '"tech-savvy friend who loves cooking"',
    'budget': '50',
    'age': '30',
    'gender': '"any"',
    'relationship': '"friend"',
    'gift_name': '"Smart Watch"',

    # Business
    'competitor_name': '"Competitor Inc"',
    'competitors': '["Competitor A", "Competitor B"]',
    'ticket_text': '"My login is not working. I get an error when trying to reset my password."',
    'tickets': '["Login not working", "Page loads slowly", "Cannot upload files"]',
    'financial_data': '{"revenue": 1000000, "expenses": 750000, "profit": 250000, "quarter": "Q4 2024"}',
    'kpi_data': '{"metric": "Monthly Active Users", "current": 50000, "target": 60000, "previous": 45000}',
    'metrics': '{"users": 50000, "revenue": 100000, "churn": 0.05}',
    'trend_data': '[100, 120, 115, 130, 145, 140, 160, 175, 170, 190]',
    'stock_data': '{"ticker": "AAPL", "price": 195.50, "change": 2.3, "volume": 54000000}',
    'ticker': '"AAPL"',
    'prospect': '{"name": "Jane Doe", "company": "TechCorp", "role": "CTO"}',
    'prospect_info': '{"name": "Jane Doe", "company": "TechCorp", "role": "CTO"}',
    'campaign': '{"name": "Summer Sale", "type": "promotional"}',
    'campaign_type': '"promotional"',
    'swot': '{"strengths": ["Innovation"], "weaknesses": ["Small team"]}',
    'segment': '"enterprise"',

    # Content creation
    'blog_topic': '"The Future of AI in Healthcare"',
    'social_topic': '"Launch of our new product"',
    'platform': '"twitter"',
    'email_topic': '"New product launch announcement"',
    'audience': '"tech professionals aged 25-45"',
    'newsletter_content': '"This month we launched three new features..."',
    'poem_topic': '"the beauty of a sunset over the ocean"',
    'style': '"professional"',
    'tone': '"friendly and professional"',
    'genre': '"science fiction"',
    'theme': '"innovation"',
    'video_topic': '"How to start a vegetable garden"',
    'story_premise': '"A robot discovers it can dream"',
    'premise': '"A robot discovers it can dream"',
    'presentation_topic': '"Quarterly Business Review Q4 2024"',
    'slides_count': '10',
    'length': '"medium"',
    'format_type': '"markdown"',
    'output_format': '"markdown"',
    'template': '"default"',
    'template_id': '"default"',
    'num_emails': '3',
    'num_suggestions': '3',
    'plot_structure': '"three-act"',
    'characters': '["Alice", "Bob"]',
    'worldbuilding': '"A futuristic city"',
    'cover_letter_info': '{"name": "Jane Smith", "position": "Data Scientist", "company": "TechCorp"}',

    # Document processing
    'invoice_text': '"Invoice #1234\\nDate: 2024-01-15\\nItem: Consulting Services\\nAmount: $5,000.00"',
    'invoices': '["Invoice #1: $500", "Invoice #2: $1200"]',
    'meeting_transcript': '"Alice: Let\'s discuss Q4.\\nBob: Focus on performance.\\nAlice: Agreed."',
    'transcript': '"Alice: Let\'s discuss Q4.\\nBob: Focus on performance.\\nAlice: Agreed."',
    'news_articles': '["Tech giant announces new AI model.", "Stock markets reach all-time high."]',
    'sentiment_text': '"I absolutely love this product! It exceeded all my expectations."',
    'sentiments': '["positive", "neutral", "negative", "positive"]',
    'review_text': '"The service was okay but delivery took too long. Product quality is decent."',
    'survey_responses': '["Great product!", "Needs improvement in shipping", "Love the customer service"]',
    'responses': '["Good experience", "Could be better", "Excellent service"]',
    'classifications': '["bug", "feature_request", "question"]',
    'categorization': '{"type": "bug", "priority": "high"}',
    'classification': '{"type": "bug", "priority": "high"}',

    # Calendar/Time
    'event': '{"title": "Team Meeting", "date": "2024-02-15", "time": "10:00", "duration": "1 hour"}',
    'events': '[{"title": "Meeting", "date": "2024-02-15"}, {"title": "Lunch", "date": "2024-02-15"}]',
    'date': '"2024-02-15"',
    'timezone': '"UTC"',
    'available_hours': '8',
    'period': '"weekly"',
    'weeks': '4',
    'focus': '"productivity"',
    'focus_areas': '["health", "career", "learning"]',
    'priority': '"high"',

    # Knowledge/Reading
    'knowledge_item': '"Python decorators are functions that modify the behavior of other functions."',
    'book_title': '"The Pragmatic Programmer"',
    'book': '{"title": "Clean Code", "author": "Robert C. Martin", "status": "to_read"}',
    'note_id': '"note-001"',

    # Home/Personal
    'automation_request': '"Turn on the living room lights at sunset"',
    'family_member': '"grandma"',
    'family_story': '"Tell a story about grandma\'s garden"',
    'habit': '"exercise"',
    'habit_data': '{"habit": "exercise", "completed": [True, True, False, True, True, False, True]}',
    'standup_data': '{"yesterday": "Completed API integration", "today": "Write unit tests", "blockers": "None"}',
    'tasks': '["Write report", "Review PRs", "Team meeting at 2pm", "Deploy to staging"]',
    'sleep_data': '{"hours": 6.5, "quality": "fair", "wake_ups": 2}',
    'quality': '"good"',
    'stress_level': '7',
    'stress_description': '"Feeling overwhelmed with work deadlines and not sleeping well"',
    'first_aid_scenario': '"Someone has a minor burn on their hand from touching a hot pan"',

    # DevOps
    'env_vars': '{"DATABASE_URL": "postgres://localhost/mydb", "API_KEY": "xxx", "DEBUG": "true"}',
    'env': '"production"',
    'docker_requirements': '"Python 3.11 web app with PostgreSQL and Redis"',
    'config_type': '"docker-compose"',

    # Numeric
    'number': '5',
    'count': '5',
    'n': '5',
    'k': '3',
    'size': '10',
    'limit': '10',
    'score': '85',
    'total': '100',
    'threshold': '0.5',
    'index': '0',
    'depth': '2',

    # DataFrame
    'df': 'None  # Pass a pandas DataFrame',
    'text_col': '"text"',
    'fmt': '"markdown"',

    # Misc callable
    'chat_fn': 'None  # Uses default LLM chat function',

    # Report
    'report_topic': '"Monthly Security Audit Report"',
    'breakdown': '{"category1": 60, "category2": 40}',
    'detail_level': '"detailed"',

    # Story
    'story': '"Once upon a time in a digital world..."',
}


def get_sample_value(param_name, source_code="", type_hint=None):
    """Get a sample value for a parameter based on its name and type hint."""
    # If we have a type hint, use that first
    if type_hint:
        th = type_hint.lower().strip()
        if th == 'bool':
            return 'True'
        if th == 'int':
            return '5'
        if th == 'float':
            return '0.7'
        if th.startswith('list') or th.startswith('list['):
            if 'str' in th:
                return '["item1", "item2", "item3"]'
            if 'int' in th:
                return '[1, 2, 3]'
            if 'dict' in th:
                return '[{"key": "value"}]'
            return '[]'
        if th.startswith('dict') or th.startswith('dict['):
            return '{}'
        if th.startswith('optional'):
            return 'None'

    # Direct match
    if param_name in SAMPLE_VALUES:
        return SAMPLE_VALUES[param_name]

    # Partial matches (longer keys first for better specificity, min 4 chars to avoid false matches)
    sorted_keys = sorted(SAMPLE_VALUES.keys(), key=len, reverse=True)
    for key in sorted_keys:
        if len(key) < 4:
            continue
        if key in param_name or param_name in key:
            return SAMPLE_VALUES[key]

    # Type-based fallbacks
    pn = param_name.lower()
    if 'list' in pn or 'items' in pn:
        return '["item1", "item2", "item3"]'
    if 'dict' in pn or 'config' in pn or 'options' in pn or 'settings' in pn:
        return '{}'
    if 'num' in pn or 'count' in pn or 'max' in pn or 'min' in pn:
        return '5'
    if 'flag' in pn or 'enable' in pn or pn.startswith('is_') or pn.startswith('has_'):
        return 'True'
    if 'path' in pn or 'file' in pn or 'dir' in pn:
        return '"sample.txt"'
    if 'output' in pn:
        return '"output.txt"'
    if 'text' in pn or 'string' in pn or 'str' in pn:
        return '"sample text"'
    if 'fn' in pn or 'func' in pn or 'callback' in pn:
        return 'None'

    return '"sample data"'


def generate_demo(proj_name, module_name, functions, classes, source):
    """Generate a demo.py script tailored to the project."""
    title = get_project_title(proj_name)

    lines = []
    lines.append(f'"""')
    lines.append(f'Demo script for {title}')
    lines.append(f'Shows how to use the core module programmatically.')
    lines.append(f'')
    lines.append(f'Usage:')
    lines.append(f'    python examples/demo.py')
    lines.append(f'"""')
    lines.append(f'import os')
    lines.append(f'import sys')
    lines.append(f'')
    lines.append(f'# Add project root to path')
    lines.append(f"sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))")
    lines.append(f'')

    # Build import line - import specific functions/classes
    importables = []
    for func in functions:
        importables.append(func['name'])
    for cls in classes:
        importables.append(cls['name'])

    if importables:
        import_names = ", ".join(importables[:10])  # limit to 10
        lines.append(f'from src.{module_name}.core import {import_names}')
    else:
        lines.append(f'from src.{module_name}.core import *')
    lines.append(f'')
    lines.append(f'')
    lines.append(f'def main():')
    lines.append(f'    """Run a quick demo of {title}."""')
    lines.append(f'    print("=" * 60)')
    lines.append(f'    print("🚀 {title} - Demo")')
    lines.append(f'    print("=" * 60)')
    lines.append(f'    print()')

    # Generate demo calls
    if not functions and not classes:
        lines.append(f'    print("📝 Module loaded successfully!")')
        lines.append(f'    print("   Check the source code for available functions.")')
    else:
        demo_count = 0
        max_demos = 4

        # Demo top-level functions first
        for func in functions:
            if demo_count >= max_demos:
                break

            fname = func['name']
            doc = func['docstring']
            params = func['params']

            # Build function call
            args = []
            for param_tuple in params:
                pname = param_tuple[0]
                has_default = param_tuple[1]
                type_hint = param_tuple[2] if len(param_tuple) > 2 else None
                if has_default:
                    continue  # skip optional params
                if pname in ('self',):
                    continue
                val = get_sample_value(pname, source, type_hint)
                args.append(f"{pname}={val}")

            args_str = ", ".join(args)

            desc = doc.split('\n')[0] if doc else f"Using {fname}"
            lines.append(f'    # {desc}')
            lines.append(f'    print("📝 Example: {fname}()")')

            if args_str:
                lines.append(f'    result = {fname}(')
                for i, a in enumerate(args):
                    comma = "," if i < len(args) - 1 else ""
                    lines.append(f'        {a}{comma}')
                lines.append(f'    )')
            else:
                lines.append(f'    result = {fname}()')

            lines.append(f'    print(f"   Result: {{result}}")')
            lines.append(f'    print()')
            demo_count += 1

        # Demo classes
        for cls in classes:
            if demo_count >= max_demos:
                break

            cname = cls['name']
            init_params = cls['init_params']
            methods = cls['methods']
            doc = cls['docstring']

            # Build constructor call
            init_args = []
            for param_tuple in init_params:
                pname = param_tuple[0]
                has_default = param_tuple[1]
                type_hint = param_tuple[2] if len(param_tuple) > 2 else None
                if has_default:
                    continue
                val = get_sample_value(pname, source, type_hint)
                init_args.append(f"{pname}={val}")

            init_args_str = ", ".join(init_args)
            var_name = cname[0].lower() + cname[1:] if cname else "obj"
            # Make it a simple snake_case variable
            var_name = re.sub(r'(?<!^)(?=[A-Z])', '_', var_name).lower()

            desc = doc.split('\n')[0] if doc else f"Using {cname}"
            lines.append(f'    # {desc}')
            lines.append(f'    print("📝 Example: {cname}")')
            if init_args:
                lines.append(f'    {var_name} = {cname}(')
                for i, a in enumerate(init_args):
                    comma = "," if i < len(init_args) - 1 else ""
                    lines.append(f'        {a}{comma}')
                lines.append(f'    )')
            else:
                lines.append(f'    {var_name} = {cname}()')

            # Call first public method
            if methods:
                m = methods[0]
                method_args = []
                for param_tuple in m['params']:
                    pname = param_tuple[0]
                    type_hint = param_tuple[2] if len(param_tuple) > 2 else None
                    val = get_sample_value(pname, source, type_hint)
                    method_args.append(f"{pname}={val}")
                method_args_str = ", ".join(method_args)
                if method_args:
                    lines.append(f'    result = {var_name}.{m["name"]}(')
                    for i, a in enumerate(method_args):
                        comma = "," if i < len(method_args) - 1 else ""
                        lines.append(f'        {a}{comma}')
                    lines.append(f'    )')
                else:
                    lines.append(f'    result = {var_name}.{m["name"]}()')
                lines.append(f'    print(f"   Result: {{result}}")')
            else:
                lines.append(f'    print(f"   Created: {{{var_name}}}")')

            lines.append(f'    print()')
            demo_count += 1

    lines.append(f'    print("✅ Demo complete! See README.md for more examples.")')
    lines.append(f'')
    lines.append(f'')
    lines.append(f'if __name__ == "__main__":')
    lines.append(f'    main()')
    lines.append(f'')

    return "\n".join(lines)


def generate_readme(proj_name, module_name, functions, classes):
    """Generate examples/README.md."""
    title = get_project_title(proj_name)

    lines = [
        f"# Examples for {title}",
        f"",
        f"This directory contains example scripts demonstrating how to use this project.",
        f"",
        f"## Quick Demo",
        f"",
        f"```bash",
        f"python examples/demo.py",
        f"```",
        f"",
        f"## What the Demo Shows",
        f"",
    ]

    for func in functions[:5]:
        doc = func['docstring'].split('\n')[0] if func['docstring'] else f"Call {func['name']}"
        lines.append(f"- **`{func['name']}()`** — {doc}")

    for cls in classes[:3]:
        doc = cls['docstring'].split('\n')[0] if cls['docstring'] else f"Use {cls['name']}"
        lines.append(f"- **`{cls['name']}`** — {doc}")

    lines.extend([
        f"",
        f"## Prerequisites",
        f"",
        f"- Python 3.10+",
        f"- Ollama running with Gemma 4 model",
        f"- Project dependencies installed (`pip install -e .`)",
        f"",
        f"## Running",
        f"",
        f"From the project root directory:",
        f"",
        f"```bash",
        f"# Install the project in development mode",
        f"pip install -e .",
        f"",
        f"# Run the demo",
        f"python examples/demo.py",
        f"```",
        f"",
    ])

    return "\n".join(lines)


def main():
    projects = get_project_dirs()
    print(f"Found {len(projects)} projects")

    created = 0
    errors = []

    for proj_name, proj_path in projects:
        module_name = get_module_name(proj_path)
        if not module_name:
            errors.append(f"{proj_name}: No module found in src/")
            continue

        core_path = os.path.join(proj_path, "src", module_name, "core.py")
        if not os.path.exists(core_path):
            errors.append(f"{proj_name}: No core.py found at {core_path}")
            continue

        functions, source = extract_functions(core_path)
        classes = extract_classes(core_path)

        # Create examples directory
        examples_dir = os.path.join(proj_path, "examples")
        os.makedirs(examples_dir, exist_ok=True)

        # Generate demo.py
        demo_content = generate_demo(proj_name, module_name, functions, classes, source)
        demo_path = os.path.join(examples_dir, "demo.py")
        with open(demo_path, 'w', encoding='utf-8') as f:
            f.write(demo_content)

        # Generate README.md
        readme_content = generate_readme(proj_name, module_name, functions, classes)
        readme_path = os.path.join(examples_dir, "README.md")
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        print(f"  OK {proj_name} ({module_name}): {len(functions)} functions, {len(classes)} classes")
        created += 1

    print(f"\nCreated examples for {created}/{len(projects)} projects")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  ❌ {e}")


if __name__ == "__main__":
    main()
