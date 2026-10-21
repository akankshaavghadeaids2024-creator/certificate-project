from app import app

def test_home_page():
    app.config["TESTING"] = True
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_empty_form():
    app.config["TESTING"] = True
    client = app.test_client()
    response = client.post(
        "/generate",
        data={"name": "", "roll": ""}
    )
    assert response.status_code == 400

def test_generate_certificate():
    app.config["TESTING"] = True
    client = app.test_client()
    response = client.post(
        "/generate",
        data={"name": "Vaishnavi", "roll": "EN24107045"}
    )
    assert response.status_code == 200
