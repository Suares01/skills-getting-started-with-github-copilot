from src.app import activities


def test_unregister_removes_participant(client):
    email = "michael@mergington.edu"

    response = client.post("/activities/Chess Club/unregister", params={"email": email})

    assert response.status_code == 200
    assert response.json() == {
        "message": f"Unregistered {email} from Chess Club"
    }
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_returns_404_for_missing_activity(client):
    response = client.post("/activities/Unknown Club/unregister", params={"email": "student@mergington.edu"})

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_rejects_non_participant(client):
    response = client.post("/activities/Chess Club/unregister", params={"email": "student@mergington.edu"})

    assert response.status_code == 400
    assert response.json() == {"detail": "Student not signed up for this activity"}