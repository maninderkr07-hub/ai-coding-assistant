import ollama

def query_gemma(system_instructions, user_code_or_prompt):
    """Sends instructions and prompt to the local Gemma 4 model."""
    try:
        response = ollama.chat(
            model='gemma4:e2b', # Optimized lightweight model for 8GB RAM
            messages=[
                {'role': 'system', 'content': system_instructions},
                {'role': 'user', 'content': user_code_or_prompt}
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}. Make sure Ollama is running in your taskbar tray!"

def generate_code(prompt):
    system = "You are an expert software engineer. Generate clean, efficient code based on the request. Return ONLY the code block."
    return query_gemma(system, prompt)

def explain_code(code):
    system = "You are a teacher. Explain the following code step-by-step using plain language."
    return query_gemma(system, code)

def detect_bugs(code):
    system = "You are a debugger. Identify bugs in the code. Format: 1. Bug Found, 2. Reason, 3. Suggested Fix."
    return query_gemma(system, code)

def convert_code(code, target_language):
    system = f"Convert the provided code cleanly into {target_language}."
    return query_gemma(system, code)

def generate_docs(code):
    system = "Generate professional documentation and docstrings for the provided code."
    return query_gemma(system, code)

def generate_tests(code):
    system = "Generate standard unit test cases for the provided code snippet."
    return query_gemma(system, code)
