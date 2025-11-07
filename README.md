# 📇 CRM - Customer Relationship Management

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.0+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

> Application de gestion de contacts (Customer Relationship Management) construite avec Django. Gérez facilement vos contacts professionnels avec un système CRUD complet.

## 🎯 Aperçu

Ce projet est un **système de gestion de contacts** (CRM simplifié) qui permet d'ajouter, modifier, consulter et supprimer des contacts via une interface web intuitive. Les données sont stockées dans un fichier JSON pour une persistence simple et efficace.

**Cas d'usage :** Idéal pour les freelances, petites entreprises ou entrepreneurs qui ont besoin d'un carnet d'adresses digital simple et fonctionnel.

---

## ✨ Fonctionnalités

- ✅ **Ajouter un contact** - Formulaire complet avec validation
- ✅ **Liste des contacts** - Affichage de tous les contacts enregistrés
- ✅ **Détails du contact** - Vue détaillée de chaque contact
- ✅ **Modifier un contact** - Mise à jour des informations existantes
- ✅ **Supprimer un contact** - Suppression avec confirmation
- ✅ **Sauvegarde JSON** - Persistence des données dans `db.json`
- ✅ **Interface responsive** - Design adapté mobile et desktop
- ✅ **Validation des données** - Vérification des champs (email, téléphone, etc.)

---

## 🛠️ Technologies utilisées

**Backend**
- ![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white) **Python 3.8+**
- ![Django](https://img.shields.io/badge/Django-4.0+-092E20?logo=django&logoColor=white) **Django 4.0+**

**Frontend**
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) **HTML5**
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white) **CSS3**
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-7952B3?logo=bootstrap&logoColor=white) **Bootstrap 5**

**Stockage**
- 📄 **JSON** - Fichier `db.json` pour la persistence

---

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone https://github.com/EbroVital/crm-django.git
cd crm-django
```

2. **Créer un environnement virtuel**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Appliquer les migrations**
```bash
python manage.py migrate
```

5. **Lancer le serveur de développement**
```bash
python manage.py runserver
```

6. **Accéder à l'application**
```
Ouvrir le navigateur à : http://127.0.0.1:8000
```

---

## 💻 Utilisation

### Ajouter un contact

1. Cliquer sur "Ajouter un contact" ou "Nouveau contact"
2. Remplir le formulaire avec les informations :
   - Nom complet
   - Email
   - Téléphone
   - Adresse (optionnel)
3. Cliquer sur "Enregistrer"

### Supprimer un contact
2. Cliquer sur "Supprimer"

---

## 🔮 Améliorations futures

- [ ] Authentification utilisateur (login/logout)
- [ ] Catégories de contacts (Clients, Prospects, Partenaires)
- [ ] Export des contacts (CSV, PDF)
- [ ] Import de contacts via fichier CSV
- [ ] Tags personnalisables
- [ ] Historique des interactions
- [ ] Intégration email (envoi direct depuis l'app)
- [ ] API REST pour intégration mobile
- [ ] Base de données PostgreSQL/MySQL (au lieu de JSON)
- [ ] Dark mode
- [ ] Notifications et rappels

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet :

1. Fork le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

---

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---
⭐️ **Si ce projet vous a été utile, n'hésitez pas à mettre une étoile !** ⭐️

---

## 📝 Notes de développement

**Objectifs d'apprentissage atteints :**
- ✅ Maîtrise du MVT (Model-View-Template) de Django
- ✅ CRUD complet avec Django
- ✅ Formulaires Django avec validation
- ✅ Gestion de fichiers JSON en Python
- ✅ Templates Django et héritage
- ✅ Routing et URLs Django
- ✅ Design responsive avec Bootstrap

**Difficultés rencontrées et solutions :**
- Persistence des données → Solution : Sérialisation JSON
- Validation des formulaires → Solution: Django Forms
- Design responsive → Solution: Bootstrap Grid System
