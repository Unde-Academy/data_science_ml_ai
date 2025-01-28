# unde_academy-data_science Repository
Welcome to the official repository for  the Data science Department at Unde Academy This repository contains:

## Repository Contents
- **Lecture Notes and Resources**: Access detailed and comprehensive materials for your classes.
- **Assignments and Templates**: Practice hands-on data science skills through guided assignments.
- **Submission System**: Clear guidelines for submitting assignments.
- **Capstone Projects**: Showcase your skills with advanced, industry-standard projects.

---

## Repository Structure
```plaintext
├── class_notes/        # Lecture notes organized by topics
├── assignments/        # Assignment instructions and starter templates
├── submissions/        # Folder for assignment submissions
│   └── assignment_1/   # Submission path for Assignment 1
├── projects/           # Advanced capstone projects
└── README.md           # Repository overview and guidelines
```
## How to Access Lecture Notes
1. Navigate to the `class_notes/` folder.
2. Select the topic you are interested in.
3. View or download the `.ipynb` file or other files directly through GitHub.

## Assignment Submission Guidelines
All students must submit assignments to the designated folder for each assignment. For Assignment 1, use the following submission path:

### **Submit via Fork and Pull Request (Recommended)**  
Students are encouraged to submit their assignments using **Forks and Pull Requests** for a seamless process.
```plaintext
https://github.com/Unde-Academy/data_science_ml_ai/tree/main/submissions/assignment_1.
```

#### Steps for Students:
1. **Fork the Repository**  
   Click the **Fork** button on the top right corner of this GitHub repository page.

2. **Clone the Forked Repository **  
   Clone your forked repository to your local machine using HTTPS:  
   ```bash
   git clone https://github.com/<student_username>/data_science_ml_ai.git

3. **Add Your Assignment**
Navigate to the correct folder for Assignment 1:
```plaintext
submissions/assignment_1/
```
Add your completed assignment file.


5. **Follow Naming Conventions**
Save your assignment file with the naming format: your_name.ipynb or your_name.py.

6. **Commit Your Changes**
Stage and commit your work:
```bash
git add .
git commit -m "Add assignment submission"
```
6. ## Push Changes to Your Fork
Push your changes to your forked repository:
```bash
git push origin main
```
7. **Create a Pull Request**
On GitHub, navigate to your forked repository and click New Pull Request to merge your changes into the main repository.

## Contributing
To contribute to this repository or submit assignments, refer to the  `CONTRIBUTING.md` file.

#  Common Errors and how to handle Them
The error "please complete authentication in your browser" occurs because GitHub requires authentication to allow the push command. Here's how students can fix this issue:

# Solution 1: Authenticate Using a Personal Access Token (PAT)

GitHub has replaced password authentication with Personal Access Tokens (PAT) for better security.

## 1. Generate a Personal Access Token:
- Go to your GitHub profile, click on Settings.
- Navigate to Developer Settings → Personal Access Tokens → Tokens (classic) → Generate New Token.
- Select scopes (check repo and write:packages for access).
- Generate the token and copy it.

## 2. Replace Password with the Token:
- When prompted for your GitHub credentials during git push, use the token as the password.

# Solution 2: Use SSH Keys for Authentication
## 1. Generate an SSH Key:

Open a terminal and type:
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
- change the  "your_email@example.com" and enter your email address linked to the git hub account
- Press Enter to save the key to the default location.
- Optionally, add a passphrase.
  
  ## 2.  Add the SSH Key to Your GitHub Account:
Copy the key to your clipboard:
```bash
cat ~/.ssh/id_rsa.pub | xclip -sel clip
```
- Go to GitHub → Settings → SSH and GPG keys → New SSH Key.
- Paste the key and save.

## 3. Update Your Git Remote URL to Use SSH:
Replace the HTTPS URL with the SSH URL:
```bash
git remote set-url origin git@github.com:<username>/<repository>.git
```
## 4. Push Again:
Now try running:
```bash
git push origin main
```
# Solution 3: Use GitHub CLI
1. Install GitHub CLI:
- Install GitHub CLI by following the instructions for your OS: GitHub CLI Installation.
2. Authenticate with GitHub:
- Run the following command to log in:
```bash
git push origin main
```
- Follow the instructions to authenticate via the browser.
 3. Push Changes:
Retry the git push origin main command.

















