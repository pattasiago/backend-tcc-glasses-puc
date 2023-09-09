from src.app import app


# create a test for the /api route
def test_api():
    # create a test client for the app
    client = app.test_client()

    # send data as POST form to endpoint
    response = client.get("/api", data={"name": "John Doe"})

    # check the status code of the response
    assert response.status_code == 200
