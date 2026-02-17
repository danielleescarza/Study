# Clinic Management System of the School Clinic at St. Jude College Dasmariñas Cavite Inc.

<!-- someone was here, someone cooked here -->

## Installation

1. Clone this project:

```
git clone https://github.com/danielleescarza/Study.git
```

or

```
git clone https://github.com/danielleescarza/Study.git <project-name>
```

2. Go to the project directory:

```
cd Study
```

3. Set up a python virtual environment:

```
python -m venv env
```

4. Activate the environment:

```
.\env\Scripts\activate.bat
```

5. Install dependencies:

```
python -m pip install -r requirements.txt
```

6. Apply the migrations:

```
python manage.py migrate
```

7. Seed the database with initial data:

```
python manage.py seed_groups_permissions
```

8. Run the server:

```
python manage.py runserver
```
