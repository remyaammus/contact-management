# contact-management
Simple Contact Management app

## Prerequisites
1. Python 3.x
2. Git (to clone the repo)

### Create and Activate virtualenv
1. `pip3 install virtualenv`
2. `virtualenv -p python3.x my_env`  (*replace `python3.x` with any available python verson. Ex: `python3.6`* )
3. Activate virtualenv
    1. **For Ubuntu/Linux** `source my_env/bin/activate`
    2. **For Windows** `\my_env\Scripts\activate.bat`
4. Clone repository `https://github.com/remyaammus/contact-management.git`
5. `cd contact-management/`
6. Install dependencies `pip install -r requirements.txt`
8. `export FLASK_APP='run.py' `
9. `export FULLCONTACT_API_KEY=YOUR_API_KEY`
9. migrate the database
10. `flask db upgrade` 
10.  run the app `flask run`

## end-points
1. `/` : List all contacts in db
3. `/<contact_id>/` : Details of a specific contact
2. `/add/` : Create new contact
4. `/delete/<contact_id>/` : Delete specific contact from db
5. `/search/<search_term>/` : Search against db entries (db lookup will be against `first_name`, `last_name` and `email` fields)