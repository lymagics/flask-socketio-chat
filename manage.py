from app import create_app, sio 

app = create_app(debug=True)

if __name__ == "__main__":
    sio.run(app)
    