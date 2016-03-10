This is a Django app that will let you see how many meals and points you have left on your Brandeis meal plan

#Installation:
    pip install -r requirements.txt

#Running:
    python manage.py runserver

#Example of using it in a different Python app:
    import requests
    r = requests.post("http://0.0.0.0:8000/points/", data={'username':'aboudaie', 'password':'AryaSuperSecurePassword'})
    plan = r.json()
    #process however you want after this

Obviously you should have the app hosted somewhere legit (and change the URL in the request) - I have a demo on Heroku at brandeis-points.herokuapp.com
