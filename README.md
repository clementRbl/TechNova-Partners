# 🏢 TechNova Partners - Analyse des causes d'attrition

Projet HR Analytics pour identifier les facteurs de démission au sein de l'ESN TechNova Partners et construire un modèle prédictif.

## 📋 Contexte métier

TechNova Partners, une ESN de 1470 employés, fait face à un **turnover de 16%**. Ce projet vise à :

1. **Analyser** les données RH pour identifier les différences entre employés partis et restés
2. **Prédire** les démissions avec un modèle de classification (LightGBM)
3. **Interpréter** les causes via SHAP (feature importance globale et locale)

## 🎯 Résultats obtenus

| Métrique | Valeur |
|----------|--------|
| **Recall** | 59.6% (détecte 60% des départs) |
| **Precision** | 36.8% |
| **F1-Score** | 45.5% |
| **ROC-AUC** | 80.0% |

**Top 3 facteurs de départ identifiés :**
1. 🕐 Heures supplémentaires excessives
2. 💰 Salaire bas
3. 😞 Faible satisfaction globale

---

## 🚀 Installation

### Prérequis
- Python >= 3.10
- [uv](https://docs.astral.sh/uv/) (gestionnaire de packages recommandé)

### Option 1 : Avec uv (recommandé)

```bash
# Installer uv si nécessaire
curl -LsSf https://astral.sh/uv/install.sh | sh

# Cloner le projet
git clone <url-du-repo>
cd "Projet 4"

# Installer les dépendances (crée automatiquement le .venv)
uv sync
```

### Option 2 : Avec pip (alternative)

```bash
# Cloner le projet
git clone <url-du-repo>
cd "Projet 4"

# Créer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Installer les dépendances
pip install -e .
```

---

## 💻 Lancer le projet

### VS Code (recommandé)

1. Ouvrir le dossier dans VS Code
2. Ouvrir `technova_partners.ipynb`
3. Sélectionner le kernel Python `.venv`
4. Exécuter toutes les cellules

### JupyterLab

```bash
source .venv/bin/activate
jupyter lab
# Ouvrir technova_partners.ipynb
```

---

## 📂 Structure du projet

```
Projet 4/
├── technova_partners.ipynb   # 📓 Notebook principal (analyse complète)
├── pyproject.toml            # 📦 Dépendances du projet
├── README.md                 # 📖 Ce fichier
├── data/
│   ├── extrait_sirh.csv      # Données RH (âge, salaire, ancienneté)
│   ├── extrait_eval.csv      # Évaluations (satisfaction, heures sup)
│   └── extrait_sondage.csv   # Sondage + variable cible
└── .venv/                    # Environnement virtuel (non versionné)
```

## 📊 Données sources

| Fichier | Description | Observations |
|---------|-------------|--------------|
| `extrait_sirh.csv` | Infos employé (âge, salaire, poste) | 1470 lignes |
| `extrait_eval.csv` | Évaluations et heures supplémentaires | 1470 lignes |
| `extrait_sondage.csv` | Satisfaction + **`a_quitte_l_entreprise`** | 1470 lignes |

## 📦 Dépendances principales

| Package | Usage |
|---------|-------|
| `pandas`, `numpy` | Manipulation des données |
| `matplotlib`, `seaborn` | Visualisation |
| `scikit-learn` | Preprocessing, métriques, GridSearchCV |
| `lightgbm` | Modèle final (Gradient Boosting) |
| `imbalanced-learn` | Gestion du déséquilibre (SMOTE, undersampling) |
| `shap` | Interprétation du modèle |

---

## 📓 Contenu du notebook

Le notebook `technova_partners.ipynb` contient **5 parties** :

| Partie | Contenu |
|--------|---------|
| **1. EDA** | Chargement, nettoyage, analyse univariée/bivariée |
| **2. Feature Engineering** | Création de variables, encoding, fusion |
| **3. Modélisation Baseline** | Dummy, Logistic Regression, Random Forest |
| **4. Gestion Déséquilibre** | class_weight, SMOTE, undersampling, calibration |
| **5. Fine-tuning & SHAP** | GridSearchCV, LightGBM, interprétation SHAP |

---

## 👤 Auteur

**Clément** - Data Scientist

---

*Projet 4 - Formation Data Scientist OpenClassrooms*
