# Flask Task API

Une petite API Flask pour gérer une liste de tâches (todo), connectée à une base PostgreSQL.

## 🔧 Prérequis

- Python 3.10+
- PostgreSQL (local ou conteneurisé)
- `pip` pour installer les dépendances

## 🚀 Installation

### ⚙️ Sans Docker

1. Cloner le dépôt ou décompresser l'archive :
```bash
cd app
pip install -r requirements.txt
```

2. Créer la base PostgreSQL :
```bash
createdb todo
```

3. Lancer le serveur :
```bash
python app.py
```

### 🐳 Avec Docker

> (nécessite un `Dockerfile` et `docker-compose.yml`, non inclus ici)

```bash
docker-compose up --build
```

## 📫 Endpoints disponibles

| Méthode | URL                  | Description                         |
|---------|----------------------|-------------------------------------|
| GET     | /tasks               | Liste toutes les tâches             |
| POST    | /tasks               | Ajoute une nouvelle tâche           |
| PUT     | /tasks/<id>/done     | Marque une tâche comme terminée     |

## 📁 Structure du projet

```
.
├── app/
│   ├── app.py           # L’API Flask
│   ├── db.py            # Initialisation SQLAlchemy
│   ├── models.py        # Modèle Task
│   └── requirements.txt # Dépendances Python
└── README.md
```

## ✍️ Auteur

Projet généré pour apprentissage Docker et Flask.
