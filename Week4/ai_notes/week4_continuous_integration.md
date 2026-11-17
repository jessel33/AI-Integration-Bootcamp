# Let's move into **GitHub Actions and Continuous Integration (CI)**.

## **Week 4 — Lesson: Continuous Integration**

You've built three automated tests. Now we're going to teach GitHub to run those
tests whenever you push code.

Here's the workflow:

**Your Computer**

Write code, commit, push

**GitHub Actions**

Starts an automated workflow

**Run Unit Tests**

Report PASS or FAIL

Think of GitHub Actions like an automated CNC inspection station. Whenever new
parts arrive, the station runs the same quality checks without requiring an
operator to start them manually.

### **Our First Task: Create the Workflow Directory**

GitHub Actions looks for workflow configuration files in a specific directory at
the root of your repository:

```
AI-Integration-Bootcamp/
├── .github/
│   └── workflows/
│       └── (our workflow file will go here)
├── Week3/
├── Week4/
└── .venv/
```

In VS Code, at the root of your `AI-Integration-Bootcamp` repository:

1. Create a directory named `.github` if it doesn't already exist.
2. Inside it, create another directory named `workflows`.

We'll use a YAML (`.yml`) file to define the automated steps GitHub should
execute.

**One step at a time:** Create those directories and tell me when you're ready.
Then we'll build the workflow configuration together, without skipping the
concepts. 🚀
