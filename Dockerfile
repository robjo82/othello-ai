# Utilisez une image de base. Remplacez <langage> et <version> par ce qui est approprié pour votre projet
# Exemples : 
# FROM node:14
# FROM python:3.9
# FROM openjdk:11
# FROM golang:1.17
# FROM ruby:2.7
FROM <langage>:<version>

LABEL authors="Robin"

# Installez les dépendances globales ou les outils nécessaires
# RUN npm install -g <outil>

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers locaux dans le conteneur
COPY . .

# Installez les dépendances du projet
# Utilisez le gestionnaire de paquets approprié pour votre langage
# Exemples :
# RUN npm install
# RUN pip install -r requirements.txt
# RUN bundle install
# RUN go mod download
RUN <commande_d_installation>

# Exposez le port que votre application utilise
# Remplacez <port> par le numéro de port approprié
EXPOSE <port>

# Commande pour exécuter votre application
# Remplacez <commande> par la commande qui lance votre application
# Exemples :
# CMD ["npm", "start"]
# CMD ["python", "app.py"]
# CMD ["java", "-jar", "app.jar"]
# CMD ["./monexecutable"]
CMD ["<commande>"]
