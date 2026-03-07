"""
Test d'intégration pour la récupération de tous les utilisateurs
"""

def test_get_all_retourne_200(client):
    response = client.get("/api/v1/users")

    assert response.status_code == 200


def test_get_all_retourne_liste_vide_si_aucun_user(client):
    response = client.get("/api/v1/users")

    assert response.json() == []


def test_get_all_retourne_les_users_enregistres(client):
    client.post("/api/v1/register", json={
        "name": "Alice", "email": "alice@example.com", "password": "password123"
    })
    client.post("/api/v1/register", json={
        "name": "Bob", "email": "bob@example.com", "password": "password456"
    })

    response = client.get("/api/v1/users")

    assert response.status_code == 200
    assert len(response.json()) == 2
    emails = {u["email"] for u in response.json()}
    assert emails == {"alice@example.com", "bob@example.com"}


def test_get_all_ne_retourne_pas_les_passwords(client):
    client.post("/api/v1/register", json={
        "name": "Alice", "email": "alice@example.com", "password": "password123"
    })

    response = client.get("/api/v1/users")

    for user in response.json():
        assert "password" not in user
