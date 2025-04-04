# Cahier des charges – Application de gestion immobilière Yesoda

## Objectif

Développer une application web destinée à un administrateur unique pour la gestion complète de biens immobiliers, locataires, propriétaires, techniciens et interventions, avec des extensions futures pour l’IA et le multi-utilisateur.

---

## Fonctionnalités principales

### 1. Gestion des profils
- **Propriétaires** : nom, téléphone, e-mail.
- **Locataires** : nom, téléphone, e-mail, date d’entrée, date de sortie, remarques.
- **Biens** : adresse, surface, loyer, propriétaire associé, locataire associé.
- **Documents** : contrat PDF, états des lieux (entrée/sortie), compteurs eau/électricité/gaz.

### 2. Gestion documentaire
- Téléversement de fichiers (PDF) pour les contrats.
- Classement et affichage des documents associés à chaque bien.
- Connecté au système de notification pour rappeler les échéances.

### 3. Notifications intelligentes
- Envoi automatique d’un **bilan mensuel** le 1er du mois pour chaque locataire.
- Alertes sur documents manquants ou état des lieux non rempli.

### 4. Fidélisation & notation
- Système de **points de fidélité** pour les bons locataires.
- Remarques qualitatives pour repérer les locataires exemplaires ou à risque.

### 5. Carnet d’adresses techniques
- Base de données des **techniciens** (plombiers, électriciens, etc.) avec spécialité, téléphone.
- **Évaluation** des techniciens par les locataires après intervention.

### 6. Interventions
- Planification d’interventions avec :
  - Date, durée estimée, marge de sécurité de 1h30.
  - Association bien / technicien / description.
- Affichage historique et évaluation post-intervention.

### 7. Bloc-notes "Mission du jour"
- Notes quotidiennes horodatées.
- Suivi budgétaire simple (revenus vs dépenses journalières).
- Archivage automatique.

---

## Extensions prévues

### Intelligence Artificielle intégrée
- Génération automatique de **contrats personnalisés** à partir de modèles.
- Analyse automatique des paiements en retard.
- Générateur de fiches de synthèse par locataire ou bien.
- Agent LLM pour assister dans la gestion et prise de décision.

### Interface personnalisable
- Mode sombre.
- Possibilité de créer des vues personnalisées ou widgets.
- Tableau de bord modulable.

### Multi-utilisateur
- Application mono-utilisateur pour l’instant.
- Extension future pour entreprise avec rôles et droits (admin, assistant, technicien…).

---

## Parcours utilisateurs (extensions)
- Création de comptes en ligne (pour les locataires ou partenaires).
- Système de tickets / demandes via l’interface.
- Signature électronique à distance.

---

## Contraintes
- Application développée en **Django**.
- Déploiement en local dans un premier temps.
- Base de données : SQLite en développement, possibilité de migrer vers PostgreSQL.
- Pas de facturation automatique dans la V1.

---

## Rappel
> L’objectif est de donner à un gérant une **vision claire** de ses biens et de sa relation avec ses locataires et prestataires, de façon simple, rapide et personnalisable.
