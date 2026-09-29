from flask import Flask, render_template, request

# creamos la aplicación 
app = Flask(__name__)

# menu 
@app.route('/')
def inicio():
    return render_template('index.html')

# opcion 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    # si el usuario envia el formulario
    if request.method == 'POST':
        # obtenemos los datos que escribeusuario
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        
        # precio del tarro
        precio_tarro = 9000
        # total sin descuento
        total_sin_descuento = tarros * precio_tarro
        
        # reglas de descuento
        # 18 y 30 años (inclusive): 15% de descuento
        # Mayores de 30 años: 25% de descuento
        # Menores de 18 años: 0% de descuento
        if 18 <= edad <= 30:
            porcentaje_descuento = 0.15
        elif edad > 30:
            porcentaje_descuento = 0.25
        else:
            porcentaje_descuento = 0.0
            
        # calculamos el descuento y el total 
        monto_descuento = int(total_sin_descuento * porcentaje_descuento)
        total_a_pagar = total_sin_descuento - monto_descuento
        
        # devolvemos los resultados 
        return render_template('ejercicio1.html', 
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               monto_descuento=monto_descuento,
                               total_a_pagar=total_a_pagar,
                               calculado=True)
                               
    # si el usuario solo entra a ver la página
    return render_template('ejercicio1.html', calculado=False)

# opcion 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    # el usuario envia form
    if request.method == 'POST':
        # usuario y contraseña
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        
        # usuario permitido
        if usuario == 'juan' and contrasena == 'admin':
            mensaje = "Bienvenido Administrador juan"
            es_exito = True
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = "Bienvenido Usuario pepe"
            es_exito = True
        else:
            mensaje = "Usuario o contraseña incorrectos"
            es_exito = False
            
        # enviar mensaje
        return render_template('ejercicio2.html', mensaje=mensaje, es_exito=es_exito)
        
    # si usuario entra a página
    return render_template('ejercicio2.html', mensaje=None)

# iniciar el servidor modo desarrollo
if __name__ == '__main__':
    app.run(debug=True)
