# 🏢 TechNova Partners - Analyse des causes d'attrition

Projet HR Analytics pour identifier les causes racines de démission au sein de l'ESN TechNova Partners.

## 📋 Contexte

TechNova Partners fait face à un turnover élevé. Ce projet vise à :
- Analyser les données RH pour identifier les différences entre employés partis et restés
- Construire un modèle de classification pour prédire les démissions
- Extraire les causes potentielles via l'interprétation du modèle (SHAP)

## 📁 Structure du projet

```
Projet 4/
├── pyproject.toml              # Configuration projet et dépendances
├── uv.lock                     # Verrouillage des versions
├── README.md                   # Ce fichier
├── generate_reports.py         # Script de génération des rapports
├── main.py                     # Point d'entrée principal
├── 01_exploration_donnees.ipynb # Notebook d'exploration des données
├── data/                       # Dossier des données sources
│   ├── extrait_sirh.csv        # Données SIRH (sociodémo, salaire, poste...)
│   ├── extrait_eval.csv        # Données évaluations de performance
│   └── extrait_sondage.csv     # Données sondage + variable cible
├── reports/                    # Rapports générés (auto-créé)
└── .venv/                      # Environnement virtuel (auto-créé)
```

## 🚀 Installation et lancement

### Prérequis
- Python >= 3.10
- [uv](https://docs.astral.sh/uv/) (gestionnaire de packages)

### Installation

**1. Installer uv** (si non installé)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**2. Cloner le projet**

```bash
git clone <url-du-repo>
cd "Projet 4"
```

**3. Installer les dépendances**

```bash
uv sync
```

Cette commande va :
- Créer automatiquement l'environnement virtuel `.venv/`
- Installer toutes les dépendances depuis `pyproject.toml` et `uv.lock`

**4. Activer l'environnement**

```bash
source .venv/bin/activate
```

## 💻 Lancer Jupyter

**Option A - JupyterLab (recommandé) :**
```bash
uv run jupyter lab
```

**Option B - Jupyter Notebook classique :**
```bash
uv run jupyter notebook
```

**Option C - VS Code :**
Ouvrir le fichier `.ipynb` directement dans VS Code et sélectionner le kernel `.venv`

## 📦 Dépendances principales

| Package | Usage |
|---------|-------|
| pandas, numpy | Manipulation des données |
| matplotlib, seaborn, plotly | Visualisation |
| scikit-learn, xgboost, lightgbm | Machine Learning |
| shap | Interprétation du modèle |
| ydata-profiling | Profiling automatique des données |

## 📊 Données sources

| Fichier | Description | Clé potentielle |
|---------|-------------|-----------------|
| `data/extrait_sirh.csv` | Infos employé (âge, salaire, poste, ancienneté) | `id_employee` |
| `data/extrait_eval.csv` | Évaluations (satisfaction, notes, heures sup) | `eval_number` |
| `data/extrait_sondage.csv` | Sondage + **variable cible** `a_quitte_l_entreprise` | `code_sondage` |

## 🔧 Workflow recommandé

1. **Installer** : `uv sync`
2. **Activer** : `source .venv/bin/activate`
3. **Explorer** : `python generate_reports.py` puis ouvrir les rapports HTML
4. **Analyser** : Ouvrir `01_exploration_donnees.ipynb` dans Jupyter Lab ou VS Code
5. **Modéliser** : Créer les notebooks de modélisation

## 👤 Auteur

Clément - Consultant Data Scientist

---
*Projet réalisé dans le cadre de la formation OpenClassrooms*
