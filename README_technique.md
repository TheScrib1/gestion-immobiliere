<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Liste des techniciens</title>
</head>
<body>
    <h1>Techniciens disponibles</h1>

    <form method="get">
        <label for="specialite">Filtrer par spécialité :</label>
        <input type="text" id="specialite" name="specialite" value="{{ request.GET.specialite }}">
        <button type="submit">Filtrer</button>
    </form>

    <ul>
        {% for technicien in techniciens %}
            <li>{{ technicien.nom }} – {{ technicien.specialite }} – {{ technicien.telephone }}</li>
        {% empty %}
            <li>Aucun technicien trouvé.</li>
        {% endfor %}
    </ul>
</body>
</html>
