from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route("/")
def index():
    edades = [20, 21, 22, 25, 27, 29, 31, 33, 35, 40]
    plt.hist(edades, bins=10)
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.title("Histograma de Edades de Empleados")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plot = base64.b64encode(buf.read()).decode("utf-8")
    return render_template("index.html", plot=plot)

if __name__ == "__main__":
    app.run()
