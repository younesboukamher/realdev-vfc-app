# Configurer un domaine personnalisé pour l'app RealDev VFC

## Option recommandée : app.futsal-realdev.com

### Étape 1 — Chez votre registrar DNS (ex: OVH, Combell, Namecheap)
Ajouter un enregistrement CNAME :

```
Type  : CNAME
Nom   : app
Valeur: younesboukamher.github.io
TTL   : 3600
```

### Étape 2 — Dans GitHub (Settings → Pages)
1. Aller sur https://github.com/younesboukamher/realdev-vfc-app/settings/pages
2. Dans "Custom domain" : taper `app.futsal-realdev.com`
3. Cocher "Enforce HTTPS"
4. Attendre 10-30 min pour la propagation DNS

### Étape 3 — Fichier CNAME (déjà créé)
Le fichier `CNAME` à la racine du repo contient le domaine.

### Résultat
L'app sera accessible sur :
  https://app.futsal-realdev.com

Et la page d'installation sur :
  https://app.futsal-realdev.com/install.html

---

## Alternative gratuite sans domaine
Continuer avec l'URL GitHub Pages actuelle :
  https://younesboukamher.github.io/realdev-vfc-app/
