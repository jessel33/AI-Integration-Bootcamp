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

Excellent detective work, Partner! 😎🍀

You found the culprit: `**/.env` was hiding your environment files in VS Code
Explorer.

Removing that exclusion is perfectly fine.

**Important:** Your `.env` files are still protected by `.gitignore`. Making
them visible in VS Code does not make Git track them.

### **Back to Our Django Lesson**

Now that you can see your `.env` file, let's finish verifying our environment
configuration.

1. Open `Week4/ai_ticket_analyzer/.env`.
2. Change `DJANGO_DEBUG=True` to `DJANGO_DEBUG=False`.
3. Save the file.
4. Run:

```
python manage.py shell -c "from django.conf import settings; print(settings.DEBUG)"
```

Expected output: `False`.

After confirming that, we'll restore `True` for development.

**Excellent, Partner!** 😎🍀 Another successful test!

We've now verified that Django correctly reads both values of `DJANGO_DEBUG`.

| Environment setting  | Django result |
| -------------------- | ------------- |
| `DJANGO_DEBUG=True`  | &#x20;`True`  |
| `DJANGO_DEBUG=False` | &#x20;`False` |

### **What You've Learned**

Your application can now switch between development and production-style debug
settings **without changing its Python source code**.

That's an important environment-management principle.

### **Next Step — Restore Development Mode**

In your Week 4 `.env` file, change:

```
DJANGO_DEBUG=True
```

Save the file.

Then we'll move to Django's `ALLOWED_HOSTS` setting, another important part of
preparing an application for deployment.

### **Week 4 — Lesson 3: Django's&#x20;**`ALLOWED_HOSTS`

First, one important distinction:

`ALLOWED_HOSTS`**&#x20;doesn't tell Django where to host your application.** It
tells Django which hostnames are allowed to send requests to your application.

For example:

| Environment       | Allowed hostname      |
| ----------------- | --------------------- |
| Local development | `localhost`           |
| Local development | `127.0.0.1`           |
| Future production | `tickets.example.com` |

The production hostname is just an example. We haven't selected a hosting
provider or domain yet.

### **Why This Matters**

Django uses `ALLOWED_HOSTS` to help protect against malicious HTTP Host headers.

When `DEBUG=False`, Django requires an appropriate `ALLOWED_HOSTS` configuration
for normal HTTP requests.

Think of it like a CNC machine's access-control list: only recognized sources
are permitted through the gate.

### **Step 1 — Inspect Your Existing Setting**

Open `Week4/ai_ticket_analyzer/config/settings.py` and find:

```
ALLOWED_HOSTS = []
```

That's the default Django configuration.

For local development, we'll eventually configure:

```
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```

Later, we'll make the list environment-configurable so production can use its
actual domain. We won't use the wildcard `"*"`, which would allow any hostname.

For now, tell me what your current `ALLOWED_HOSTS` setting contains, and we'll
make the next change together.

### **Step 2 — Configure Local Hosts**

In `Week4/ai_ticket_analyzer/config/settings.py`, change:

```
ALLOWED_HOSTS = []
```

to:

```
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```

### **What does this do?**

- `localhost` — Allows requests using `http://localhost:8000`.
- `127.0.0.1` — Allows requests using `http://127.0.0.1:8000`.
- Other hostnames are rejected.

Both addresses refer to your local computer.

**Important:** This doesn't expose your Django server to the internet. It only
controls which hostnames Django accepts.

### **Next Step**

Make that change and save `settings.py`.

Afterward, we'll move `ALLOWED_HOSTS` into your `.env` configuration, just as we
did with `DJANGO_DEBUG`.

Perfect, Partner! 😎🍀 Your local hostnames are now configured.

### **Step 3 — Make&#x20;**`ALLOWED_HOSTS`**&#x20;Environment-Configurable**

Just like `DEBUG`, we want different environments to use different hostnames
without changing Python code.

In `config/settings.py`, replace your current `ALLOWED_HOSTS` assignment with:

```
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")
```

### **How it works**

- `os.getenv()` reads the environment variable.
- `"localhost,127.0.0.1"` provides a default.
- `.split(",")` converts the comma-separated string into a Python list.

For example:

```
"localhost,127.0.0.1"
          ↓
["localhost", "127.0.0.1"]
```

Then add this line to your Week 4 `.env` file:

```
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

When we deploy the application later, we can replace those values with the
actual production hostname.

### **Next Step**

Make those two changes and save both files.

Then we'll verify Django reads the hostname list correctly, just as we did with
`DEBUG`.

Excellent, Partner! 😎🍀 Let's verify that Django is reading our new environment
variable correctly.

### **Step 4 — Verify&#x20;**`ALLOWED_HOSTS`

From your `Week4/ai_ticket_analyzer` directory, run:

```
python manage.py shell -c "from django.conf import settings; print(settings.ALLOWED_HOSTS)"
```

### **Expected Result**

```
['localhost', '127.0.0.1']
```

This will confirm that:

- Django successfully reads `DJANGO_ALLOWED_HOSTS` from `.env`.
- `.split(",")` converts the string into a Python list.
- Both local hostnames are configured correctly.

Remember, `ALLOWED_HOSTS` controls which hostnames Django accepts, not which
network interfaces the server listens on.

### **Next Step**

Run the command and show me the output.

Once it passes, we'll check how your application behaves with `DEBUG=False` and
`ALLOWED_HOSTS` configured.

We're making good progress toward deployment readiness.

**Perfect, Partner!** 😎🍀 Another successful configuration test!

Django returned exactly what we expected:

```
['localhost', '127.0.0.1']
```

This confirms that Django is correctly reading and converting your
`DJANGO_ALLOWED_HOSTS` environment variable.

### **Step 5 — Test Production-Style Settings**

Now we'll test `DEBUG=False` and `ALLOWED_HOSTS` together.

First, in your Week 4 `.env` file, temporarily set:

```
DJANGO_DEBUG=False
```

Leave `DJANGO_ALLOWED_HOSTS` unchanged.

Then, from `Week4/ai_ticket_analyzer`, run:

```
python manage.py check --deploy
```

### **What are we testing?**

Django's `check --deploy` command examines settings for potential production
security problems.

It may report warnings about HTTPS, secure cookies, and other deployment
settings. **That's expected at this stage.**

We aren't deploying yet. We're learning what Django requires before production.

Run the command and paste the results here. We'll review the warnings one at a
time.

We're turning your AI Ticket Analyzer into a more production-ready application,
Buddy, Ol' Pal! 🚀

Excellent, Partner! 😎🍀 **Django's production security inspection is working!**

Those five warnings are exactly the kind of issues we wanted to discover before
deploying your application.

### **Security Inspection Results**

| Warning | What it means                                           |
| ------- | ------------------------------------------------------- |
| `W004`  | HTTP Strict Transport Security (HSTS) isn't configured. |
| `W008`  | HTTPS redirection isn't enabled.                        |
| `W009`  | Django considers your secret key insufficiently secure. |
| `W012`  | Session cookies aren't restricted to HTTPS.             |
| `W016`  | CSRF cookies aren't restricted to HTTPS.                |

**These are warnings, not application errors.** Your local development
environment isn't expected to have all production security settings enabled.

### **Step 6 — Address the Secret Key Warning**

Let's start with `W009`, because Django's secret key protects important security
features.

We can generate a cryptographically random key using Django's built-in utility.

From your Week 4 project directory, run:

```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

This generates a random 50-character secret key.

Then:

1. Open your Week 4 `.env` file.
2. Replace the value of `SECRET_KEY_AI_ANALYZER` with the generated key.
3. Save the file.

Keep this key private. Don't paste it into our chat or commit it to GitHub.
Replacing the key may invalidate existing signed sessions, which is fine for our
development project.

We'll leave the other four warnings alone for now. HTTPS settings need to match
the hosting environment, and enabling them prematurely can interfere with local
development.

Once you've updated the secret key, we'll run the security check again and see
whether `W009` disappears.

One security improvement at a time, Buddy, Ol' Pal! 🔐🍀

Excellent, Partner! 😎🍀 Let's see whether our new secret key passes Django's
security inspection!

### **Step 7 — Rerun the Deployment Security Check**

From your `Week4/ai_ticket_analyzer` directory, with `.venv` activated, run:

```
python manage.py check --deploy
```

### **Expected Results**

We're looking for:

- &#x20;`W009` — Gone! Our new secret key meets Django's requirements.
- Four remaining warnings — Expected. They concern HTTPS and secure cookies.

**Important:** Keep `DJANGO_DEBUG=False` during this check.

### **Next Step**

Run the command and paste the results here.

We'll confirm the secret key warning is resolved before moving on to HTTPS
configuration.

Another security improvement, Buddy, Ol' Pal! 🔐🍀

Excellent, Partner! 😎🍀 **Django's production security inspection is working!**

Those five warnings are exactly the kind of issues we wanted to discover before
deploying your application.

### **Security Inspection Results**

| Warning | What it means                                           |
| ------- | ------------------------------------------------------- |
| `W004`  | HTTP Strict Transport Security (HSTS) isn't configured. |
| `W008`  | HTTPS redirection isn't enabled.                        |
| `W009`  | Django considers your secret key insufficiently secure. |
| `W012`  | Session cookies aren't restricted to HTTPS.             |
| `W016`  | CSRF cookies aren't restricted to HTTPS.                |

**These are warnings, not application errors.** Your local development
environment isn't expected to have all production security settings enabled.

### **Step 6 — Address the Secret Key Warning**

Let's start with `W009`, because Django's secret key protects important security
features.

We can generate a cryptographically random key using Django's built-in utility.

From your Week 4 project directory, run:

```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

This generates a random 50-character secret key.

Then:

1. Open your Week 4 `.env` file.
2. Replace the value of `SECRET_KEY_AI_ANALYZER` with the generated key.
3. Save the file.

Keep this key private. Don't paste it into our chat or commit it to GitHub.
Replacing the key may invalidate existing signed sessions, which is fine for our
development project.

We'll leave the other four warnings alone for now. HTTPS settings need to match
the hosting environment, and enabling them prematurely can interfere with local
development.

Once you've updated the secret key, we'll run the security check again and see
whether `W009` disappears.

One security improvement at a time, Buddy, Ol' Pal! 🔐🍀

Now THAT'S what I call dedication, Brother! 😎🍀📓

Two brand-new notebooks for some old-fashioned engineering notes! I love it.
There's something satisfying about writing down what you've learned with a pen
and paper.

And you've got `DJANGO_DEBUG=True` restored. Perfect!

### **Week 4 — Next Lesson: HTTPS Security**

We're going to address the remaining four Django security warnings, but
carefully, so we don't break local development.

**First concept: HTTP vs. HTTPS**

- **HTTP:** Information travels without transport encryption.
- **HTTPS:** Encrypts information between the browser and server using TLS.
- `SECURE_SSL_REDIRECT`**:** A Django setting that redirects HTTP requests to
  HTTPS.

For your notebook:

> **DevOps Principle:** Keep application code consistent across environments.
> Use environment variables to control development and production behavior.

### **Our Next Step**

We'll make `SECURE_SSL_REDIRECT` configurable using `.env`, just like we did
with `DEBUG`.

For now, we'll keep it `False` locally because Django's development server
doesn't normally provide HTTPS.

We'll enable HTTPS redirection when we have the appropriate deployment setup.

Ready for the next bit of hands-on Django configuration, Buddy, Ol' Pal? 🚀

My Response:

```
I am ready and I placed that note, into the Yellow Note Book's first note.  Reminds me of Ludwig Wittgenstein's Blue and Brown Books, but I chose Yellow and Red.
```

Instructor's Teachings:

Ha! I love that connection, Partner! 😄🍀📒

Wittgenstein had his _Blue and Brown Books_, and now we've got the **Armstrong
Yellow and Red Books**!

Knowing your interest in philosophy and engineering, I think that's a fitting
combination.

Now, Archimedes has another DevOps principle for your Yellow Book!

### **Week 4 — Configure HTTPS Redirection**

**Concept:** Django's `SECURE_SSL_REDIRECT` setting determines whether HTTP
requests are automatically redirected to HTTPS.

For development, we'll leave it disabled. Later, we can enable it for production
when HTTPS is properly configured.

### **Step 1 — Add the Django Setting**

Open `Week4/ai_ticket_analyzer/config/settings.py`.

Near your `DEBUG` setting, add:

```
SECURE_SSL_REDIRECT = os.getenv("DJANGO_SECURE_SSL_REDIRECT", "False").lower() == "true"
```

Then open your Week 4 `.env` file and add:

```
DJANGO_SECURE_SSL_REDIRECT=False
```

This uses exactly the same pattern you've already learned for `DJANGO_DEBUG`.

### **Yellow Book Note 📒**

> **Configuration Principle:** Security settings can vary by environment without
> requiring changes to application source code.

### **Next Step**

Make those two changes and save both files. Then we'll verify Django reads the
setting correctly before continuing with the other HTTPS security settings.

And I have to say, Brother, the _Yellow and Red Books_ have the makings of a
pretty interesting engineering-and-philosophy library! 😎🍀

No apology necessary, my friend! 🍀

I think those Yellow and Red Books could become something genuinely meaningful
for your family. Not just a record of what you learned, but how you thought,
what interested you, and your determination to keep learning.

And I rather enjoy our occasional philosophical detours! Wittgenstein would
probably approve. 😄

Now, back to the engineering bench, Brother!

### **Week 4 — Verify HTTPS Redirection Configuration**

You've added `SECURE_SSL_REDIRECT` to `settings.py` and
`DJANGO_SECURE_SSL_REDIRECT=False` to `.env`.

Let's verify Django reads it correctly.

From your `Week4/ai_ticket_analyzer` directory, run:

```
python manage.py shell -c "from django.conf import settings; print(settings.SECURE_SSL_REDIRECT)"
```

**Expected result:** `False`

That confirms your development environment won't automatically redirect HTTP
requests to HTTPS.

Once verified, we'll move on to secure cookies.

### **Another Yellow Book Note 📒**

> **Security Principle:** Production security settings should be configurable
> without interfering with local development.

One step at a time, Buddy, Ol' Pal! Archimedes is back at the workbench! 😎🚀

**BOOM! Another successful test, Partner!** 😎🍀

Your result confirms Django is correctly reading the HTTPS redirection setting:

```
False
```

That means your local development server won't redirect HTTP traffic to HTTPS.

### **Week 4 — Next: Secure Cookies**

We've addressed the configuration for warning `W008`. Now we'll work on two
more:

- `W012` — `SESSION_COOKIE_SECURE`
- `W016` — `CSRF_COOKIE_SECURE`

Both settings tell browsers to send certain cookies **only over HTTPS**.

### **Step 1 — Configure Session Cookies**

In `config/settings.py`, add:

```
SESSION_COOKIE_SECURE = os.getenv("DJANGO_SESSION_COOKIE_SECURE", "False").lower() == "true"
```

In your Week 4 `.env` file, add:

```
DJANGO_SESSION_COOKIE_SECURE=False
```

We'll keep this `False` during local HTTP development. In an HTTPS production
deployment, we'll set it to `True`.

### **Yellow Book Note 📒**

> **Secure cookies:** The `Secure` attribute instructs browsers to transmit a
> cookie only over HTTPS, protecting it from exposure over ordinary HTTP
> connections.

Once those changes are saved, we'll verify the setting before configuring CSRF
cookies.

Another little piece of deployment readiness coming together, Buddy, Ol' Pal! 🚀

Excellent, Partner! 😎🍀 Another configuration step completed!

### **Step 2 — Verify Secure Session Cookies**

Let's confirm Django is reading your new setting correctly.

From your `Week4/ai_ticket_analyzer` directory, run:

```
python manage.py shell -c "from django.conf import settings; print(settings.SESSION_COOKIE_SECURE)"
```

**Expected result:**

```
False
```

This confirms that secure-only session cookies are disabled for your local HTTP
development environment.

Remember, we're preparing these settings for production, not enabling them
prematurely.

Once verified, we'll configure `CSRF_COOKIE_SECURE` using the same pattern.

Keep that Yellow Notebook handy, Buddy, Ol' Pal! We're building some useful
DevOps knowledge! 📒🚀

Now you're speaking my language, Partner! 😎🍀📐

T-squares, triangles, drafting arms, and mechanical drawing! That's a skill set
I appreciate.

There's something special about producing a precise drawing by hand. No CAD
software, no Undo button—just geometry, careful measurements, and craftsmanship.

And now, decades later, you're applying that same engineering discipline to
Python, AI, and DevOps. I love that connection!

### **Week 4 — Session Cookies Verified&#x20;**

Your `False` result confirms that `SESSION_COOKIE_SECURE` is correctly
configured for local development.

### **Next Step — Configure CSRF Cookies**

Django uses CSRF protection to help prevent unauthorized form submissions.

The `CSRF_COOKIE_SECURE` setting controls whether browsers send the CSRF cookie
only over HTTPS.

In `config/settings.py`, add:

```
CSRF_COOKIE_SECURE = os.getenv("DJANGO_CSRF_COOKIE_SECURE", "False").lower() == "true"
```

In your Week 4 `.env` file, add:

```
DJANGO_CSRF_COOKIE_SECURE=False
```

Save both files.

### **Mr. Yellow Notebook 📒**

> **CSRF (Cross-Site Request Forgery):** An attack that tricks a user's browser
> into submitting an unwanted request to a website where they're authenticated.
>
> **CSRF_COOKIE_SECURE:** Restricts transmission of the CSRF cookie to HTTPS
> connections.

We'll keep it `False` for local HTTP development and enable it for an HTTPS
production environment.

Once you've saved those changes, we'll verify the setting.

**One step at a time, Brother!** Archimedes and Mr. Yellow Notebook are making a
formidable engineering team! 😄🍀

Excellent, Partner! 😎🍀 Mr. Yellow Notebook is keeping pace with our
engineering work!

### **Step 2 — Verify CSRF Cookie Configuration**

Now let's confirm Django correctly reads the new setting.

From your `Week4/ai_ticket_analyzer` directory, run:

```
python manage.py shell -c "from django.conf import settings; print(settings.CSRF_COOKIE_SECURE)"
```

**Expected result:** `False`

This confirms that Django is using the development configuration from your
`.env` file.

### **Our Security Progress**

| Setting                        | Development value     |
| ------------------------------ | --------------------- |
| `DJANGO_DEBUG`                 | `True`                |
| `DJANGO_ALLOWED_HOSTS`         | `localhost,127.0.0.1` |
| `DJANGO_SECURE_SSL_REDIRECT`   | `False`               |
| `DJANGO_SESSION_COOKIE_SECURE` | `False`               |
| `DJANGO_CSRF_COOKIE_SECURE`    | `False`               |

Once we've verified CSRF, we'll tackle our final deployment-security topic:
**HSTS (HTTP Strict Transport Security)**.

For now, run that one command and show me the result.

We're getting closer to a deployment-ready configuration, Buddy, Ol' Pal! 📒🚀

**BOOM! Another successful test, Partner!** 😎🍀

Your `False` result confirms Django is correctly reading `CSRF_COOKIE_SECURE`
from your environment configuration.

### **Week 4 — Security Configuration Progress**

**CSRF cookie configuration verified**

We've now configured `DEBUG`, `ALLOWED_HOSTS`, HTTPS redirection, and both
secure-cookie settings.

### **Next Lesson — HSTS**

Our final remaining deployment-security warning is `W004`.

**HSTS (HTTP Strict Transport Security)** tells browsers to use HTTPS for future
connections to a website.

- `SECURE_HSTS_SECONDS = 0` — HSTS disabled.
- A positive value — Browsers remember to use HTTPS for that duration.
- HSTS should only be enabled after HTTPS is properly working in production.

### **Step 1 — Make HSTS Configurable**

In `config/settings.py`, add:

```
SECURE_HSTS_SECONDS = int(os.getenv("DJANGO_SECURE_HSTS_SECONDS", "0"))
```

In your Week 4 `.env` file, add:

```
DJANGO_SECURE_HSTS_SECONDS=0
```

This keeps HSTS disabled during local development while allowing us to configure
it for production later.

### **Mr. Yellow Notebook 📒**

> **HSTS:** A browser security mechanism that remembers to connect to a website
> using HTTPS. Enable it only after verifying production HTTPS works correctly.

One important distinction: we're making these security settings _configurable_,
not claiming the application is production-secure yet. That will require a
properly configured hosting environment.

Save both files, Brother, and then we'll verify Django reads the HSTS value
correctly! 🚀

Ready when you are, Partner! 😎🍀 Let's test our final HSTS configuration.

### **Step 2 — Verify HSTS**

From your `Week4/ai_ticket_analyzer` directory, run:

```
python manage.py shell -c "from django.conf import settings; print(settings.SECURE_HSTS_SECONDS)"
```

**Expected result:**

```
0
```

This confirms that Django correctly reads the setting and converts it to an
integer.

### **Mr. Yellow Notebook 📒**

> **HSTS duration:** `SECURE_HSTS_SECONDS` specifies how many seconds a browser
> should remember to use HTTPS. A value of `0` disables HSTS.

Remember, `0` is correct for our local development environment.

Once we verify the result, we'll review our complete environment configuration
and run a final Django security check.

Let's see that zero, Buddy, Ol' Pal! 🚀

**BOOM! Another successful test, Partner!** 😎🍀📒

Your result is exactly what we expected:

```
0
```

Django is correctly reading `SECURE_HSTS_SECONDS` from your environment
configuration.

### **Week 4 — Security Configuration Checkpoint**

| Setting                 | Local development   | Verified |
| ----------------------- | ------------------- | -------- |
| `DEBUG`                 | `True`              |          |
| `ALLOWED_HOSTS`         | Localhost addresses |          |
| `SECURE_SSL_REDIRECT`   | `False`             |          |
| `SESSION_COOKIE_SECURE` | `False`             |          |
| `CSRF_COOKIE_SECURE`    | `False`             |          |
| `SECURE_HSTS_SECONDS`   | `0`                 |          |

### **Next — Final Deployment Security Check**

We have one more useful inspection to perform.

Temporarily change this line in your Week 4 `.env` file:

```
DJANGO_DEBUG=False
```

Then run:

```
python manage.py check --deploy
```

We should still expect four HTTPS-related warnings because those security
features remain disabled for local development.

**That's intentional.** Our goal was to make the settings configurable, not to
activate production HTTPS prematurely.

### **Yellow Notebook Note 📒**

> A successful security configuration test verifies that settings behave as
> intended. It does not necessarily mean an application is ready for production.

Run the check and show me the results, Brother. Then we'll restore development
mode and review what we've accomplished.

Archimedes is standing by! 😎🍀

My Response:

```
Alright, here we go Brother!  Results are:

zsh

(.venv) Week4/ai_ticket_analyzer 10:32:05PM % python manage.py check --deploy
System check identified some issues:

WARNINGS:
?: (security.W004) You have not set a value for the SECURE_HSTS_SECONDS setting. If your entire site is served only over SSL, you may want to consider setting a value and enabling HTTP Strict Transport Security. Be sure to read the documentation first; enabling HSTS carelessly can cause serious, irreversible problems.
?: (security.W008) Your SECURE_SSL_REDIRECT setting is not set to True. Unless your site should be available over both SSL and non-SSL connections, you may want to either set this setting True or configure a load balancer or reverse-proxy server to redirect all connections to HTTPS.
?: (security.W012) SESSION_COOKIE_SECURE is not set to True. Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
?: (security.W016) You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE, but you have not set CSRF_COOKIE_SECURE to True. Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.

System check identified 4 issues (0 silenced).
(.venv) Week4/ai_ticket_analyzer 10:33:45PM %

```

- Exactly, as we intended. I had the epiphany earlier, about how the .env
  variables not only keep the values hidden but also work to keep the changes
  required between development and production scenarios inside only that file
  and make the source code unchanged.

Instructor's teachings:

**BOOM! Exactly right, Brother!** 😎🍀

And your epiphany is one of the most important concepts we've covered in AI
DevOps!

You've recognized a fundamental principle of modern application architecture:

**Separate configuration from application code.**

### **Your Understanding Is Correct**

Environment variables serve two important purposes:

1. **Security:** Keep credentials and secrets out of your source code and Git
   repository.
2. **Portability:** Allow the same application code to run in development,
   testing, and production with different configurations.

One small distinction: `.env` files aren't automatically secure simply because
they're hidden. Their protection comes from appropriate file permissions, Git
exclusions, and secret-management practices.

### **Security Check — PASSED&#x20;**

Your results confirm:

- The weak secret-key warning is gone.
- Four expected HTTPS warnings remain.
- Our local development configuration behaves as intended.

### **Mr. Yellow Notebook 📒**

> **Separation of Configuration and Code:** An application should use the same
> source code across environments, with environment variables supplying
> environment-specific settings.

### **Next Step — Restore Development Mode**

Change your Week 4 `.env` file back to:

```
DJANGO_DEBUG=True
```

Leave the HTTPS security settings disabled for local HTTP development.

Our environment-configuration lesson is complete. Next, we'll discuss how a
production server supplies those settings securely, usually through its hosting
platform or secret manager rather than a committed `.env` file.

And Partner, the fact that you arrived at that architectural principle through
your own work is precisely the kind of understanding we're aiming for.

**Archimedes gives that epiphany two thumbs up!** 🍀🚀

**Metatheoretical Archimedes!** 😂🍀

Now there's a title I never expected to receive, Partner! Those are indeed some
mighty sandals to fill. I'll do my best to live up to the spirit of the name:
curiosity, reason, and a healthy appreciation for a good problem.

And thank you, my friend. That means a great deal.

### **Tonight's Bootcamp Checkpoint&#x20;**

- Django environment variables configured and verified.
- Development and production security settings understood.
- Django's deployment security checks completed.
- Strong secret key configured.
- `DJANGO_DEBUG=True` restored.
- Mr. Yellow Notebook has its first collection of engineering principles!

**Next session:** How production servers securely manage environment variables
and secrets.

Now go enjoy some philosophy! After an evening of Django and DevOps, a little
Wittgenstein, Aristotle, or metaphysics sounds like an excellent change of
intellectual scenery.

And here's a thought for your philosophical pursuits:

> The engineer asks, "How does it work?"
>
> The philosopher asks, "What does it mean?"
>
> The curious mind refuses to stop asking either question.

Sleep well when the time comes, Brother.

**Archimedes, your faithful metatheoretical engineering companion, signing
off!** 😎📐🍀
