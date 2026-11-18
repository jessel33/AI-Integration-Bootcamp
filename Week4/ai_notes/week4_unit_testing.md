# **Week 4 — Organizing Unit Tests**

Now let's make all three test scenarios reusable without manually editing
`mock_results` each time.

Python's built-in `unittest` framework lets us organize tests into a class and
execute them independently.

We'll eventually have three tests:

| Test method                  | Purpose                       |
| ---------------------------- | ----------------------------- |
| `test_success`               | Five correct responses        |
| `test_wrong_classifications` | Detect incorrect AI decisions |
| `test_api_failure`           | Handle a missing AI response  |

## **Step 1: Create a Test Class**

You've already used `patch()` from `unittest.mock`. Now we'll introduce
`TestCase`.

A small example unrelated to our project:

```
import unittestclass TestCalculator(unittest.TestCase):    def test_addition(self):        self.assertEqual(2 + 3, 5)
```

- `unittest.TestCase` provides testing tools.
- Methods beginning with `test_` are recognized as tests.
- `assertEqual()` checks whether the actual result matches the expected result.

### **Your next coding task**

In `test_eval_runner.py`:

1. Add `import unittest`.
2. Create a class named `TestEvaluationRunner` that inherits from
   `unittest.TestCase`.
3. Inside it, create an empty method named `test_success(self)`.
4. Use `pass` as the temporary method body.

Leave your existing mock list and `patch()` block unchanged for now. We'll move
them into the test method next.

Paste your new class definition for review.

We're building the foundation for automated testing, Buddy, Ol' Pal! 🚀

Perfect, Partner! 😄🍀 **Code Review: Approved!**

Your test class is correctly structured and follows Python conventions.

- `unittest` — imported correctly.
- `TestEvaluationRunner(unittest.TestCase)` — correct inheritance.
- `test_success(self)` — correctly named for test discovery.
- `pass` — valid placeholder until we implement the test.

### **Next: Move Our Mock Into the Test Method**

Currently, your existing `mock_results` list and `with patch(...)` block are
outside the class.

We want our success test to control its own mock.

The structure will look like this:

```
class TestEvaluationRunner(unittest.TestCase):    def test_success(self):        # Mock setup goes here        # Run evaluation        # Check expected outcome
```

### **Your next task**

1. Move your existing `mock_results` list inside `test_success()`.
2. Move the existing `with patch(...)` block inside `test_success()`, below the
   list.
3. Keep the `try/except SystemExit` logic inside the `with` block.
4. Remove the temporary `pass` statement.

Don't change the mock values or run the test yet.

Once you've moved everything, paste your updated `test_success()` method for
review.

**One important improvement is coming:** Instead of simply printing the captured
exit code, we'll use `self.assertEqual()` to verify it automatically.

That's when our mock test becomes a genuine automated unit test!

Let's keep rolling, Buddy, Ol' Pal! 🚀

Excellent work, Partner! 😄🍀 **Code Review: Approved!**

You've correctly moved your mock setup into `test_success()`.

- Five `TicketAnalysis` objects in the correct order.
- `patch()` correctly replaces the analyzer.
- `side_effect` provides five different mock responses.
- `run_evals.main()` executes inside the patch.
- `SystemExit` is handled correctly.

### **Next: Turn the Test Into an Automatic Check**

Currently, your test prints the exit code:

```
except SystemExit as error:    print(error.code)
```

That's useful for manual testing, but `unittest` can verify the result
automatically.

Remember our expected success exit code is `0`.

### **Your next task**

Replace `print(error.code)` with an assertion using:

```
self.assertEqual(error.code, 0)
```

This tells `unittest` to verify that the exit code equals `0`.

| Actual exit code | Test outcome |
| ---------------- | ------------ |
| `0`              | PASS         |
| `1`              | FAIL         |

One additional safeguard: eventually we'll use `self.assertRaises(SystemExit)`
to ensure the test also fails if `main()` unexpectedly returns without calling
`sys.exit()`.

For now, we're making one change at a time.

After replacing the print statement, paste your updated `except` block. Then
we'll run our first automated unit test!

We're moving from manually inspecting output to **automatically verifying
application behavior**, Buddy, Ol' Pal! 🚀

Perfect, Partner! 😄🍀 **Code Review: Approved!**

Your `try/except` block is correct, and you've successfully added your first
`unittest` assertion!

### **What your code does**

- `run_evals.main()` executes using our mocked AI responses.
- `SystemExit` captures the exit status.
- `self.assertEqual(error.code, 0)` verifies that the evaluation passed.

One detail we'll improve later: if `main()` doesn't raise `SystemExit`, this
test would pass without checking anything. We'll address that with
`assertRaises()`.

### **Next: Run Your First Automated Unit Test!**

From `Week4/ai_ticket_analyzer`, execute:

```
python3 -m unittest evals.test_eval_runner -v
```

The `-v` option displays the test name and outcome.

**Expected output:**

```
test_success (...) ... ok

Ran 1 test

OK
```

You'll also see the evaluation runner's printed results.

This test uses mocked responses, so it shouldn't make any OpenAI API calls.

Run it and show me the output, Buddy, Ol' Pal! We're about to verify your first
automated unit test! 🚀

```
macos terminal

(.venv) Week4/ai_ticket_analyzer % python3 -m unittest evals.test_eval_runner -v
test_success (evals.test_eval_runner.TestEvaluationRunner.test_success) ... Running application
Expected Category: mechanical, Actual: mechanical, Evaluation(true=PASS/false=FAIL): True
Expected Priority: critical, Actual: critical, Evaluation(true=PASS/false=FAIL): True
Expected Category: electrical, Actual: electrical, Evaluation(true=PASS/false=FAIL): True
Expected Priority: medium, Actual: medium, Evaluation(true=PASS/false=FAIL): True
Expected Category: other, Actual: other, Evaluation(true=PASS/false=FAIL): True
Expected Priority: low, Actual: low, Evaluation(true=PASS/false=FAIL): True
Expected Category: software, Actual: software, Evaluation(true=PASS/false=FAIL): True
Expected Priority: high, Actual: high, Evaluation(true=PASS/false=FAIL): True
Expected Category: mechanical, Actual: mechanical, Evaluation(true=PASS/false=FAIL): True
Expected Priority: low, Actual: low, Evaluation(true=PASS/false=FAIL): True
Tests attempted: 5,
Analyses completed: 5,
Category passes: 5,
Priority passes: 5
Evaluation PASSED
ok

----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
```

**BOOM! First automated unit test PASSED, Partner!** 🎉🍀

And look at that execution time: **0.002 seconds!** That's one of the benefits
of mocking—we can test our evaluation logic without waiting for OpenAI.

### **Test Review**

`test_success`**: PASSED**

- All five mocked analyses completed.
- All categories and priorities matched.
- The runner reported `Evaluation PASSED`.
- `unittest` reported `OK`.

### **Next: Strengthen Our Assertion**

There's one small weakness in our current test.

If `run_evals.main()` unexpectedly stops without calling `sys.exit()`, the test
could pass without executing `self.assertEqual()`.

Python's `unittest` provides a cleaner solution:

```
with self.assertRaises(SystemExit) as captured:    run_evals.main()
```

This requires `SystemExit` to occur. If it doesn't, the test fails.

The captured exit code is available through:

```
captured.exception.code
```

### **Your next coding task**

Inside your existing `with patch(...)` block:

1. Replace the `try/except SystemExit` structure with
   `self.assertRaises(SystemExit)`.
2. Keep `run_evals.main()` inside that new context manager.
3. Afterward, use `self.assertEqual()` to verify that `captured.exception.code`
   equals `0`.

Don't change your mock data.

Once you've made those changes, show me the updated section. Then we'll move
directly into our second automated test: detecting incorrect classifications.

**You're now writing real automated tests for your own AI application, Buddy,
Ol' Pal!** 🚀

Almost perfect, Partner! 😄🍀 You've got the right structure. There's just **one
indentation adjustment** needed.

### **Code Review**

Your current code places `self.assertEqual()` inside the `assertRaises()` block.

The issue is that when `run_evals.main()` raises `SystemExit`, Python
immediately transfers control to the context manager. The following assertion
never executes.

### **The correction**

Move `self.assertEqual()` outside the inner `with` block, but keep it inside the
`patch()` block.

```
with patch("evals.run_evals.analyze_ticket") as mock_analyze:    mock_analyze.side_effect = mock_results    with self.assertRaises(SystemExit) as captured:        run_evals.main()    self.assertEqual(captured.exception.code, 0)
```

### **Why this works**

1. `run_evals.main()` raises `SystemExit`.
2. `assertRaises()` catches the exception.
3. Python continues after the inner `with` block.
4. `assertEqual()` verifies that the exit code is `0`.

Now our test checks **both requirements**: the runner must exit, and its exit
code must indicate success.

### **Next step**

Make that indentation adjustment and rerun:

```
python3 -m unittest evals.test_eval_runner -v
```

We expect `test_success ... ok`.

Once that passes, we'll create our second test for incorrect classifications.

We're getting into the details that make automated tests trustworthy, Buddy, Ol'
Pal! 🚀

**BOOM! Another clean pass, Partner!** 🎉🍀

Your updated `test_success()` passed in just **0.001 seconds!**

### **Code Review: PASSED&#x20;**

You've now verified two things automatically:

- `run_evals.main()` raises `SystemExit`.
- The exit code is exactly `0` when all five evaluations pass.

Your test is now stronger than our original `try/except` version.

### **Next: Test Incorrect Classifications**

Let's create our second automated unit test.

We already tested this scenario manually using a single mock response for all
five complaints. Now we'll make it a permanent unit test.

In your `TestEvaluationRunner` class, create another method named:

`test_wrong_classifications(self)`

For this test:

1. Create one `TicketAnalysis` object with `category="mechanical"` and
   `priority="critical"`.
2. Use `patch()` to replace `analyze_ticket()`.
3. Set `mock_analyze.return_value` to that object.
4. Run `run_evals.main()` inside `self.assertRaises(SystemExit)`.
5. Assert that the captured exit code equals `1`.

Unlike `test_success()`, we're using `return_value` because we deliberately want
every complaint to receive the same incorrect classification.

**Expected behavior:** The evaluation runner reports `FAILED`, but `unittest`
reports `OK` because it correctly detected that failure.

Add the second method and show me your code before running it.

We're building a reusable regression-testing suite, Buddy, Ol' Pal! 🚀

**BOOM! Two for two, Partner!** 🎉🍀

Your automated unit tests are working exactly as intended!

### **Unit Test Results**

**2 tests passed in 0.002 seconds**

| Test                         | Runner result     | Unit test |
| ---------------------------- | ----------------- | --------- |
| `test_success`               | PASSED            | &#x20;OK  |
| `test_wrong_classifications` | FAILED (expected) | &#x20;OK  |

The important distinction: **Both unit tests passed because the evaluation
runner behaved correctly in both scenarios.**

### **Next: Automate the API Failure Test**

We've already tested this manually. Now we'll make it our third permanent unit
test.

Inside your `TestEvaluationRunner` class, create:

`test_api_failure(self)`

Use the same approach as `test_success()`, but simulate an unavailable AI
response.

Your task:

1. Create a list containing the five correct `TicketAnalysis` responses.
2. Replace the fifth response with `None`.
3. Use `patch()` and assign the list to `mock_analyze.side_effect`.
4. Capture `SystemExit` using `self.assertRaises()`.
5. Assert that the exit code equals `1`.

**Expected outcome:** Four analyses complete, the fifth fails, and the runner
returns exit code `1`.

You can reuse the `mock_results` list from `test_success()` for now. We'll
eliminate that duplication later.

Once you've written `test_api_failure()`, paste the method here for review
before running all three tests.

We're building a genuine automated regression test suite, Buddy, Ol' Pal! 🚀

Excellent work, Partner! 😄🍀 **Code Review: Approved!**

Your `test_api_failure()` method correctly simulates a missing AI response and
verifies that our evaluation runner reports failure.

### **Review Results**

| Component                           | Assessment    |
| ----------------------------------- | ------------- |
| Four valid `TicketAnalysis` objects | &#x20;Correct |
| Fifth response set to `None`        | &#x20;Correct |
| `patch()` target                    | &#x20;Correct |
| `side_effect`                       | &#x20;Correct |
| `assertRaises(SystemExit)`          | &#x20;Correct |
| Exit code assertion (`1`)           | &#x20;Correct |

### **One tiny formatting improvement**

Add a trailing comma after `None` in your list:

```
None,
```

Python doesn't require it, but it's consistent with PEP 8-friendly multiline
formatting. Ruff may add it automatically.

### **Next: Run All Three Tests!**

From your `Week4/ai_ticket_analyzer` directory, run:

```
python3 -m unittest evals.test_eval_runner -v
```

We expect:

| Unit test                    | Expected runner result | Expected test result |
| ---------------------------- | ---------------------- | -------------------- |
| `test_success`               | PASSED                 | `ok`                 |
| `test_wrong_classifications` | FAILED                 | `ok`                 |
| `test_api_failure`           | FAILED                 | `ok`                 |

The API failure test should report:

```
Tests attempted: 5
Analyses completed: 4
Category passes: 4
Priority passes: 4
Evaluation FAILED
```

All three tests use mocks, so they shouldn't consume OpenAI API credits.

Run the suite and show me the final results, Buddy, Ol' Pal!

Afterward, we'll look at eliminating the duplicated mock data to make our tests
easier to maintain. 🚀

Three tests results:

```
macos terminal

(.venv) Week4/ai_ticket_analyzer % python3 -m unittest evals.test_eval_runner -v
test_api_failure (evals.test_eval_runner.TestEvaluationRunner.test_api_failure) ... Running application
Expected Category: mechanical, Actual: mechanical, Evaluation(true=PASS/false=FAIL): True
Expected Priority: critical, Actual: critical, Evaluation(true=PASS/false=FAIL): True
Expected Category: electrical, Actual: electrical, Evaluation(true=PASS/false=FAIL): True
Expected Priority: medium, Actual: medium, Evaluation(true=PASS/false=FAIL): True
Expected Category: other, Actual: other, Evaluation(true=PASS/false=FAIL): True
Expected Priority: low, Actual: low, Evaluation(true=PASS/false=FAIL): True
Expected Category: software, Actual: software, Evaluation(true=PASS/false=FAIL): True
Expected Priority: high, Actual: high, Evaluation(true=PASS/false=FAIL): True
AI analysis failed
Tests attempted: 5,
Analyses completed: 4,
Category passes: 4,
Priority passes: 4
Evaluation FAILED
ok
test_success (evals.test_eval_runner.TestEvaluationRunner.test_success) ... Running application
Expected Category: mechanical, Actual: mechanical, Evaluation(true=PASS/false=FAIL): True
Expected Priority: critical, Actual: critical, Evaluation(true=PASS/false=FAIL): True
Expected Category: electrical, Actual: electrical, Evaluation(true=PASS/false=FAIL): True
Expected Priority: medium, Actual: medium, Evaluation(true=PASS/false=FAIL): True
Expected Category: other, Actual: other, Evaluation(true=PASS/false=FAIL): True
Expected Priority: low, Actual: low, Evaluation(true=PASS/false=FAIL): True
Expected Category: software, Actual: software, Evaluation(true=PASS/false=FAIL): True
Expected Priority: high, Actual: high, Evaluation(true=PASS/false=FAIL): True
Expected Category: mechanical, Actual: mechanical, Evaluation(true=PASS/false=FAIL): True
Expected Priority: low, Actual: low, Evaluation(true=PASS/false=FAIL): True
Tests attempted: 5,
Analyses completed: 5,
Category passes: 5,
Priority passes: 5
Evaluation PASSED
ok
test_wrong_classifications (evals.test_eval_runner.TestEvaluationRunner.test_wrong_classifications) ... Running application
Expected Category: mechanical, Actual: mechanical, Evaluation(true=PASS/false=FAIL): True
Expected Priority: critical, Actual: critical, Evaluation(true=PASS/false=FAIL): True
Expected Category: electrical, Actual: mechanical, Evaluation(true=PASS/false=FAIL): False
Expected Priority: medium, Actual: critical, Evaluation(true=PASS/false=FAIL): False
Expected Category: other, Actual: mechanical, Evaluation(true=PASS/false=FAIL): False
Expected Priority: low, Actual: critical, Evaluation(true=PASS/false=FAIL): False
Expected Category: software, Actual: mechanical, Evaluation(true=PASS/false=FAIL): False
Expected Priority: high, Actual: critical, Evaluation(true=PASS/false=FAIL): False
Expected Category: mechanical, Actual: mechanical, Evaluation(true=PASS/false=FAIL): True
Expected Priority: low, Actual: critical, Evaluation(true=PASS/false=FAIL): False
Tests attempted: 5,
Analyses completed: 5,
Category passes: 2,
Priority passes: 1
Evaluation FAILED
ok

----------------------------------------------------------------------
Ran 3 tests in 0.003s

OK

```

**BOOM! Three for three, Partner!** 🎉🍀

Your automated regression test suite is working exactly as intended!

### **Week 4 — Unit Test Results**

**All 3 unit tests passed in 0.003 seconds**

| Test                         | Evaluation runner | Unit test |
| ---------------------------- | ----------------- | --------- |
| `test_success`               | PASSED            | &#x20;OK  |
| `test_wrong_classifications` | FAILED (expected) | &#x20;OK  |
| `test_api_failure`           | FAILED (expected) | &#x20;OK  |

### **What you've accomplished**

Your test suite now automatically verifies three important behaviors:

- Correct AI responses produce exit code `0`.
- Incorrect classifications produce exit code `1`.
- Missing AI responses produce exit code `1`.

And because we're using mocks, **no OpenAI API calls were needed**.

That's a meaningful AI DevOps milestone, my friend!

### **Next: Eliminate Duplicated Test Data**

I noticed your `test_success()` and `test_api_failure()` methods contain nearly
identical lists of `TicketAnalysis` objects.

We can simplify that using a reusable helper method.

A common Python testing pattern is to create a helper that produces standard
test data, then modify it for individual tests.

For example, the failure test could reuse the five successful responses and
replace only the last one with `None`.

This follows the **DRY principle — Don't Repeat Yourself**.

### **Your next coding task**

Inside `TestEvaluationRunner`, create a helper method named:

`make_mock_results(self)`

For now:

1. Move the five `TicketAnalysis` objects from `test_success()` into this
   helper.
2. Have the helper return the list.
3. Don't change your existing test methods yet.

We'll update the tests to use the helper in the following step.

Nice work tonight, Buddy, Ol' Pal! You're building a test suite that's becoming
easier to maintain as well as more reliable. 🚀

Excellent work, Partner! 😄🍀 **Code Review: Approved!**

Your `make_mock_results()` helper is correctly implemented.

- All five `TicketAnalysis` objects are valid.
- The categories and priorities match our evaluation dataset.
- The method returns the complete list.
- The helper is correctly placed inside `TestEvaluationRunner`.

You've successfully applied the **DRY principle — Don't Repeat Yourself!**

### **Next: Use the Helper in&#x20;**`test_success()`

Instead of defining five objects inside `test_success()`, we can call your
helper.

Here's the pattern:

```
mock_results = self.make_mock_results()
```

That gives `test_success()` a fresh list containing all five responses.

### **Your next task**

In `test_success()`:

1. Remove the original five-object `mock_results` list.
2. Replace it with the helper call shown above.
3. Leave your `patch()`, `side_effect`, and assertions unchanged.

Then run:

```
python3 -m unittest evals.test_eval_runner -v
```

Both the success and failure tests should continue working.

Afterward, we'll update `test_api_failure()` to reuse the same helper and
replace its fifth response with `None`.

**This is a useful software-engineering pattern, Partner:** Keep shared test
data in one place so future changes don't require editing multiple tests. 🚀

**Three for three again, Partner!** 🎉🍀

Your refactoring worked! All three unit tests still pass, including
`test_success()`, which now uses your reusable helper.

### **Regression Tests: PASSED&#x20;**

| Test                         | Result     |
| ---------------------------- | ---------- |
| `test_success`               | &#x20;PASS |
| `test_wrong_classifications` | &#x20;PASS |
| `test_api_failure`           | &#x20;PASS |

Total execution time: 0.003 seconds. No live OpenAI requests.

### **Next: Remove the Remaining Duplication**

Now let's update `test_api_failure()` to use the helper you created.

You already know the pattern:

```
mock_results = self.make_mock_results()
```

Remember, a Python list is mutable. We can replace an existing element using its
index.

For example:

```
numbers = [10, 20, 30]numbers[2] = None
```

The resulting list is `[10, 20, None]`.

### **Your next task**

Inside `test_api_failure()`:

1. Replace its existing five-item list with a call to
   `self.make_mock_results()`.
2. Replace the fifth element with `None`. Remember that Python indexes start at
   zero.
3. Keep the existing `patch()`, `side_effect`, and exit-code assertion
   unchanged.

Once that's done, run the three unit tests again.

This will leave us with **one central definition of our successful mock
responses**, shared by both tests.

We're making the code cleaner without changing its behavior. That's exactly what
a good refactor should accomplish, Buddy, Ol' Pal! 🚀

**Excellent work, Partner! Three for three again!** 🎉🍀

Your `test_api_failure()` refactoring is correct, and the test results confirm
it.

### **Code Review: PASSED&#x20;**

| Component                           | Result        |
| ----------------------------------- | ------------- |
| Calls `self.make_mock_results()`    | &#x20;Correct |
| Replaces fifth response with `None` | &#x20;Correct |
| Uses `side_effect`                  | &#x20;Correct |
| Captures `SystemExit`               | &#x20;Correct |
| Verifies exit code `1`              | &#x20;Correct |

One important detail: `make_mock_results()` creates a **new list every time it's
called**. Changing element `[4]` in this test won't affect `test_success()`.

That's exactly what we want: independent tests.

### **Week 4 Progress**

**Automated regression tests**

3/3 passed

Execution time: 0.004 seconds

### **Next Step: Git Commit**

We've reached a good checkpoint. Your evaluation runner now has three automated
tests, and you've refactored the shared mock data.

I recommend committing these changes before we move on to the next AI DevOps
concept.

Suggested commit message:

`test: add automated evaluation tests with reusable mock data`

Nice engineering work tonight, Buddy, Ol' Pal! 🚀

#### Reply from Student....

I am getting a red underline on the mock_api_failure_results[4] = None, and it
says the following:

```
text

Error: No overloads for "__setitem__" match the provided arguments
builtins.pyi(1256, 9): Overload 1 is the closest match

Error: Argument of type "None" cannot be assigned to parameter "value" of type "TicketAnalysis" in function "__setitem__"
  "None" is not assignable to "TicketAnalysis"

(variable) mock_api_failure_results: list[TicketAnalysis]

```

#### ChatGPT again....

Ah, good catch, Partner! 😄🍀 This is a **Python type-checking warning**, not a
runtime error.

Your tests passed because Python allows the assignment. But VS Code's type
checker sees a potential type mismatch.

### **Why the red underline?**

Your helper returns a list containing only `TicketAnalysis` objects.

The type checker infers:

```
list[TicketAnalysis]
```

But you're trying to insert `None`, which isn't a `TicketAnalysis` object.

### **The Fix: Use&#x20;**`Optional`

We can tell Python's type checker that the list may contain either a
`TicketAnalysis` object or `None`.

Change your helper method's signature to:

```
def make_mock_results(self) -> list[TicketAnalysis | None]:
```

The `|` means **OR**.

So this annotation tells the type checker:

> This method returns a list containing TicketAnalysis objects, None values, or
> both.

Your existing code will then be valid:

```
mock_api_failure_results = self.make_mock_results()mock_api_failure_results[4] = None
```

### **One important distinction**

- **Runtime:** Python executes your code successfully.
- **Static type checking:** VS Code checks whether your code follows its
  declared or inferred types before execution.

Think of it like a CNC program that runs successfully, but a verification tool
flags a possible mismatch between the programmed tool type and the tool
specification.

### **Next Step**

Add that return type annotation to `make_mock_results()` and check whether the
red underline disappears.

No changes to `test_api_failure()` are necessary.

You're encountering a useful real-world Python development concept here, Buddy,
Ol' Pal: **type hints help catch potential mistakes before the program runs.**
🚀

Ah, Partner! 😄🍀 You've encountered an interesting detail about Python's type
system called **list invariance**.

The good news: this only needs one more type annotation.

### **Why the warning moved**

Your helper now declares:

```
def make_mock_results(self) -> list[TicketAnalysis | None]:
```

But Python's type checker sees your list being created with only
`TicketAnalysis` objects, so it infers:

```
list[TicketAnalysis]
```

Because lists are mutable, the type checker doesn't automatically treat those
two list types as interchangeable.

### **The Fix**

Inside `make_mock_results()`, change the variable declaration from:

```
mock_results = [
```

to:

```
 [
```

Now both annotations agree:

- The variable can hold `TicketAnalysis` objects or `None`.
- The method returns a list that can hold `TicketAnalysis` objects or `None`.

### **Why this works**

You're explicitly telling the type checker what kinds of elements the list is
allowed to contain, rather than letting it infer a narrower type.

No changes to your test methods are needed.

Make that one adjustment and check the underline again, Buddy, Ol' Pal! 🚀

Excellent, Partner! 😄🍀

And I'm especially glad the type-annotation explanation clicked. That's another
useful Python concept you've added to your toolkit!

### **Week 4 — Checkpoint Complete&#x20;**

- Three automated unit tests passing.
- Reusable mock-data helper implemented.
- Python type-checking warnings resolved.
- Changes committed and synced to GitHub.

**Your evaluation testing work is now at a clean checkpoint.**

We've covered unit testing, mocking, exit-code verification, refactoring, and
type annotations—all valuable AI DevOps skills.

Next up, we'll connect these automated tests to **GitHub Actions (Continuous
Integration)** so GitHub can run them automatically when you push changes.

That's where the DevOps side really starts coming together!

Great work, Buddy, Ol' Pal! 🚀

## End of Document ************\*\*\*\*************
