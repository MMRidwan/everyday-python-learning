# Git Cheat Sheet – Everyday Python Learning

## Repo

https://github.com/MMRidwan/everyday-python-learning.git

---

# Core Git Concepts (Don’t Skip This)

## What is Git?

* Version control system
* Tracks changes in your code over time

## Key Areas

* **Working Directory** → your files
* **Staging Area** → files ready to commit
* **Repository** → saved history

---

# Basic Commands (You Must Know These Cold)

## Check status

```bash
git status
```

## Add files

```bash
git add .
```

## Commit changes

```bash
git commit -m "clear message"
```

## Push to GitHub

```bash
git push
```

## Pull latest changes

```bash
git pull
```

---

# 🌿 Branching (Non-Negotiable Habit)

## Create new branch

```bash
git checkout -b feature/branch-name
```

## Switch branches

```bash
git checkout master
```

## Delete branch (after merge)

```bash
git branch -d feature/branch-name
```

---

# 🔗 First-Time Setup (One-Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

---

# 🚫 .gitignore (Prevent Garbage)

Create `.gitignore`:

```
__pycache__/
*.pyc
.env
.vscode/
```

---

# 📅 DAILY WORKFLOW (Your System)

## 1. Start your day → create new branch

```bash
git checkout master
git pull
git checkout -b feature/04-10
```

---

## 2. Create daily folder

Inside your project:

```
/04.10/
    script1.py
    script2.py
```

---

## 3. Work normally (throughout the day)

* Write Python scripts
* Keep files inside that date folder

---

## 4. End of day → commit everything

```bash
git status
git add .
git commit -m "04.10 - practiced loops, conditionals, and functions"
```

---

## 5. Push branch

```bash
git push -u origin feature/04-10
```

---

## 6. Create Pull Request (on GitHub)

* Go to repo
* Click **Compare & pull request**
* Add description:

  * What you practiced
  * What you learned

---

## 7. Merge PR

* Click **Merge Pull Request**
* Delete branch (on GitHub)

---

## 8. Clean up locally

```bash
git checkout master
git pull
git branch -d feature/04-10
```

---

# 🔁 NEXT DAY (Repeat System)

```bash
git checkout master
git pull
git checkout -b feature/04-11
```

---

#  Common Mistakes (Stop Doing These)

##  Committing garbage

Bad:

```bash
git commit -m "update"
```

Good:

```bash
git commit -m "04.10 - added list practice and fixed loop bug"
```

---

## ❌ Working on master

Never code directly on `master`

---

## ❌ Blind `git add .`

Always check:

```bash
git status
```

---

## ❌ Skipping pull before branching

Always:

```bash
git checkout master
git pull
```

---

# 🧱 Naming Convention (Stay Consistent)

Branches:

```
feature/04-10
feature/04-11
```

Folders:

```
04.10/
04.11/
```

---

# 🧠 Mental Model (This is what you're actually doing)

* `branch` → isolated workspace
* `commit` → save progress
* `push` → upload to GitHub
* `PR` → review checkpoint
* `merge` → finalize work

---

# 🧨 Reality Check

If you:

* Skip commit messages → your history becomes useless
* Skip PR review → you stay sloppy
* Work on master → you will break things

Consistency matters more than complexity.

---

# 🚀 Minimum Standard You Should Hit Daily

* One clean branch
* One meaningful commit
* One merged PR
* One clear learning outcome

---

Stick to this for 30 days and you’ll be ahead of most beginners who just “code randomly” with no structure.
