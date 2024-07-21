# Syllabus PDF to Markdown Converter

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A user-friendly desktop application that converts VIT syllabus PDFs into structured Markdown files, making it easier to manage  course materials.

<!--  -->

## Features

- Simple and intuitive graphical user interface
- Converts VIT theory syllabus PDFs into structured Markdown
- Preserves module structure and content hierarchy
- Creates task lists for easy tracking of course progress

## Installation

1. Ensure you have Python 3.6 or higher installed on your system.

2. Clone this repository:
   ```
   git clone https://github.com/parthsidpara/syllabus-markdown
   cd syllabus-markdown
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. In the application window:
   - Click "Browse" next to "Syllabus PDF" to select your input PDF file.
   - Click "Browse" next to "Markdown File" to choose the save location for the output Markdown file.
   - Click "Convert PDF to Markdown" to start the conversion process.

3. Once the conversion is complete, you'll see a success message with the location of your new Markdown file.

## Example

Input PDF structure:
```
Module:1 Introduction to Computer Science
- Basic concepts: algorithms, data structures
- History of computing
- Introduction to programming languages: Python, Java, C++
```

Output Markdown:
```markdown
## Module 1: Introduction to Computer Science

- [ ] Basic concepts:
  - [ ] algorithms
  - [ ] data structures
- [ ] History of computing
- [ ] Introduction to programming languages:
  - [ ] Python
  - [ ] Java
  - [ ] C++
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](License) file for details.


## Contact

If you have any questions or feedback, please open an issue on this repository or contact me at (parthsidpara2005@gmail.com).

---
