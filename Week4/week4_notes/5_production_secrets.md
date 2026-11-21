# AI-Integration-Bootcamp

## Week 4 Production Secrets Notes

- Mostly copies of the Instructions the Instructor gives to the student.

**Welcome back, Brother!** 😎🍀 Archimedes(Instructor Named) reporting for duty!

Since you've got a little time, we'll keep tonight's lesson short, practical,
and focused.

### **Week 4 — AI DevOps: Managing Production Secrets**

Last session, we completed Django's environment configuration and security
checks.

**Today's concept:** How production servers securely receive environment
variables without committing `.env` files to GitHub.

**GitHub Repository**

Application code — no secrets

**Production Server**

Receives code and environment configuration

**Secret Manager**

Supplies credentials securely

### **Three Important Points**

- Your `.env` file is useful for local development.
- Production hosting platforms can supply environment variables without storing
  a `.env` file in your repository.
- Sensitive values such as `OPENAI_API_KEY` and `SECRET_KEY_AI_ANALYZER` should
  be stored in a protected secret-management system.

### **Mr. Yellow Notebook 📒**

> **Secret Management:** Keep credentials separate from source code. Supply them
> securely to the application at runtime.

### **Our First Practical Task**

We already have GitHub Actions configured for the AI Ticket Analyzer.

Let's inspect its environment configuration before deciding whether anything
needs changing.

Open `.github/workflows/week4-tests.yml` and find the `env:` section.

You should see the two placeholder values we configured for testing.

No changes yet—just confirm they're still there.

Then we'll compare **test credentials versus production secrets**, one concept
at a time, Buddy, Ol' Pal! 🚀

Perfect, Partner! 😎🍀 That's exactly what I wanted to see.

### **Code Review: Correct&#x20;**

Your GitHub Actions workflow uses two placeholder values:

| Variable                 | Purpose                                                         |
| ------------------------ | --------------------------------------------------------------- |
| `SECRET_KEY_AI_ANALYZER` | Allows Django to initialize during testing                      |
| `OPENAI_API_KEY`         | Allows the OpenAI client to initialize without real credentials |

Because your unit tests mock the OpenAI API calls, **neither value needs to be a
real secret**.

### **Lesson: Test Credentials vs. Production Secrets**

Here's the important difference:

- **CI testing:** Use harmless placeholders when tests don't need real
  credentials.
- **Production:** Use real credentials supplied securely by the hosting
  environment.
- **Source code:** Never hardcode production secrets.

Your existing workflow follows this principle correctly. No changes needed!

### **Mr. Yellow Notebook 📒**

> **Principle of Least Privilege:** Give an application or automated process
> only the access it needs to perform its job.

Our unit tests don't need access to your real OpenAI account, so we don't give
them access.

### **Next Step — GitHub Secrets**

GitHub provides a feature called **Actions Secrets** for workflows that
genuinely need confidential values.

We'll learn where to find that feature without creating or exposing any real
credentials.

In your GitHub repository, navigate to:

**Settings → Secrets and variables → Actions**

You should find a section called **Repository secrets**.

For now, just locate that page. We'll discuss when to use repository secrets and
when to use hosting-provider secrets.

We're keeping this lesson short and practical, Brother! 🍀🚀

Perfect, Partner! 😎🍀 You're exactly where we want to be!

### **GitHub Actions — Two Types of Secrets**

| Type                    | Purpose                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------- |
| **Repository secrets**  | Available to workflows throughout the repository, subject to GitHub's access rules. |
| **Environment secrets** | Associated with a specific environment, such as `staging` or `production`.          |

### **Practical Example**

Suppose we eventually deploy your AI Ticket Analyzer.

- **Repository secret:** A credential needed by multiple CI workflows.
- **Environment secret:** A production deployment credential available only to
  jobs using the `production` environment.

Environment secrets can also be combined with deployment protections, such as
requiring approval before a job proceeds.

### **Do We Need to Create Secrets Now?**

**No!** Our three unit tests already work using harmless placeholders.

Adding your real OpenAI API key would introduce unnecessary security risk and
could allow unexpected API charges if a test accidentally made a live request.

### **Mr. Yellow Notebook 📒**

> **Secrets vs. Variables:** Secrets protect confidential values. Variables
> store ordinary, non-sensitive configuration.

### **Next Step**

Let's leave GitHub's secret settings unchanged.

Our next practical concept will be **deployment environments**—how we separate
staging from production so that testing changes doesn't affect real users.

We're building the foundation for deploying your AI Ticket Analyzer safely,
Brother! 🚀

Outstanding, Brother! 😎🍀

And that's useful experience! Since you've already worked with Namecheap's
environment storage for your Django website, we can move past the basics and
build on what you know.

### **Week 4 — Lesson: Staging vs. Production**

A **staging environment** is a place to test an application under
production-like conditions before real users see the changes.

**Development**

Your Mac — write code and debug.

**CI Testing**

GitHub Actions — run Ruff and automated tests.

**Staging**

A deployed test application with production-like settings and test data.

**Production**

The live application serving real users.

### **What's the difference between CI and staging?**

- **CI:** Verifies that the code passes automated checks.
- **Staging:** Verifies that the deployed application actually works in a
  realistic environment.

For example, your AI Ticket Analyzer might pass every unit test but fail in
staging because a production-style environment variable is missing.

That's exactly the kind of issue staging helps catch.

### **Mr. Yellow Notebook 📒**

> **Staging:** A production-like environment used to validate deployments before
> releasing changes to real users.

### **Next Step — Our First Deployment Plan**

Before choosing any hosting provider, let's identify the environment
requirements for our Week 4 application.

Open `Week4/ai_ticket_analyzer/config/settings.py` and locate the `DATABASES`
setting.

Tell me which database engine it's currently configured to use (SQLite, MySQL,
PostgreSQL, etc.).

That will help us determine what a staging deployment actually needs.

Onward, Partner! Archimedes is back at the engineering bench! 🚀

Perfect, Partner! 😎🍀 We've confirmed that Django is using the standard SQLite
configuration.

### **Week 4 — Planning Persistent Storage**

Your current configuration:

```
"NAME": BASE_DIR / "db.sqlite3",
```

means Django stores its database in a file inside your project directory.

That's fine for development. But there's an important deployment consideration.

### **What Happens During Deployment?**

**Staging Application**

Django running on a hosting server

**SQLite Database**

db.sqlite3 stored on disk

If the database lives on temporary storage, redeployment can erase its contents.

### **The Solution: Persistent Storage**

A hosting provider may offer a persistent disk or volume that survives
application restarts and redeployments.

We can configure Django to store its SQLite database there instead of inside the
application directory.

For example:

| Environment | Database location                       |
| ----------- | --------------------------------------- |
| Development | `BASE_DIR / "db.sqlite3"`               |
| Staging     | `/data/staging.sqlite3`                 |
| Production  | A persistent database service or volume |

These are illustrative paths, not locations we've configured.

### **Mr. Yellow Notebook 📒**

> **Ephemeral vs. Persistent Storage:** Ephemeral storage can disappear when an
> application instance is replaced. Persistent storage is designed to retain
> data independently of an application's lifecycle.

### **Next Step — One Important Decision**

Before changing database configuration, let's establish what our Week 4
application actually needs.

Your AI Ticket Analyzer currently analyzes submitted complaints and returns
structured AI results.

**Does it save those analyses to the SQLite database, or only display the
results?**

This determines whether persistent database storage is necessary for our staging
demonstration.

One engineering decision at a time, Buddy, Ol' Pal! 🚀

**BOOM! Mystery solved, Partner!** 😎🍀

Your database inspection confirms what you suspected.

### **SQLite Inspection — Results**

10 Django framework tables found

No application-specific ticket analysis tables

Database size explained by Django's built-in tables and SQLite storage

### **What This Means**

Your current AI Ticket Analyzer appears to be **stateless with respect to ticket
analyses**.

That means:

1. A user submits a complaint.
2. Your application sends it to OpenAI.
3. OpenAI returns a structured analysis.
4. Django displays the result.
5. The application doesn't persist that analysis in SQLite.

The table listing confirms there's no dedicated analysis table. It doesn't prove
that no other storage mechanism exists, but it agrees with your code review.

### **Why This Is Good for Staging**

Since we're not storing analyses, **we don't need persistent ticket-analysis
storage for our first staging deployment**.

That simplifies our deployment plan considerably!

### **Mr. Yellow Notebook 📒**

> **Stateless Application:** An application that doesn't depend on retaining
> application-specific data between requests. Stateless designs are often easier
> to deploy and scale.

One qualification: Django's built-in authentication and session features can
still require database storage if we use them.

### **Next Step**

Our next deployment decision is whether the staging version should make real
OpenAI API calls or use mocked responses.

For a first staging deployment, I'd favor testing with controlled, low-cost real
API requests so we can verify the complete integration.

We'll discuss how to do that safely before configuring any hosting service.

Nice investigative work, Buddy, Ol' Pal! 📒🚀

### - Currently in Progress!!! \*\*\*
