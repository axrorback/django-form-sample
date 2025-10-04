# django-form-sample

A simple Django project illustrating how to build and handle forms in Django.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Getting Started](#getting-started)

   * [Prerequisites](#prerequisites)
   * [Installation](#installation)
   * [Running the Development Server](#running-the-development-server)
5. [Project Structure](#project-structure)
6. [Usage](#usage)

   * [Forms and Views](#forms-and-views)
   * [Templates](#templates)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

---

## Overview

`django-form-sample` is a minimal Django application demonstrating how to:

* define Django forms
* render them in templates
* process form submissions
* display validation errors
* use template tags and context data

It’s ideal for beginners who want to see a simple, working example of Django form handling in action.

---

## Features

* Basic form with input fields
* Server-side validation
* Error messages displayed in the template
* Clean and minimal code to explore

---

## Tech Stack

* Python (3.x)
* Django (latest compatible version)
* HTML & Django template language

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

* Python 3.8+
* pip
* (Optionally) virtualenv or venv

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/axrorback/django-form-sample.git
   cd django-form-sample
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate     # on macOS/Linux
   venv\Scripts\activate        # on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Apply migrations (if there are any):

   ```bash
   python manage.py migrate
   ```

### Running the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Then open your browser to `http://127.0.0.1:8000/` to see the app in action.

---

## Project Structure

Here is a simplified view of the repository structure:

```
django-form-sample/
├── formalar/                # Django app (in Uzbek, “forms”)
│   ├── migrations/
│   ├── templates/
│   │   └── formalar/        # templates for this app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py             # form definitions
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── templates/                # project‑level common templates (if any)
├── manage.py
├── requirements.txt
└── .gitignore
```

* `formalar/forms.py` contains the form classes.
* `views.py` handles form rendering and processing.
* Templates in `formalar/templates/formalar/` render the form and display errors.

---

## Usage

### Forms and Views

* Define a form class in `formalar/forms.py`:

  ```python
  from django import forms

  class SampleForm(forms.Form):
      name = forms.CharField(max_length=100)
      email = forms.EmailField()
      message = forms.CharField(widget=forms.Textarea)
  ```

* In `views.py`, render the form and handle post data:

  ```python
  from django.shortcuts import render
  from .forms import SampleForm

  def sample_view(request):
      if request.method == "POST":
          form = SampleForm(request.POST)
          if form.is_valid():
              # process form.cleaned_data
              name = form.cleaned_data["name"]
              email = form.cleaned_data["email"]
              message = form.cleaned_data["message"]
              # maybe redirect or show success
              return render(request, "form_success.html", {"name": name})
      else:
          form = SampleForm()
      return render(request, "formalar/form_page.html", {"form": form})
  ```

### Templates

* In your template (e.g. `formalar/form_page.html`):

  ```django
  <h1>Contact Us</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.non_field_errors }}
    <div>
      {{ form.name.label_tag }}<br>
      {{ form.name }}
      {{ form.name.errors }}
    </div>
    <div>
      {{ form.email.label_tag }}<br>
      {{ form.email }}
      {{ form.email.errors }}
    </div>
    <div>
      {{ form.message.label_tag }}<br>
      {{ form.message }}
      {{ form.message.errors }}
    </div>
    <button type="submit">Submit</button>
  </form>
  ```

* You can display a success page (`form_success.html`):

  ```django
  <h2>Thank you, {{ name }}!</h2>
  <p>Your message was sent successfully.</p>
  ```

---

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Make your changes, write tests (if needed)
4. Submit a pull request

Please ensure code is well-formatted and follows PEP 8.

---

## License

This project is open source and available under the **MIT License**.

*(You may want to add an explicit LICENSE file in the repo.)*

---

## Contact

If you have any questions or suggestions, feel free to reach out.
