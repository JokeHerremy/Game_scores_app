from website import create_app, conn_database

app = create_app()
api = conn_database()

if __name__ == '__main__':
    app.run(debug=True)