from microservice_template.app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=10000)
