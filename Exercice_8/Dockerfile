# Utilisez l'image de base Python 3.9
FROM python:3.11

# Copiez le répertoire de l'application dans l'image
COPY . /app

# Définissez le répertoire de travail sur celui de l'application
WORKDIR /app

# Installez les dépendances de l'application
RUN pip install falcon
RUN pip install gunicorn

# Exposez le port 4242
EXPOSE 4242

# Démarrez l'application en utilisant gunicorn
CMD ["gunicorn", "api:api", "-b", "0.0.0.0:4242"]