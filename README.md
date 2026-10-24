# Payment Provider Integration Family — Starter

This repository is the starting point for the **Factory Method & Abstract Factory** class activity.

The current implementation works for **Stripe** and **Adyen**, but `CheckoutService`
knows the concrete classes for every provider capability:

- payment authorization,
- refunds,
- webhook verification.

A third provider — **Mercado Pago** — is coming.

Your job is to identify the creation pressure, choose the creational pattern that best fits,
and refactor the design so the provider-specific family can change coherently.

## Repository workflow

If you are working in a pair/team:

1. **Only one teammate** clicks **Use this template → Create a new repository**.
2. The team repository must be **public**.
3. Everyone works in that same repository.
4. Submit that single public repository URL in Canvas.

Do not create one repository per teammate.

## Before you start

The starter code should begin green.

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

## Design task

Start by identifying the **product roles / capabilities** that checkout actually needs.

Then decide which creational pattern best fits the pressure.

Your refactoring must:

1. Keep checkout business logic independent of provider-specific classes.
2. Represent these capabilities explicitly:
   - authorization,
   - refund processing,
   - webhook verification.
3. Provide one creation boundary for a complete provider family.
4. Preserve working Stripe and Adyen behavior.
5. Add a **Mercado Pago** family.
6. Add or update unit tests.
7. Allow Mercado Pago to be added **without modifying checkout business logic**.

## Course constraints

Use an explicit **object-oriented design**:

- classes and objects,
- interfaces / abstract base classes where a contract is useful,
- composition,
- dependency injection.

Do not solve the exercise with standalone functions, lambdas, callback registries,
or other functional-programming alternatives.

Keep **one main class per source file**.

The pattern concept is language-agnostic; this starter uses Python only as the implementation language for the activity.

## Be ready to explain

1. What varies?
2. What stays stable?
3. Why is this a **family-level** creation problem?
4. Which creational pattern did you choose, and why?
5. Who selects the concrete provider family?
6. What complexity cost does your design introduce?

## Submission

Submit your team's **public GitHub repository URL** in Canvas.

A **Possible Solution / Reference Implementation** will be published after submissions close.
