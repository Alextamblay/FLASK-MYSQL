from flask import Flask, render_template, request, redirect
# importar la clase de friend.py
from models.friend import Friend

app = Flask(__name__)
@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html",fr =friends)

@app.route("/newform")
def newform():
    return render_template("form.html")

# fragmento de código relevante de server.py
@app.route('/create_friend', methods=["POST"])
def create_friend():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
        }
    # Pasamos el diccionario de datos al método save de la clase Friend
    Friend.save(data)
    # # No olvides redirigir después de guardar en la base de datos
    return redirect('/')

            
if __name__ == "__main__":
    app.run(debug=True)


