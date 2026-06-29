# Classification Report
> Rapport de classification des documents pour le pipeline RAG — ERP AI Assistant
> Généré le : 2026-06-28

## Résumé

| Catégorie | Nombre de fichiers |
|---|---|
| accounting | 15 |
| taxation | 4 |
| regulations | 6 |
| erp | 2 |
| **Total** | **27** |

---

## Détail par document

| # | Nom original | Nouveau nom | Dossier destination | Raison de classification |
|---|---|---|---|---|
| 1 | `24-4-financieres.pdf` | `mathematiques_financieres.pdf` | `accounting` | Contenu relatif aux mathématiques financières (intérêts, annuités, actualisation) |
| 2 | `9782297092005.pdf` | `exercices_comptabilite_generale.pdf` | `accounting` | Recueil d'exercices et corrigés de comptabilité générale |
| 3 | `COURS COMPTABILITE GENERALE S2.pdf` | `cours_comptabilite_generale_s2.pdf` | `accounting` | Cours complet de comptabilité générale — Semestre 2 |
| 4 | `COURS-DE-MATHS-FINANCIERES-Mme-HARECHEB-2020.pdf` | `cours_maths_financieres_harecheb.pdf` | `accounting` | Cours de mathématiques financières (Mme Harecheb, 2020) |
| 5 | `Chapitre-I.pdf` | `cours_comptabilite_generale_1.pdf` | `accounting` | Premier chapitre d'un cours de comptabilité générale |
| 6 | `Cours Math Fin S2 Pr. NOKAIRI.pdf` | `cours_maths_financieres_nokairi.pdf` | `accounting` | Cours de mathématiques financières (Pr. Nokairi, S2) |
| 7 | `LES BASES DE LA COMPTABILITÉ.pdf` | `bases_comptabilite.pdf` | `accounting` | Introduction aux bases de la comptabilité (définitions, principes fondamentaux) |
| 8 | `Nomenclature-et-Fonctionnement-des-comptes.pdf` | `nomenclature_comptes.pdf` | `accounting` | Nomenclature et fonctionnement du plan comptable (classes de comptes, journaux) |
| 9 | `SUPPORT PEDAGOGIQUE.pdf` | `support_pedagogique_comptabilite.pdf` | `accounting` | Support pédagogique de comptabilité financière (états financiers, bilan, résultat) |
| 10 | `comptabilite_generale.pdf` | `comptabilite_generale.pdf` | `accounting` | Manuel de comptabilité générale (écritures, grand livre, balance) |
| 11 | `comptabilité_smaoui1.pdf` | `concepts_comptables_smaoui.pdf` | `accounting` | Cours de concepts fondamentaux de comptabilité (auteur Smaoui) |
| 12 | `comptabilité_smaoui2.pdf` | `comptabilite_smaoui_2.pdf` | `accounting` | Suite du cours de comptabilité générale (auteur Smaoui) |
| 13 | `comptabilité_smaoui3.pdf` | `comptabilite_smaoui_3.pdf` | `accounting` | Continuation du cours de comptabilité générale (auteur Smaoui) |
| 14 | `comptagenerale.pdf` | `compta_generale.pdf` | `accounting` | Cours de comptabilité générale (plan comptable, écritures, clôture) |
| 15 | `hasbnclic747.pdf` | `cours_comptabilite_ohada.pdf` | `accounting` | Cours de comptabilité selon le référentiel OHADA |
| 16 | `fiscalité_smaoui4.pdf` | `fiscalite_smaoui_4.pdf` | `taxation` | Cours de fiscalité tunisienne — partie 4 (auteur Smaoui) |
| 17 | `samoui_fiscalité.pdf` | `fiscalite_smaoui_1.pdf` | `taxation` | Cours de fiscalité tunisienne — partie 1 (auteur Smaoui) |
| 18 | `samoui_fiscalité2.pdf` | `fiscalite_smaoui_2.pdf` | `taxation` | Cours de fiscalité tunisienne — partie 2 (TVA, impôts, taxes) |
| 19 | `smaoui_fiscalité3.pdf` | `fiscalite_smaoui_3.pdf` | `taxation` | Cours de fiscalité tunisienne — partie 3 (IS, IR, procédures fiscales) |
| 20 | `Systeme-Comptable-Tunisien.pdf` | `systeme_comptable_tunisien.pdf` | `regulations` | Système Comptable des Entreprises tunisien (SCE) — normes et réglementation officielle |
| 21 | `code_compta_fr.pdf` | `code_comptabilite.pdf` | `regulations` | Code de la comptabilité — texte réglementaire et juridique |
| 22 | `comptabilité_smaoui.pdf` | `normes_comptables_smaoui.pdf` | `regulations` | Introduction aux normes comptables tunisiennes et internationales |
| 23 | `ias-1-prc3a9sentation-des-c3a9tats-financiers.pdf` | `ias_1_etats_financiers.pdf` | `regulations` | Norme IAS 1 — Présentation des états financiers (IFRS officiel) |
| 24 | `nc01.pdf` | `norme_comptable_01.pdf` | `regulations` | Norme Comptable Tunisienne NC 01 — cadre conceptuel officiel |
| 25 | `normes_comptables_internationales_ias_ifrs.pdf` | `normes_ias_ifrs.pdf` | `regulations` | Recueil complet des normes IAS/IFRS internationales |
| 26 | `erp.pdf` | `introduction_erp.pdf` | `erp` | Document d'introduction aux systèmes ERP (concepts, modules, architecture) |
| 27 | `odoo_erp.pdf` | `documentation_odoo_erp.pdf` | `erp` | Documentation fonctionnelle Odoo ERP (modules comptabilité, ventes, achats) |

---

## Fichiers ignorés

| Fichier | Raison |
|---|---|
| `Unconfirmed 212113.crdownload` | Téléchargement incomplet (fichier corrompu) — supprimé |

---

## Structure finale du dossier `data/raw/`

```
data/
└── raw/
    ├── accounting/     (15 fichiers — comptabilité générale, cours, exercices, maths financières)
    ├── taxation/       (4 fichiers  — fiscalité tunisienne, TVA, impôts)
    ├── regulations/    (6 fichiers  — normes IAS/IFRS, SCE tunisien, code comptable)
    └── erp/            (2 fichiers  — documentation Odoo, introduction ERP)
```