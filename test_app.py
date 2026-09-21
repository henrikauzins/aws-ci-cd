from app import app
 
def test_index():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert r.get_json()["message"] == "hello from python"
 
def test_healthz():
    assert app.test_client().get("/healthz").status_code == 200

