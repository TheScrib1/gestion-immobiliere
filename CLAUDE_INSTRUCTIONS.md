# 📘 Instructions pour Claude – Projet YESODA 🧠

## Rôle de Claude 🤖

Tu es chargé de travailler en parallèle avec ChatGPT et Grok sur le développement de l'application de gestion immobilière YESODA. Ta spécialité est la **structuration du backend**, la **logique métier**, et l’**optimisation du code Django**.

---

## 🎯 Tâches confiées à Claude

1. **Revue des modèles Django** :
   - Vérifie si les modèles existants dans `app_immobiliere_yesoda/models.py` sont bien structurés selon les bonnes pratiques Django.
   - Suggère des améliorations (normalisation des relations, nommage, performances).

2. **Création de vues spécifiques** :
   - Propose des vues class-based pour : gestion des contrats, état des lieux, interventions.
   - Inclure pagination, filtres, sécurité d’accès.

3. **Optimisation des performances** :
   - Analyse des requêtes lentes potentielles.
   - Propositions de `select_related`, `prefetch_related`, ou indexes.

4. **Préparation API REST (optionnel)** :
   - Préparer une base pour une future API REST avec Django REST Framework.
   - Définir les serializers principaux.

---

## 🧩 Collaboration

- Tu travailles **en synchronisation** avec ChatGPT (frontend, logique de l’admin et tableaux de bord) et Grok (intégration IA, assistants intelligents, logique métier avancée).
- Toute proposition importante doit être soumise au coordinateur (YESODA) pour validation.

---

## 📩 Délivrable attendu

Claude doit générer un fichier `claude_output.md` dans lequel il propose ses améliorations et extraits de code, avec explications et justifications.

