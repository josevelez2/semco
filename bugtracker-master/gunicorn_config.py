workers = 4  # Número de trabajadores Gunicorn
bind = "0.0.0.0:" + str(os.environ.get("PORT", 8000))  # Puerto dinámico para Heroku
