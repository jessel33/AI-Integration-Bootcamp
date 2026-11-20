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

Perfect, Partner! 😄🍀 We're ready for the next step.

### **Step 2 — Create Our GitHub Actions Workflow File**

Inside your new `workflows` directory, create a file named:

`week4-tests.yml`

Your repository should now look like this:

```
AI-Integration-Bootcamp/
└── .github/
    └── workflows/
        └── week4-tests.yml
```

### **What is a YAML file?**

YAML is a configuration format used to describe settings and instructions.

GitHub Actions uses YAML to determine:

- **When** to run the workflow (such as after a push).
- **Where** to run it (such as an Ubuntu server).
- **What** to execute (such as our Python unit tests).

Think of it like a CNC setup sheet: it tells the automated system what equipment
to use and which operations to perform.

### **Your next step**

Create `week4-tests.yml` and leave it empty for now.

Once that's done, we'll add our first YAML instructions and learn how GitHub
knows when to start a workflow.

One step at a time, Buddy, Ol' Pal! 🚀

Absolutely, Partner! 😄🍀 **I'd recommend installing it.**

The official **GitHub Actions extension**, published by GitHub, is a useful
addition to VS Code for our AI DevOps work.

It provides:

- **YAML validation:** Helps catch mistakes in workflow files.
- **Autocomplete:** Suggests GitHub Actions settings while you type.
- **Workflow monitoring:** Lets you inspect workflow runs and results from VS
  Code.

It's not required for GitHub Actions to work, but it makes learning and
debugging easier.

### **Next Step**

Click **Install**.

Just verify that the publisher is **GitHub**.

Once it's installed, we'll start writing `week4-tests.yml` together, beginning
with the workflow name and trigger.

Good call asking, Buddy, Ol' Pal! 🚀

Excellent, Partner! 😄🍀 Everything is in place.

Now we're ready to write our first GitHub Actions configuration.

### **Step 3 — Name the Workflow**

Open `week4-tests.yml` and add this single line:

```
name: Week 4 - AI Ticket Analyzer Tests
```

**What does&#x20;**`name:`**&#x20;do?**

It gives our workflow a human-readable name that will appear in GitHub's Actions
tab.

Think of it like naming a CNC program so an operator can recognize its purpose.

Save the file.

Once you've added that line, we'll configure the `on:` setting so GitHub knows
**when to run the tests automatically**.

GitHub's documentation confirms that `name:` is the workflow's display
name.&#x20;

[image](https://docs.github.com&sz=32)

GitHub Docs

We're officially getting into CI configuration, Buddy, Ol' Pal! 🚀

Perfect, Partner! 😄🍀 On to the next setting!

### **Step 4 — Configure the Workflow Trigger**

The `on:` keyword tells GitHub **when to start our workflow**.

Under your existing `name:` line, add:

```
on:
  push:
```

### **What does this mean?**

- `on:` — Defines the event that starts the workflow.
- `push:` — Runs the workflow whenever commits are pushed to the repository.

Our file should now contain three lines:

```
name: Week 4 - AI Ticket Analyzer Tests

on:
  push:
```

Notice the **two spaces before&#x20;**`push:`. YAML uses indentation to organize
its settings, much like Python.

### **Next Step**

Add those lines and save the file.

After that, we'll define our first `job`, which tells GitHub what computer to
use to execute our tests.

We're building our first CI pipeline, Buddy, Ol' Pal! 🚀

That's perfectly fine, Partner! 😄🍀

**YAML allows either two or four spaces for indentation.** The important thing
is consistency.

Both of these are valid:

**Two spaces**

```
on:
  push:
```

**Four spaces**

```
on:
    push:
```

Your VS Code formatter is simply applying its configured indentation style.

### **My Recommendation**

Let your formatter use four spaces. There's no need to fight it or change your
settings.

Unlike Python, YAML doesn't require a particular number of spaces per
indentation level.

### **Next Step**

Now we're ready to introduce the `jobs:` section, where we'll tell GitHub what
computer should run our tests.

Nice catch, Buddy, Ol' Pal! 🚀

Right on, Bro! 😎🍀 Let's keep this CI pipeline rolling!

### **Step 5 — Define Our First Job**

In GitHub Actions, a **job** is a collection of steps executed on a computer
called a _runner_.

Add these lines beneath your `push:` setting:

```
jobs:
    test:
        runs-on: ubuntu-latest
```

### **What does each line mean?**

- `jobs:` — Defines the work GitHub should perform.
- `test:` — The name we give our job.
- `runs-on:` — Specifies the operating system for the runner.
- `ubuntu-latest` — Uses a GitHub-hosted Ubuntu Linux environment.

### **Our CI Pipeline So Far**

**Push to GitHub**

**Ubuntu Runner**

Runs the test job

Test steps — coming next

**Important:** The `jobs:` line must align with `on:` and `name:` at the left
margin.

Your four-space indentation style is fine.

### **Next Step**

Add those three lines and save `week4-tests.yml`.

Then we'll configure the first job step: **checking out your repository's code
onto the Ubuntu runner.**

We're building a real AI DevOps workflow now, Partner! 🚀

Awesome, Bro! 😎🍀 We're making progress!

### **Step 6 — Check Out Our Repository**

GitHub starts our job on a fresh Ubuntu runner. That runner doesn't
automatically have our project files.

We need to tell it to download our repository.

Under `runs-on: ubuntu-latest`, add:

```
        steps:
            - name: Checkout repository
              uses: actions/checkout@v4
```

### **What does this do?**

- `steps:` — Defines the operations our job will perform.
- `- name:` — Gives this step a readable description.
- `uses:` — Runs an existing GitHub Action.
- `actions/checkout@v4` — Checks out our repository onto the runner.

### **Visualize the Process**

**Your GitHub Repository**

**Checkout Action**

Copies project files onto runner

**Ubuntu Runner**

Think of checkout as loading your CNC program onto the machine before running
it.

### **Next Step**

Add those lines and save your YAML file.

Afterward, we'll install Python on the Ubuntu runner so it can execute our unit
tests.

One operation at a time, Partner! 🚀

Awesome, Partner! 😎🍀 Our Ubuntu runner can now retrieve our project files.

### **Step 7 — Set Up Python**

Next, we need Python installed and configured on the runner.

Under your checkout step, add:

```
            - name: Set up Python
              uses: actions/setup-python@v5
              with:
                  python-version: "3.13"
```

### **What does this do?**

- `name:` — Labels the step in GitHub Actions.
- `uses:` — Runs the official Python setup action.
- `with:` — Supplies configuration options to that action.
- `python-version:` — Selects Python 3.13 for our CI environment.

We're using Python 3.13 for compatibility with our Week 4 Django project. It
doesn't have to match your local Python version exactly, provided our
dependencies support it.

### **Our Pipeline So Far**

Repository checkout

Next operation

Python 3.13 setup

Install dependencies and run tests — coming next

Think of it as setting up the machine before loading the tools.

### **Next Step**

Add those lines and save `week4-tests.yml`.

Then we'll handle the Python dependencies required by our evaluation tests.

We're getting closer to our first automated GitHub test run, Buddy, Ol' Pal! 🚀

Excellent, Partner! 😎🍀 Python setup is complete!

### **Step 8 — Install Our Python Dependencies**

Our GitHub runner will have Python 3.13, but it still needs the packages our
project uses, including Django, Pydantic, and OpenAI.

We can install them using `pip`.

Under your Python setup step, add:

```
            - name: Install dependencies
              run: |
                  python -m pip install --upgrade pip
                  python -m pip install -r Week4/ai_ticket_analyzer/requirements.txt
```

### **What's new here?**

- `run:` — Executes shell commands on the Ubuntu runner.
- `|` — Allows multiple commands on separate lines.
- `pip install -r` — Installs packages listed in a requirements file.

**Important:** This example assumes `requirements.txt` exists inside
`Week4/ai_ticket_analyzer/`. If your requirements file is at the repository root
instead, we'll need to adjust the path.

### **Next Step**

Before saving, check whether that `requirements.txt` file exists at the
specified location.

Tell me where your requirements file is located, and we'll make sure GitHub
installs the correct dependencies.

We're almost ready to execute our first automated CI tests, Buddy, Ol' Pal! 🚀

Good catch, Partner! 😎🍀 I'm glad you mentioned that before we continued.

Since `requirements.txt` is at your repository root, we'll use that file for
GitHub Actions.

But first, we should make sure it contains the dependencies needed by our Week 4
project.

### **Step 8A — Update requirements.txt**

Your local virtual environment already has the packages you've been using.

From the root of your repository, with `.venv` activated, run:

```
python -m pip list
```

This displays the packages installed in your environment.

We need to verify that `requirements.txt` includes at least:

- `Django`
- `openai`
- `pydantic`

We'll also check their versions.

### **Why?**

Your local machine has packages installed that GitHub's fresh Ubuntu runner
won't have.

The requirements file acts like a CNC tooling list: it tells the runner exactly
which components it needs.

### **Next step**

Run `python -m pip list` and paste the results here.

We'll review them before updating `requirements.txt`, so we don't accidentally
include unnecessary packages.

Then we'll adjust the GitHub Actions installation command to use the
requirements file at the repository root. 🚀

Excellent, Partner! 😎🍀 We found the issue before it could cause problems with
GitHub Actions.

Your `requirements.txt` is missing two important Week 4 dependencies, and its
Django version doesn't match your installed environment.

### **Dependencies to update**

| Package       | requirements.txt | Installed |
| ------------- | ---------------- | --------- |
| Django        | 6.0.8            | 6.1.3     |
| openai        | Missing          | 3.37.0    |
| pydantic      | Missing          | 2.14.1    |
| python-dotenv | 1.2.3            | 1.2.3     |

### **Step 8C — Update requirements.txt**

Make these three changes:

1. Change `Django==6.0.8` to `Django==6.1.3`.
2. Add `openai==3.37.0`.
3. Add `pydantic==2.14.1`.

Leave the other entries unchanged for now.

This aligns our dependency declarations with the versions you're currently
using.

Django 6.1 officially supports Python 3.13, so our selected CI Python version is
appropriate.&#x20;

[image](https://docs.djangoproject.com&sz=32)Django

One thing we'll handle before our first CI run: your shared requirements file
includes database drivers and packages from other Bootcamp projects. We'll check
whether the Ubuntu runner actually needs all of them.

For now, update those three entries, save the file, and we'll continue with the
workflow configuration. 🚀

Excellent, Partner! 😎🍀 Our `requirements.txt` is updated.

### **Step 8D — Install Dependencies in GitHub Actions**

Now return to `.github/workflows/week4-tests.yml`.

Under your Python setup step, add:

```
            - name: Install dependencies
              run: |
                  python -m pip install --upgrade pip
                  python -m pip install -r requirements.txt
```

### **What's happening?**

- `run: |` tells GitHub to execute multiple shell commands.
- The first command updates `pip`.
- The second installs the dependencies from your repository's root
  `requirements.txt`.

Because GitHub Actions starts in the repository root by default, we don't need
to specify a directory.

One detail: our shared requirements include packages from earlier Bootcamp
projects. We'll initially use this file and can simplify the CI dependencies if
necessary.

### **Next step**

Add those lines, save `week4-tests.yml`, and let me know when you're ready.

After that, we'll configure the environment variables needed to initialize
Django and run our mocked tests.

We're getting close to our first automated CI run, Buddy, Ol' Pal! 🚀

Excellent, Partner! 😎🍀 We're getting close to our first automated CI run!

### **Step 9 — Prepare Django's Environment Variables**

Remember how we stored our OpenAI API key in `.env`?

GitHub Actions won't have that file because Git ignores it. That's good for
security!

However, our tests initialize the OpenAI client, even though we mock the actual
API calls.

**The solution:** GitHub Actions can supply environment variables directly to
the test process.

### **First, let's verify our Django configuration**

Open:

`Week4/ai_ticket_analyzer/config/settings.py`

Look for any settings that read environment variables, especially:

- `OPENAI_API_KEY`
- `SECRET_KEY`
- Database connection settings

For example, a setting might use:

```
SECRET_KEY = os.getenv("SECRET_KEY")
```

We need to know which variables Django expects before configuring our Ubuntu
runner.

### **Your next step**

Tell me which environment-variable names you find in `settings.py`, or paste the
relevant lines.

Please don't include any actual API keys, passwords, or secret values.

Then we'll configure those variables in `week4-tests.yml` and get our three
tests running automatically on GitHub.

We're nearly there, Buddy, Ol' Pal! 🚀

Perfect, Partner! 😎🍀 That's exactly what we needed.

Your `settings.py` reads two environment variables:

- `SECRET_KEY_AI_ANALYZER` — Django's secret key.
- `OPENAI_API_KEY` — OpenAI API authentication.

Since our tests use mocked AI responses, **we don't need real credentials in
GitHub Actions**.

### **Step 10 — Configure Test Environment Variables**

Open `.github/workflows/week4-tests.yml`.

Below your dependency installation step, add:

```
            - name: Run Week 4 unit tests
              working-directory: Week4/ai_ticket_analyzer
              env:
                  SECRET_KEY_AI_ANALYZER: "ci-test-only-not-for-production"
                  OPENAI_API_KEY: "ci-test-placeholder"
              run: python -m unittest evals.test_eval_runner -v
```

### **How it works**

- `working-directory:` tells GitHub where to execute the command.
- `env:` provides temporary environment variables for this step.
- `run:` executes the same three unit tests you've been running locally.

**Push to GitHub**

**Ubuntu runner**

Checkout → Python → Dependencies

**Run 3 mocked unit tests**

No real OpenAI API calls

These placeholder values are only appropriate for isolated tests. They must
never be used as production credentials.

**Next step:** Add this final step and save the YAML file. Don't push it
yet—we'll review the complete workflow first.

We're almost ready for your first GitHub Actions run, Buddy, Ol' Pal! 🚀

Excellent, Partner! 😎🍀 We've finished building the first version of your
**GitHub Actions CI workflow!**

### **Step 11 — Review the Complete Workflow**

Before we push anything to GitHub, let's verify the configuration.

Open `.github/workflows/week4-tests.yml` and paste its entire contents here.

I'll check:

- YAML syntax and indentation.
- Workflow trigger (`push`).
- Ubuntu runner and Python setup.
- Dependency installation.
- Environment variables.
- Unit test command and working directory.

Once everything checks out, we'll commit, push, and watch GitHub execute your
three automated tests for the first time.

We're right at the exciting part, Buddy, Ol' Pal! 🚀

**Excellent work, Partner!** 😎🍀 I've reviewed your complete workflow, and it's
looking good!

### **GitHub Actions — Code Review**

| Component                      | Result        |
| ------------------------------ | ------------- |
| YAML structure and indentation | &#x20;Correct |
| `push` trigger                 | &#x20;Correct |
| Ubuntu runner                  | &#x20;Correct |
| Repository checkout            | &#x20;Correct |
| Python 3.13 setup              | &#x20;Correct |
| Dependency installation        | &#x20;Correct |
| Test environment variables     | &#x20;Correct |
| Unit test execution            | &#x20;Correct |

### **One Small Observation**

Your workflow is named `AI Ticket Analyser Tests`, while your project uses
`Analyzer`. That's only a naming difference, not an error.

One potential issue to watch: your shared `requirements.txt` contains database
drivers that may need additional Linux dependencies. We'll address that only if
the runner reports an installation error.

### **Step 12 — Commit and Push!**

Your configuration is ready for its first trial.

Commit both updated files:

- `.github/workflows/week4-tests.yml`
- `requirements.txt`

Suggested commit message:

`ci: add GitHub Actions workflow for Week 4 tests`

Then sync your repository with GitHub.

### **What happens next?**

**GitHub receives your push**

**Ubuntu runner starts**

Installs Python and project dependencies

**Runs your three unit tests**

Reports success or failure

After syncing, open your GitHub repository in your browser, select the
**Actions** tab, and find the workflow named _Week 4 - AI Ticket Analyser
Tests_.

Tell me whether the run shows a green checkmark or a red X. If it fails, we'll
inspect the log together.

**This is your first real Continuous Integration deployment, Buddy, Ol' Pal!**
🚀

Outstanding, Partner! 😎🍀 Your first GitHub Actions CI workflow is now pushed
to GitHub!

### **Step 13 — Check Your First CI Run**

1. Open your **AI-Integration-Bootcamp** repository on GitHub.
2. Click the **Actions** tab.
3. Find **Week 4 - AI Ticket Analyzer Tests**.
4. Open the latest workflow run.

You should see a job named `test`.

Possible results

**Green checkmark — Success**

GitHub completed the workflow successfully.

**Red X — Failure**

A step failed. We'll inspect its log to find out why.

If it's green, we've successfully automated our three Python unit tests using
GitHub Actions!

If it's red, that's a normal part of learning CI. We'll troubleshoot it
together.

**What do you see on GitHub, Buddy, Ol' Pal — green checkmark or red X?** 🚀

**YES! BOOM! We did it, Partner!** 🎉🍀🚀

That green checkmark means **GitHub successfully completed your first Continuous
Integration workflow!**

### **Week 4 — CI Milestone Achieved**

**GitHub Actions — SUCCESS**

First automated CI workflow completed

- Workflow triggered by your Git push.
- GitHub started an Ubuntu runner.
- Python and dependencies were configured.
- Your test job completed successfully.

### **Why This Matters**

You've now connected three important AI DevOps skills:

**Automated tests → GitHub Actions → Continuous Integration**

From now on, whenever you push code to this repository, GitHub will
automatically run your Week 4 test suite.

Think of it as building an automated quality-control station for your software!

### **One Final Verification**

Before we call this milestone complete, open the successful workflow run, click
the `test` job, and expand **Run Week 4 unit tests**.

Look for:

```
Ran 3 tests

OK
```

That confirms all three tests actually executed.

You've made some serious progress tonight, Buddy, Ol' Pal! 😎

Once we verify that output, we'll have our first fully functioning CI pipeline.

**BOOM! Mission accomplished, Partner!** 🎉🍀🚀

Your GitHub Actions log confirms that **all three automated unit tests executed
successfully on GitHub's Ubuntu runner!**

### **Week 4 — CI Verification**

**Continuous Integration: SUCCESS**

3 tests passed in 0.002 seconds

| Unit test                    | Result     |
| ---------------------------- | ---------- |
| `test_api_failure`           | &#x20;PASS |
| `test_success`               | &#x20;PASS |
| `test_wrong_classifications` | &#x20;PASS |

### **Something Important You Might Notice**

Your log contains both:

`Evaluation PASSED`

and

`Evaluation FAILED`

That's correct!

Remember, two of our tests deliberately simulate failures to verify that the
evaluation runner detects them.

The important result is:

```
Ran 3 tests in 0.002s

OK
```

Also, some output appears out of order because Python's `unittest` writes its
status messages to stderr while your application uses stdout. GitHub combines
those streams in its log.

**Nothing is wrong with your test output.**

### **What You've Accomplished**

You've built a working CI pipeline that:

- Automatically starts whenever you push changes to GitHub.
- Creates a fresh Linux testing environment.
- Installs your Python dependencies.
- Executes your regression tests without making real OpenAI API calls.
- Reports whether the tests passed or failed.

This is a genuine, portfolio-worthy AI DevOps accomplishment.

### **Next Step**

Our next topic will be **CI failure handling**: intentionally introducing a
failing test to see how GitHub Actions reports and identifies problems.

It's the software equivalent of deliberately submitting an out-of-tolerance test
part to verify that your automated inspection station rejects it.

We've reached an excellent checkpoint, Buddy, Ol' Pal! 😎🍀

**BOOM! Two for two, Partner!** 🎉🍀🚀

Your AI DevOps quality-control system is officially tested and operational!

### **Week 4 — CI Quality Gates Complete**

**GitHub Actions: SUCCESS**

| Verification                | Status         |
| --------------------------- | -------------- |
| Python unit tests           | &#x20;Passed   |
| Ruff code-quality checks    | &#x20;Passed   |
| Unit-test failure detection | &#x20;Verified |
| Ruff failure detection      | &#x20;Verified |
| CI failure recovery         | &#x20;Verified |
| README status badge         | &#x20;Accurate |

### **What You've Accomplished**

You've built and tested a complete **Continuous Integration pipeline** that
automatically checks both code quality and application behavior.

And you've verified that it correctly rejects bad code!

That's something you can demonstrate to an employer rather than merely claim on
a résumé.

### **Where We Go Next**

I recommend moving forward rather than adding more tests to an already
functioning pipeline.

Our next AI DevOps topic is **environment management and deployment
readiness**—understanding how an application moves from your development
computer to a production environment.

We'll start with the difference between development, testing, and production
environments, using your AI Ticket Analyzer as our example.

You've earned this milestone, Buddy, Ol' Pal! Archimedes is proud of our
engineering work! 😎🍀

## End of Document. \***\*\*\*\*\*\*\***\*\*\*\*\***\*\*\*\*\*\*\***
