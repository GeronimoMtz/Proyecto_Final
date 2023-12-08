from flask import Blueprint, request, render_template, redirect, url_for, jsonify, abort
from models import Cafe, Venta, Usuario
from forms import CafeForm
from app import db

appcoffee = Blueprint('appcoffee',__name__,template_folder="templates")

@appcoffee.route('/coffee')
def coffee():
    cafes = Cafe.query.all()
    totalDeCafes = Cafe.query.count()
    email_usuario = request.args.get('email_usuario')
    return render_template('coffee.html', cafes = cafes, totalDeCafes = totalDeCafes, email_usuario = email_usuario)

@appcoffee.route('/listacafes')
def inicio():
    cafes = Cafe.query.all()
    totalDeCafes = Cafe.query.count()
    ventas = Venta.query.all()
    totalDeVentas = Venta.query.count()
    usuarios = Usuario.query.all()
    totalDeUsuario = Usuario.query.count()
    return render_template('lista.html',cafes = cafes, totalDeCafes = totalDeCafes, ventas = ventas, totalDeVentas = totalDeVentas,
                           usuarios = usuarios, totalDeUsuario = totalDeUsuario)

@appcoffee.route('/agregarcafe',methods=["GET","POST"])
def agregar():
    cafe = Cafe()
    cafeForm = CafeForm(obj=cafe)
    if request.method == "POST":
        if cafeForm.validate_on_submit():
            cafeForm.populate_obj(cafe)
            db.session.add(cafe)
            db.session.commit()
            return redirect(url_for('appcoffee.inicio'))
    return render_template('agregar.html',forma=cafeForm)

@appcoffee.route('/editarcafe/<int:id>',methods=["GET","POST"])
def editar(id):
    cafe = Cafe.query.get_or_404(id)
    cafeForm = CafeForm(obj=cafe)
    if request.method == "POST":
        if cafeForm.validate_on_submit():
            cafeForm.populate_obj(cafe)
            db.session.commit()
            return redirect(url_for('appcoffee.inicio'))
    return render_template('editar.html',forma=cafeForm)

@appcoffee.route('/eliminarcafe/<int:id>')
def eliminar(id):
    cafe = Cafe.query.get_or_404(id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for('appcoffee.inicio'))

@appcoffee.route('/error')
def error():
    abort(404)

@appcoffee.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('error.html', error=error),404

# Nueva ruta para manejar la compra
@appcoffee.route('/comprar', methods=['POST'])
def comprar():
    print('Ruta /comprar alcanzada')
    try:
        data = request.get_json()
        print('Datos recibidos:', data)
        # Obtén los datos de la compra desde la solicitud
        cliente = data.get('emailUsuario')
        cafes = data.get('cafes')
        cantidad = data.get('cantidad')
        total = data.get('total')

        # Crea un nuevo objeto Venta y regístralo en la base de datos
        venta = Venta(cliente=cliente, cafes=cafes, cantidad=cantidad, total=total)
        db.session.add(venta)
        db.session.commit()

        return jsonify({'success': True, 'message': 'Compra registrada exitosamente'})
    except Exception as e:
        # Manejar errores, puedes personalizar según sea necesario
        return jsonify({'success': False, 'error': str(e)}), 500