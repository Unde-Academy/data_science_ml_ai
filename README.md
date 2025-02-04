# Unde Academy - Data Science and AI Repository

Welcome to the official repository for the Data Science Department at Unde Academy! This repository contains:

## Repository Contents
- **Lecture Notes & Resources**: Organized by topics in `class_notes/`
- **Assignments & Templates**: Available under `assignments/`
- **Submission System**: Submit assignments in `submissions/`
- **Capstone Projects**: Industry-standard projects in `projects/`

## Repository Structure

```plaintext
📂 data_science_ml_ai
 ┣ 📂 class_notes/          # Lecture notes organized by topics
 ┣ 📂 assignments/
 ┃ ┣ 📂 group_1/
 ┃ ┃ ┣ 📜 assignment_1.ipynb
 ┃ ┃ ┣ 📜 assignment_2.ipynb
 ┃ ┣ 📂 group_2/
 ┃ ┃ ┣ 📜 assignment_1.ipynb
 ┃ ┃ ┣ 📜 assignment_2.ipynb
 ┃ ┣ 📂 templates/           # Assignment templates
 ┃ ┃ ┣ 📜 assignment_template.ipynb
 ┣ 📂 submissions/
 ┃ ┣ 📂 assignment_1/        # Folder for assignment submissions
 ┣ 📂 projects/              # Advanced capstone projects
 ┣ 📜 README.md              # Repository overview and guidelines
 ┣ 📜 instructions.md        # Submission guidelines
 ┣ 📜 grading_criteria.md    # Rubric for assignment evaluation

```
## How to Access Lecture Notes
1. Navigate to the `class_notes/` folder.
2. Select the topic you are interested in.
3. View or download the `.ipynb` file or other files directly through GitHub.

## Assignment Submission Guidelines
1. Clone the repository:
```bash
   git clone https://github.com/Unde-Academy/data_science_ml_ai.git
   cd data_science_ml_ai
```
## 2. Create a new branch for your assignment
 ```bash
git checkout -b student_name-assignment1
```
## 3. Navigate to your folder and add your assignment
```plaintext
cd assignments/group_1
mv ~/Downloads/assignment_1.ipynb .
```
## 4. Stage and commit the changes
```plaintext
git add .
git commit -m "Completed assignment 1"
```
## 5. Push your branch to GitHub
```plaintext
git push origin student_name-assignment1
```

## 6. Create a Pull Request (PR) on GitHub.


## Common Git Issues & Fixes
```bash
Issue	               | Solution
------------------------------------------------------------------
Merge Conflicts	   | Run git pull origin main before pushing
Push Rejected	      | Ensure students use branches instead of main
Forgot to Commit	   | Use git status, git add ., git commit -m "message"
Wrong File Location	|Ensure files are placed inside assignments/student_name/
```
