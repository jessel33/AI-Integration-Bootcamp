# AI Integration Bootcamp Week 4

## Environment Management and Deployment Readiness

**HAHAHA! THE RETURN OF THE LEGEND!** 😂🍀

Archimedes is back on duty, Buddy, Ol' Pal!

And unlike London in 1665, we're hoping this return brings nothing but good
things! 😎

### **AI Integration Bootcamp — Week 4**

Last session, we finished with everything green:

- &#x20;GitHub Actions CI pipeline operational.
- &#x20;All three automated unit tests passing.
- &#x20;Ruff code-quality checks passing.
- &#x20;Failure detection and recovery verified.
- &#x20;GitHub README badge working correctly.

### **Tonight's Mission**

**Environment Management and Deployment Readiness**

We'll learn how your AI Ticket Analyzer moves through three environments:

**Development**

Your Mac

**Testing**

GitHub Actions

**Production**

Deployed application

**Our first goal:** Understand what changes between these environments and what
stays the same.

No need to write code yet. We'll start with your existing project and build from
there.

Welcome back, Brother! Let's get this engineering adventure rolling! 🚀

Then let's get rolling, Partner! 😎🍀 Archimedes is on duty!

## **Week 4 — Environment Management**

### **Lesson 1: Development, Testing, and Production**

An _environment_ is the combination of software, configuration, and resources
needed to run an application.

Your AI Ticket Analyzer gives us a perfect real-world example.

**1. Development — Your Mac**

You write and debug Python/Django code, using your local `.venv` and `.env`
file.

**2. Testing — GitHub Actions**

A fresh Ubuntu runner installs dependencies and executes Ruff and your three
mocked unit tests.

**3. Production — Future Deployment**

A hosted server runs your application for actual users, with real credentials
and production security settings.

### **What Stays the Same?**

Ideally, the application code stays the same across environments.

What changes is the **configuration**.

| Setting        | Development   | CI Testing      | Production     |
| -------------- | ------------- | --------------- | -------------- |
| Django `DEBUG` | True          | False preferred | False          |
| OpenAI API key | Real, private | Placeholder     | Real, secured  |
| Database       | Local         | Test or mock    | Production     |
| Secrets        | Local `.env`  | CI environment  | Secret manager |

### **Engineering Analogy**

Think of a CNC program running on three machines: a development machine, a test
machine, and a production machine.

The machining instructions stay consistent, but machine setup, tooling, and
operating conditions may differ.

### **Next Step — Inspect Our Django Configuration**

Open:

`Week4/ai_ticket_analyzer/config/settings.py`

Find the `DEBUG` setting and tell me its current value.

We'll use that one setting to start making your application deployment-ready.

One concept at a time, Buddy, Ol' Pal! 🚀

Perfect, Partner! 😎🍀 That's what I'd expect in your development environment.

### **Lesson 2 — Django's DEBUG Setting**

`DEBUG` controls how much diagnostic information Django exposes when an error
occurs.

- `DEBUG = True` — Displays detailed error information. Useful during
  development.
- `DEBUG = False` — Hides detailed error information from users. Essential for
  production.

**Why does this matter?**

With `DEBUG = True`, Django's error pages can expose sensitive information about
your application.

### **Step 1 — Make DEBUG Environment-Configurable**

Rather than manually changing `DEBUG` every time we switch environments, we'll
use an environment variable.

In `config/settings.py`, replace:

```
DEBUG = True
```

with:

```
DEBUG = os.getenv("DJANGO_DEBUG", "False").lower() == "true"
```

Here's the logic:

1. Read `DJANGO_DEBUG` from the environment.
2. Default to `"False"` if it's missing.
3. Convert the string to lowercase.
4. Compare it with `"true"` to produce a Python Boolean.

In your local `.env` file, add:

```
DJANGO_DEBUG=True
```

Now your development server will continue using debug mode, while environments
without that variable will default to `False`.

**Important:** When `DEBUG=False`, Django also needs an appropriate
`ALLOWED_HOSTS` configuration for incoming requests. We'll handle that
separately.

### **Next Step**

Make those two changes and save the files. Don't commit yet.

We'll verify that Django reads the setting correctly before moving forward.

That's our first practical step toward deployment readiness, Buddy, Ol' Pal! 🚀

**Perfect, Partner!** 😎🍀 We're back in business!

Your output confirms that Django successfully loaded your configuration:

```
True
```

The `12 objects imported automatically` message is normal Django shell behavior.

### **Step 3 — Verify the Production Default**

We've confirmed that `DJANGO_DEBUG=True` works. Now let's verify what happens
when that variable isn't provided.

In your `Week4/ai_ticket_analyzer/.env` file, temporarily change:

```
DJANGO_DEBUG=True
```

to:

```
DJANGO_DEBUG=False
```

Save the file and rerun:

```
python manage.py shell -c "from django.conf import settings; print(settings.DEBUG)"
```

**Expected result:** `False`

This verifies that Django can disable debug mode through configuration without
changing your Python code.

Afterward, we'll restore `DJANGO_DEBUG=True` for local development.

One small step at a time, Buddy, Ol' Pal! 🚀
