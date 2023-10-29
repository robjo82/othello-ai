**Note: A French version of this README is available right after this section.**

# Project Name

Project description.

## Table of Contents

- [Prerequisites](#prerequisites)
- [General Project Structure](#general-project-structure)
  - [File Tree](#file-tree)
  - [Description](#description)
  - [Best Practices on Branching](#best-practices-on-branching)
  - [Best Practices on Commits](#best-practices-on-commits)
  - [Best Practices on Pull Requests](#best-practices-on-pull-requests)
- [Configuration Steps](#configuration-steps)
  - [GitHub](#github)
  - [SonarQube](#sonarqube)
  - [SSH Configuration](#ssh-configuration)
  - [GPG Configuration](#gpg-configuration)
  - [CI Configuration](#ci-configuration)
- [Customization](#customization)
  - [Dockerfile](#dockerfile)
  - [Procfile](#procfile)
  - [Configuration Files](#configuration-files)
- [NPM Scripts](#npm-scripts)
- [License](#license)

---

## Prerequisites

- [Node.js](https://nodejs.org/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)
- [GPG](https://gnupg.org/)
- [SonarQube](https://www.sonarqube.org/)
- [GitHub](https://github.com)
- [Heroku](https://www.heroku.com/)
- [Semantic Release](https://semantic-release.gitbook.io/)
- [Husky](https://typicode.github.io/husky/#/)
- [Commitlint](https://commitlint.js.org/#/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

## General Project Structure

### File Tree

```
.
├── .github
│   ├── PULL_REQUEST_TEMPLATE
│   │   └── pull_request_template.md
│   └── workflows
│       └── build.yml
├── src
├── .gitignore
├── Dockerfile
├── LICENSE
├── package.json
├── Procfile
└── README.md
```


### Description

- `pull_request_template.md`: Pull request template.
- `build.yml`: CI pipeline, based on GitHub Actions.
- `src`: Folder containing the source code of the application.
- `.gitignore`: Configuration file to ignore certain files in Git.
- `Dockerfile`: Configuration file for creating a Docker image.
- `LICENSE`: License file.
- `package.json`: Configuration file for NPM, including husky and semantic-release.
- `Procfile`: Configuration file for Heroku.
- `README.md`: Project description file.

### Best Practices on Branching

- `main`: Main branch of the project. It is protected and can only be modified through pull requests. It is automatically deployed to Heroku.
- `develop`: Development branch. It is protected and can only be modified through pull requests. It can be considered as a pre-production branch, and deployed to Heroku if needed.
- `feature/<ticket_number>`: Feature branch. Created from `develop` and merged back into `develop` through a pull request.
- `hotfix/<ticket_number>`: Hotfix branch. Created from `main` and merged back into `main` through a pull request.

### Best Practices on Commits

- Commit messages should be written in English, in the present tense.
- Commit messages should be written using the [Conventional Commits](https://www.conventionalcommits.org/) convention, i.e., following the format: `<type>[optional scope]: <description> [optional issue]`.
- Adhering to these conventions allows for automated version management and package publishing.

### Best Practices on Pull Requests

- Pull requests should be written in English, in the present tense.
- A pull request template is available in the `.github/PULL_REQUEST_TEMPLATE/pull_request_template.md` directory.
- Pull requests should be assigned to a reviewer.

---

## Configuration Steps

### GitHub

1. **Create a new repository on GitHub**: Use this template to create a new GitHub repository.
2. **Clone the repository**: Clone the repository onto your local machine.

### SonarQube

1. **Create a Project**: Go to your SonarQube instance and create a new project.
2. **Generate a Key**: Generate an API key for your project.
3. **Create a GitHub Secret**: Go to your GitHub repository settings, then to `Secrets`, and create a new secret called `SONAR_TOKEN` with the generated API key.

---

### SSH Configuration

To clone this project, make sure you have configured your SSH keys. You should have the following files in your `~/.ssh/` directory:

- `config`
- `id_rsa_personal`
- `id_rsa_personal.pub`
- `id_rsa_pro`
- `id_rsa_pro.pub`
- `known_hosts`

If you use multiple GitHub accounts (personal and professional, for example), make sure your `~/.ssh/config` file is correctly configured.

**Clone the project with SSH:**

```bash
git clone git@github.com-personal:<your_username>/<project_name>.git
# or for a professional account
git clone git@github.com-pro:<your_username>/<project_name>.git
```

If your `~/.ssh/` directory does not contain the files listed above, you can either retrieve them from a backup or generate them again by following the actions below.

**Generate a new SSH key:**

 ```bash
 ssh-keygen -t rsa -b 4096 -C "<YOUR_EMAIL_ADDRESS>"
 ```

**Add the SSH key to the SSH agent:**

```bash
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_rsa_personal
  ssh-add ~/.ssh/id_rsa_pro
  ```

**Add the SSH key to GitHub:**

1. Go to your GitHub account settings, then to `SSH and GPG keys`.
2. Click on `New SSH key`.
3. Paste the previously exported SSH key into the `Key` field.

### GPG Configuration
Ensure you've configured your GPG key. You should have the following files in your ~/.gnupg/ directory:

- `pubring.kbx`
- `trustdb.gpg`

If these files are not present, you can either retrieve them from a backup or generate them anew by following the steps below.

**Import an existing GPG key:**

```bash
gpg --import <PATH_TO_KEY>
```

**Generate a new GPG key:**

```bash
gpg --full-generate-key
```

**List GPG keys:**

```bash
gpg --list-secret-keys --keyid-format LONG
```

**Export the GPG key:**

```bash
gpg --armor --export <KEY_ID>
```

**Add the GPG key to Git:**

```bash
git config --global user.signingkey <KEY_ID>
```

**Add the GPG key to GitHub:**

1. Go to your GitHub account settings, then to SSH and GPG keys.
2. Click on New GPG key.
3. Paste the previously exported GPG key into the Key field.

### CI Configuration

1. **Write Access**: Make sure your CI pipeline has write access to your repository. Check the settings at [this URL](https://github.com/robjo82/ci-template/settings/actions).
2. **Branch Rules for `main`**:
    - Disallow `force-push`.
    - Require code review before merging.
    - Require CI to pass before merging.

---

## Customization

### Dockerfile
- The `Dockerfile` is configured for a basic environment. Adapt the steps according to your application and programming language.

### Procfile
- The `Procfile` contains commented examples for different types of applications. Uncomment and modify the line that corresponds to your application.

### Configuration Files
- Modify configuration files like `.gitignore`, `package.json`, etc., according to your project needs.

---

## NPM Scripts
- `semantic-release`: To automate version management and package publishing. It is configured to run only on the `main` branch. The initial setup on version numbers is as follows: `1.0.0` for the first release, then `1.0.1` for bug fixes, `1.1.0` for new features, and `2.0.0` for major changes. For more information, consult the [semantic-release](https://semantic-release.gitbook.io/semantic-release/) documentation.

---

## License
This project is under the MIT license - see the [LICENSE](LICENSE) file for more details.
    
---

# 

# 

# Nom du Projet

Description du projet.

## Sommaire

- [Prérequis](#prérequis)
- [Structure générale des projets](#structure-générale-des-projets)
   - [Arborescence](#arborescence)
   - [Description](#description)
   - [Bonnes pratiques sur les branches](#bonnes-pratiques-sur-les-branches)
   - [Bonnes pratiques sur les commits](#bonnes-pratiques-sur-les-commits)
   - [Bonnes pratiques sur les pull requests](#bonnes-pratiques-sur-les-pull-requests)
- [Étapes de Configuration](#étapes-de-configuration)
   - [GitHub](#github)
   - [SonarQube](#sonarqube)
   - [Configuration SSH](#configuration-ssh)
   - [Configuration GPG](#configuration-gpg)
   - [Configuration CI](#configuration-ci)
- [Personnalisation](#personnalisation)
   - [Dockerfile](#dockerfile)
   - [Procfile](#procfile)
   - [Fichiers de Configuration](#fichiers-de-configuration)
- [Scripts NPM](#scripts-npm)
- [Licence](#licence)

---

## Prérequis

- [Node.js](https://nodejs.org/fr/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)
- [GPG](https://gnupg.org/)
- [SonarQube](https://www.sonarqube.org/)
- [GitHub](https://github.com)
- [Heroku](https://www.heroku.com/)
- [Semantic Release](https://semantic-release.gitbook.io/semantic-release/)
- [Husky](https://typicode.github.io/husky/#/)
- [Commitlint](https://commitlint.js.org/#/)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
---

## Structure générale des projets

### Arborescence
    
 ```
 .
 ├── .github
 │   ├── PULL_REQUEST_TEMPLATE
 │   │   └── pull_request_template.md
 │   └── workflows
 │       └── build.yml
 ├── src
 ├── .gitignore
 ├── Dockerfile
 ├── LICENSE
 ├── package.json
 ├── Procfile
 └── README.md
 ```

### Description

- `pull_request_template.md` : Modèle de pull request.
- `build.yml` : Pipeline de CI, basé sur GitHub Actions.
- `src` : Dossier contenant le code source de l'application.
- `.gitignore` : Fichier de configuration pour ignorer certains fichiers dans Git.
- `Dockerfile` : Fichier de configuration pour créer une image Docker.
- `LICENSE` : Fichier de licence.
- `package.json` : Fichier de configuration pour NPM, notamment husky et semantic-release.
- `Procfile` : Fichier de configuration pour Heroku.
- `README.md` : Fichier de description du projet.

### Bonnes pratiques sur les branches

- `main` : Branche principale du projet. Elle est protégée et ne peut être modifiée que par le biais de pull requests. Elle est automatiquement déployée sur Heroku.
- `develop` : Branche de développement. Elle est protégée et ne peut être modifiée que par le biais de pull requests. Elle peut être considérée comme une branche de pré-production, et déployée si besoin sur Heroku.
- `feature/<numéro du ticket associé à la tache>` : Branche de fonctionnalité. Elle est créée à partir de `develop` et fusionnée dans `develop` par le biais d'une pull request.
- `hotfix/<numéro du ticket associé à la tache>` : Branche de correction. Elle est créée à partir de `main` et fusionnée dans `main` par le biais d'une pull request.

### Bonnes pratiques sur les commits

- Les messages de commit doivent être rédigés en anglais, au présent.
- Les messages de commit doivent être rédigés en utilisant la convention [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), c'est-à-dire en respectant le format suivant : `<type>[optional scope]: <description> [optional issue]`.
- Le respect de ces conventions permet d'automatiser la gestion des versions et la publication du package.

### Bonnes pratiques sur les pull requests

- Les pull requests doivent être rédigées en anglais, au présent.
- Un template de pull request est disponible dans le dossier `.github/PULL_REQUEST_TEMPLATE/pull_request_template.md`.
- Les pull requests doivent être assignées à un reviewer.

---

## Étapes de Configuration

### GitHub

1. **Créer un nouveau dépôt sur GitHub** : Utilisez ce template pour créer un nouveau dépôt GitHub.

2. **Clone du dépôt** : Clonez le dépôt sur votre machine locale.

### SonarQube

1. **Créer un Projet** : Allez sur votre instance SonarQube et créez un nouveau projet.

2. **Générer une Clé** : Générez une clé d'API pour votre projet.

3. **Créer un Secret GitHub** : Allez dans les paramètres de votre dépôt GitHub, puis dans `Secrets`, et créez un nouveau secret appelé `SONAR_TOKEN` avec la clé d'API générée.


### Configuration SSH

Pour cloner ce projet, assurez-vous d'avoir configuré vos clés SSH. Vous devrez avoir les fichiers suivants dans votre dossier `~/.ssh/` :

- `config`
- `id_rsa_personal`
- `id_rsa_personal.pub`
- `id_rsa_pro`
- `id_rsa_pro.pub`
- `known_hosts`

Si vous utilisez plusieurs comptes GitHub (personnel et professionnel par exemple), assurez-vous que votre fichier `~/.ssh/config` est correctement configuré.

**Cloner le projet avec SSH :**

```bash
git clone git@github.com-personal:<votre_nom_d_utilisateur>/<nom_du_projet>.git
# ou pour un compte professionnel
git clone git@github.com-pro:<votre_nom_d_utilisateur>/<nom_du_projet>.git
```

Si votre dossier `~/.ssh/` ne contient pas les fichiers listés ci-dessus, vous pouvez soit les récupérer depuis une sauvegarde, soit les générer à nouveau en suivant les actions ci-dessous.

**Générer une nouvelle clé SSH :**

 ```bash
 ssh-keygen -t rsa -b 4096 -C "<VOTRE_ADRESSE_EMAIL>"
 ```

**Ajouter la clé SSH à l'agent SSH :**

 ```bash
 eval "$(ssh-agent -s)"
 ssh-add ~/.ssh/id_rsa_personal
 ssh-add ~/.ssh/id_rsa_pro
 ```

**Ajouter la clé SSH à GitHub :**

1. Allez dans les paramètres de votre compte GitHub, puis dans `SSH and GPG keys`.
2. Cliquez sur `New SSH key`.
3. Collez la clé SSH exportée précédemment dans le champ `Key`.



### Configuration GPG

Assurez-vous d'avoir configuré votre clé GPG. Vous devrez avoir les fichiers suivants dans votre dossier `~/.gnupg/` :
- `pubring.kbx`
- `trustdb.gpg`
  Si ces fichiers ne sont pas présents, vous pouvez soit les récupérer depuis une sauvegarde, soit les générer à nouveau en suivant les actions ci-dessous.

**Importer une clé GPG existante :**

```bash
gpg --import <CHEMIN_VERS_LA_CLE>
```

**Générer une nouvelle clé GPG :**

```bash
gpg --full-generate-key
```

**Afficher les clés GPG :**

```bash
gpg --list-secret-keys --keyid-format LONG
```

**Exporter la clé GPG :**

```bash
gpg --armor --export <ID_DE_LA_CLE>
```

**Ajouter la clé GPG à Git :**

```bash
git config --global user.signingkey <ID_DE_LA_CLE>
```

**Ajouter la clé GPG à GitHub :**

1. Allez dans les paramètres de votre compte GitHub, puis dans `SSH and GPG keys`.
2. Cliquez sur `New GPG key`.
3. Collez la clé GPG exportée précédemment dans le champ `Key`.


### Configuration CI

1. **Droits en Écriture** : Assurez-vous que votre pipeline de CI a les droits en écriture sur votre dépôt. Vérifiez les paramètres à [cette URL](https://github.com/robjo82/ci-template/settings/actions).

2. **Règles de Branche pour `main`** :
    - Interdisez les `force-push`.
    - Exigez une revue de code avant de fusionner.
    - Exigez que la CI soit réussie avant de pouvoir fusionner.

---

## Personnalisation

### Dockerfile

- Le `Dockerfile` est configuré pour un environnement de base. Adaptez les étapes en fonction de votre application et de votre langage de programmation.

### Procfile

- Le `Procfile` contient des exemples commentés pour différents types d'applications. Décommentez et modifiez la ligne qui correspond à votre application.

### Fichiers de Configuration

- Modifiez les fichiers de configuration tels que `.gitignore`, `package.json`, etc., en fonction des besoins de votre projet.

---

## Scripts NPM

- `semantic-release`: Pour automatiser la gestion des versions et la publication du package. Il est configuré pour être exécuté sur la branche `main` uniquement. La configuration initiale sur les numéros de version est la suivante : `1.0.0` pour la première version, puis `1.0.1` pour les corrections de bugs, `1.1.0` pour les nouvelles fonctionnalités, et `2.0.0` pour les changements majeurs. Pour plus d'informations, consultez la documentation de [semantic-release](https://semantic-release.gitbook.io/semantic-release/).

---

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
