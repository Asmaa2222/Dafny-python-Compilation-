import ast
import json

class MethodVisitor(ast.NodeVisitor):
    def __init__(self):
        self.methods = []

    def visit_FunctionDef(self, node):
        # Skip '__init__' methods and others as needed
        if node.name not in ['__init__']:
            method_details = {
                'method_name': node.name,
                'parameters': [arg.arg for arg in node.args.args],
                'return_type': getattr(node.returns, 'id', 'None') if node.returns else 'None'
            }
            self.methods.append(method_details)

def analyze_python_code(code):
    tree = ast.parse(code)
    visitor = MethodVisitor()
    visitor.visit(tree)
    return visitor.methods

def main():
    # Read JSON file containing Python programs
    with open('python_programs.json', 'r') as file:
        program = json.load(file)  # Here, 'program' is a single dictionary
    
    print(f"Processing ID: {program['id']}")
    print(f"Description: {program['Description']}")
    print(f"Code: {program['Code']}")

    methods = analyze_python_code(program['Code'])

    # Prepare summary information
    summary_item = {
        'id': program['id'],
        'description': program['Description'],
        'code': program['Code'],
        'input': program['input'],
        'output': program['output'],
        'methods': methods
    }

    # Wrap summary_item in a list if you want a list of summaries
    summary = [summary_item]

    # Write the summary to the output JSON file
    with open('summary_python.json', 'w') as outfile:
        json.dump(summary, outfile, indent=4)
    
    print("Summary written to summary_python.json")

if __name__ == "__main__":
    main()
