**Note: A French version of this README is available right after this section.**

# Othello AI

Pygame interface which allows you to play the Othello game with friends or against an AI.

Our goal was to apply the theoretical knowledge learned on these different so-called artificial intelligence algorithms
such as min max or alpha beta, and analyze them statistically to understand which is the best and why?

## Table of Contents

- [Prerequisites](#prerequisites)
- [Characteristics](#characteristics)
  - [Installation](#installation)
  - [Game Modes](#game-modes)
  - [AI Algorithms](#ai-algorithms)
- [Best Practices](#best-practices)
  - [Best Practices on Branching](#best-practices-on-branching)
  - [Best Practices on Commits](#best-practices-on-commits)
  - [Best Practices on Pull Requests](#best-practices-on-pull-requests)
- [Contributing](#contributing)
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
- [Python 3.X](https://www.python.org/)
- [Pygame](https://www.pygame.org/news)

---

## Characteristics

- Using Minimax Algorithm for decision-making
- Optimizing with Alpha-Beta pruning
- Using memory with a transpose table to store evaluations of platter positions
- Time management with a timeout system
- Evaluation of tabletop positions via four personalized evaluation functions

### Installation

```bash
git clone https://github.com/robjo82/othello-ai.git
cd othello-ai
pip install -r requirements.txt
python src/main.py
```

### Game Modes

- **Player vs Player** : Play against a friend on the same computer.
- **Player vs AI** : Play against an AI.
- **AI vs AI** : Watch two AIs play against each other.

### AI Algorithms

**Minimax**:

Minimax is a decision search algorithm for two-player games (like chess, checkers, etc.). The algorithm evaluates
possible moves and chooses the best move, assuming that the opponent will also play optimally. Minimax uses a game tree
to represent possible moves and a depth system to limit the search.

In the Minimax algorithm, two types of nodes are evaluated:

“Maximizing” nodes: The AI ​​searches for the move with the maximum value.
“Minimizing” nodes: The AI ​​anticipates that the opponent will choose the move with the minimum value.

**Alpha-Beta Pruning**:

Alpha-Beta pruning is an optimization of the Minimax algorithm that reduces the number of nodes evaluated in the search
tree. The idea is to maintain two values, Alpha and Beta, which respectively represent the best option for the player so
far and the best option for the opponent. When traversing the tree, branches are "cut" or ignored as soon as it is
obvious that they will not produce a better decision than the one already found.

Alpha-Beta pruning allows you to search deeper in the game tree with the same calculation time, or reduce the time
needed for a given depth.

Both algorithms are often used in game programs to help AI decide which moves to make. They are particularly effective
when the game has a limited set of possible moves and clearly defined rules for winning or losing.

## Best Practices

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

## Contributing

Contributions are welcome! Please first create a branch with the name of the feature you want to add, then create a pull
request to merge your branch into the `develop` branch.

---

## License
This project is under the MIT license - see the [LICENSE](LICENSE) file for more details.
    
---

# 

# 

# Othello AI

Interface Pygame qui vous permet de jouer au jeu Othello avec des amis ou contre une IA.

Notre objectif était d'appliquer les connaissances théoriques apprises sur ces différents algorithmes dits d'
intelligence artificielle, comme Minimax ou l'élagage Alpha Beta, et de les analyser statistiquement pour comprendre
lequel est le meilleur et pourquoi ?

## Sommaire

- [Prérequis](#prérequis)
- [Caractéristiques](#caractéristiques)
  - [Installation](#installation)
  - [Modes de Jeu](#modes-de-jeu)
  - [Algorithmes d'IA](#algorithmes-dia)
- [Bonnes Pratiques](#bonnes-pratiques)
  - [Bonnes Pratiques sur les Branches](#bonnes-pratiques-sur-les-branches)
  - [Bonnes Pratiques sur les Commits](#bonnes-pratiques-sur-les-commits)
  - [Bonnes Pratiques sur les Pull Requests](#bonnes-pratiques-sur-les-pull-requests)
- [Contribuer](#contribuer)
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
- [Python 3.X](https://www.python.org/)
- [Pygame](https://www.pygame.org/news)

---

## Caractéristiques

### Installation

```bash
git clone
cd othello-ai
pip install -r requirements.txt
python src/main.py
```

### Modes de Jeu

- **Joueur contre Joueur** : Jouez contre un ami sur le même ordinateur.
- **Joueur contre IA** : Jouez contre une IA.
- **IA contre IA** : Regardez deux IA jouer l'une contre l'autre.

### Algorithmes d'IA

**Minimax** :

Minimax est un algorithme de recherche de décision pour les jeux à deux joueurs (comme les échecs, les dames, etc.).
L'algorithme évalue les coups possibles et choisit le meilleur coup, en supposant que l'adversaire jouera également de
manière optimale. Minimax utilise un arbre de jeu pour représenter les coups possibles et un système de profondeur pour
limiter la recherche.

Dans l'algorithme Minimax, deux types de nœuds sont évalués :

Nœuds "Maximisants" : L'IA recherche le coup ayant la valeur maximale.

Nœuds "Minimisants" : L'IA anticipe que l'adversaire choisira le coup ayant la valeur minimale.

**Élagage Alpha-Beta** :

L'élagage Alpha-Beta est une optimisation de l'algorithme Minimax qui réduit le nombre de nœuds évalués dans l'arbre de
recherche. L'idée est de maintenir deux valeurs, Alpha et Beta, qui représentent respectivement la meilleure option pour
le joueur jusqu'à présent et la meilleure option pour l'adversaire. Lors du parcours de l'arbre, les branches sont "
coupées" ou ignorées dès qu'il est évident qu'elles ne produiront pas une meilleure décision que celle déjà trouvée.

L'élagage Alpha-Beta permet de rechercher plus en profondeur dans l'arbre de jeu avec le même temps de calcul, ou de
réduire le temps nécessaire pour une profondeur donnée.

Les deux algorithmes sont souvent utilisés dans les programmes de jeu pour aider l'IA à décider quels coups faire. Ils
sont particulièrement efficaces lorsque le jeu a un ensemble limité de coups possibles et des règles clairement définies
pour gagner ou perdre.

---

## Bonnes Pratiques

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

## Contribuer

Les contributions sont les bienvenues ! Veuillez d'abord créer une branche avec le nom de la fonctionnalité que vous
souhaitez ajouter, puis créer une pull request pour fusionner votre branche dans la branche `develop`.

---

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
