import ast
import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: The file does not exist.")
        exit(1)
    except OSError:
        print("Error: Unable to read the file. Please check the file path and permissions.")
        exit(1)

def analyze_file(content):
    tree = ast.parse(content)
    classes = []
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_info = {
                "name": node.name,
                "docstring": ast.get_docstring(node) or "Not found",
                "methods": [],
                "naming_issue": not is_camel_case(node.name)
            }
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    method_info = {
                        "name": item.name,
                        "docstring": ast.get_docstring(item) or "Not found",
                        "naming_issue": not is_snake_case(item.name)
                    }
                    class_info["methods"].append(method_info)
            classes.append(class_info)
        elif isinstance(node, ast.FunctionDef):
            if not any(isinstance(parent, ast.ClassDef) for parent in ast.walk(node)):
                function_info = {
                    "name": node.name,
                    "docstring": ast.get_docstring(node) or "Not found",
                    "naming_issue": not is_snake_case(node.name)
                }
                functions.append(function_info)

    return {
        "lines": len(content.splitlines()),
        "classes": classes,
        "functions": functions
    }

def is_camel_case(name):
    return name[0].isupper() and name[1:].isalnum() and not name.isdigit()

def is_snake_case(name):
    return name.islower() and "_" in name and name.replace("_", "").isalnum()

def generate_report(file_path, analysis):
    report = [f"File Analysis Report for {file_path}", f"Total lines of code: {analysis['lines']}\n"]

    report.append("\nClasses:")
    for cls in analysis['classes']:
        report.append(f"Class '{cls['name']}':")
        report.append(f"  - Docstring: {cls['docstring']}")
        if cls['naming_issue']:
            report.append("  - Naming issue: Should follow CamelCase")
        for method in cls['methods']:
            report.append(f"    Method '{method['name']}':")
            report.append(f"      - Docstring: {method['docstring']}")
            if method['naming_issue']:
                report.append("      - Naming issue: Should follow snake_case")

    report.append("\nFunctions:")
    for func in analysis['functions']:
        report.append(f"Function '{func['name']}':")
        report.append(f"  - Docstring: {func['docstring']}")
        if func['naming_issue']:
            report.append("  - Naming issue: Should follow snake_case")

    return "\n".join(report)

def write_report(file_path, report):
    report_name = f"style_report_{os.path.basename(file_path).split('.')[0]}.txt"
    try:
        with open(report_name, 'w') as file:
            file.write(report)
        print(f"Style report generated: {report_name}")
    except OSError:
        print("Error: Unable to write the report. Please check file permissions.")
        exit(1)

def main():
    file_path = input("Enter the path to the Python file: ")
    content = read_file(file_path)
    analysis = analyze_file(content)
    report = generate_report(file_path, analysis)
    write_report(file_path, report)

if __name__ == "__main__":
    main()
