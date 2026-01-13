#!/usr/bin/env python3
"""
Script de génération de rapports d'exploration avec ydata-profiling
TechNova Partners - Analyse d'attrition
"""

from pathlib import Path

import pandas as pd
from ydata_profiling import ProfileReport

print("📊 Génération des rapports d'exploration des données...")
print("=" * 60)

# Créer le dossier de sortie
output_dir = Path("reports")
output_dir.mkdir(exist_ok=True)

# 1. RAPPORTS INDIVIDUELS
print("\n📁 Génération des rapports individuels...")

# SIRH
print("\n  → Fichier SIRH...")
df_sirh = pd.read_csv("data/extrait_sirh.csv")
profile_sirh = ProfileReport(
    df_sirh, title="Rapport d'Exploration - SIRH", explorative=True
)
profile_sirh.to_file(output_dir / "rapport_sirh.html")
print(
    f"    ✅ Rapport SIRH généré: {df_sirh.shape[0]} lignes, {df_sirh.shape[1]} colonnes"
)

# Évaluations
print("\n  → Fichier Évaluations...")
df_eval = pd.read_csv("data/extrait_eval.csv")
profile_eval = ProfileReport(
    df_eval, title="Rapport d'Exploration - Évaluations", explorative=True
)
profile_eval.to_file(output_dir / "rapport_evaluations.html")
print(
    f"    ✅ Rapport Évaluations généré: {df_eval.shape[0]} lignes, {df_eval.shape[1]} colonnes"
)

# Sondage
print("\n  → Fichier Sondage...")
df_sondage = pd.read_csv("data/extrait_sondage.csv")
profile_sondage = ProfileReport(
    df_sondage, title="Rapport d'Exploration - Sondage", explorative=True
)
profile_sondage.to_file(output_dir / "rapport_sondage.html")
print(
    f"    ✅ Rapport Sondage généré: {df_sondage.shape[0]} lignes, {df_sondage.shape[1]} colonnes"
)

# 2. RAPPORT DU DATASET FUSIONNÉ
print("\n" + "=" * 60)
print("🔗 Fusion des données et génération du rapport complet...")

# Stratégie de fusion (à adapter selon vos clés de jointure)
# Option 1: Si les fichiers ont le même ordre et le même nombre de lignes
if len(df_sirh) == len(df_eval) == len(df_sondage):
    print("\n  → Les 3 fichiers ont le même nombre de lignes, fusion par index...")
    df_merged = pd.concat([df_sirh, df_eval, df_sondage], axis=1)

    # Supprimer les colonnes dupliquées si nécessaire
    df_merged = df_merged.loc[:, ~df_merged.columns.duplicated()]

    print(
        f"    ✅ Dataset fusionné: {df_merged.shape[0]} lignes, {df_merged.shape[1]} colonnes"
    )

    # Générer le rapport du dataset fusionné
    print("\n  → Génération du rapport du dataset complet...")
    profile_merged = ProfileReport(
        df_merged,
        title="Rapport d'Exploration - Dataset Complet (Fusionné)",
        explorative=True,
    )
    profile_merged.to_file(output_dir / "rapport_dataset_complet.html")
    print("    ✅ Rapport du dataset complet généré")
else:
    print("\n  ⚠️  Les fichiers ont des tailles différentes.")
    print(f"     SIRH: {len(df_sirh)} lignes")
    print(f"     Évaluations: {len(df_eval)} lignes")
    print(f"     Sondage: {len(df_sondage)} lignes")
    print("\n  → Vous devrez identifier les clés de jointure appropriées")
    print("     avant de créer le rapport du dataset fusionné.")

# Résumé
print("\n" + "=" * 60)
print("✅ Génération des rapports terminée !")
print(f"\n📂 Les rapports sont disponibles dans le dossier: {output_dir.absolute()}")
print("\nRapports générés:")
print("  - rapport_sirh.html")
print("  - rapport_evaluations.html")
print("  - rapport_sondage.html")
if len(df_sirh) == len(df_eval) == len(df_sondage):
    print("  - rapport_dataset_complet.html")
print("\nOuvrez ces fichiers HTML dans votre navigateur pour explorer les données.")
