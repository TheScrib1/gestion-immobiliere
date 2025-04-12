# 🤖 IA_PLAN.md – Coordination Multi-IA pour YESODA Real Estate

## Objectif

Organiser une collaboration entre plusieurs IA (ChatGPT, Claude, Grok) pour accélérer le développement de l'application de gestion immobilière "YESODA".

---

## 🧠 Rôle des IA

### 1. ChatGPT (Toi)
- **Rôle principal :** Architecte technique / Planificateur.
- **Responsable de :**
  - Structuration du code.
  - Instructions aux autres IA.
  - Documentation technique.
  - Vérification finale.

---

### 2. Claude (Anthropic)
- **Rôle :** Développeur fonctionnel & logique métier.
- **Tâches proposées :**
  - Générer les vues Django (CBV/Fonctionnelles).
  - Gérer les formulaires et la logique utilisateur.
  - Développer les systèmes de points, évaluations, rappels automatiques.

---

### 3. Grok (xAI)
- **Rôle :** Intégrateur IA & Automatisation.
- **Tâches proposées :**
  - Intégration d’un agent LLM dans l’app.
  - Génération automatique de contrats personnalisés.
  - Analyse des retards de paiement et suggestions.
  - Assistance quotidienne (module assistant intelligent).

---

## 🔁 Organisation du travail

- ChatGPT rédige les **instructions détaillées** pour Claude et Grok.
- Claude exécute les fonctionnalités classiques.
- Grok se concentre sur les modules IA / NLP / automations.
- Toutes les IA documentent leurs contributions (README, docstrings, commentaires).

---

## 🔄 Synchronisation

- Coordination via `README.md` et `IA_PLAN.md`.
- Dossier `docs/` pour la documentation.
- Tâches distribuées dans des fichiers dédiés si nécessaire (`tasks_claude.md`, `tasks_grok.md`...).

---

## ✅ Objectif final

Une application Django modulaire, documentée, intelligente, extensible avec des agents IA spécialisés.
