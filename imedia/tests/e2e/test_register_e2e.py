"""
Test d'intégration pour l'enregistrement d'un utilisateur
"""


def test_register_succes_retourne_201(client):
    response = client.post("/api/v1/register", json={
        "name": "Alice",
        "email": "alice@example.com",
        "password": "password123"
    })

    assert response.status_code == 201


def test_register_succes_retourne_les_bonnes_donnees(client):
    response = client.post("/api/v1/register", json={
        "name": "Alice",
        "email": "alice@example.com",
        "password": "password123"
    })

    body = response.json()
    assert body["name"] == "Alice"
    assert body["email"] == "alice@example.com"
    assert "id" in body
    assert "created_at" in body
    assert "updated_at" in body


def test_register_ne_retourne_pas_le_password(client):
    response = client.post("/api/v1/register", json={
        "name": "Alice",
        "email": "alice@example.com",
        "password": "password123"
    })

    assert "password" not in response.json()


def test_register_email_duplique_retourne_400(client):
    payload = {"name": "Alice", "email": "alice@example.com", "password": "password123"}
    client.post("/api/v1/register", json=payload)

    response = client.post("/api/v1/register", json={
        "name": "Bob",
        "email": "alice@example.com",  # même email
        "password": "password456"
    })

    assert response.status_code == 400
    assert "email est déjà utilisé" in response.json()["detail"]


def test_register_nom_duplique_retourne_400(client):
    client.post("/api/v1/register", json={
        "name": "Alice", "email": "alice@example.com", "password": "password123"
    })

    response = client.post("/api/v1/register", json={
        "name": "Alice",             # même nom
        "email": "autre@example.com",
        "password": "password456"
    })

    assert response.status_code == 400
    assert "nom est déjà utilisé" in response.json()["detail"]


def test_register_champs_manquants_retourne_422(client):
    response = client.post("/api/v1/register", json={
        "name": "Alice"
        # email et password manquants
    })

    assert response.status_code == 422


def test_register_email_invalide_retourne_422(client):
    response = client.post("/api/v1/register", json={
        "name": "Alice",
        "email": "pas-un-email",
        "password": "password123"
    })

    assert response.status_code == 422  # rejeté par Pydantic (EmailStr)


def test_register_password_trop_court_retourne_422(client):
    response = client.post("/api/v1/register", json={
        "name": "Alice",
        "email": "alice@example.com",
        "password": "abc"  # min_length=8
    })

    assert response.status_code == 422
