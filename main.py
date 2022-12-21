clientes = [{
    "id": 1,
    "nombre": "Juan",
}, {
    "id": 2,
    "nombre": "Pedro"
}]

cuentas = [{
    "id": "1941967786134",
    "tipo": "Ahorro",
    "moneda": "PEN",
    "clave_web": "192389",
    "cliente_id": 1
}, {
    "id": "1931853946025",
    "tipo": "Corriente",
    "moneda": "PEN",
    "clave_web": "145701",
    "cliente_id": 1
},
{
    "id": "1921153676312",
    "tipo": "Ahorro",
    "moneda": "USD",
    "clave_web": "145605",
    "cliente_id": 2
}]

pagos = [{
    "id": 1000,
    "fecha": "2020-01-01",
    "monto": 100,
    "moneda": "PEN",
    "empresa": "movistar",
    "servicio": "celular",
    "cliente_id": 1
}, {
    "id": 1001,
    "fecha": "2020-01-01",
    "monto": 100,
    "moneda": "USD",
    "empresa": "netflix",
    "servicio": "streaming",
    "cliente_id": 2
}]

from flask import Flask, request,jsonify
app=Flask(__name__)

@app.route('/')
def index():
    return "OPCION 02: PAGO DE SERVICIOS"

@app.route('/clientes', methods=['GET'])
def get_clientes():
    return jsonify(clientes)

@app.route('/clientes/<int:id>', methods=['GET'])
def get_cliente(id):
    for cliente in clientes:
        if cliente['id'] == id:
            return jsonify(cliente)
    return jsonify({'message': 'Cliente no encontrado'})

@app.route('/clientes/<int:id>/cuentas', methods=['GET'])
def get_cuentas(id):
    busqueda_clientes = list(filter(lambda c: c['id'] == id, clientes))
    if len(busqueda_clientes) != 1:
        return jsonify({'message': 'Cliente no encontrado'})

    busqueda_cuentas = list(filter(lambda c: c['cliente_id'] == id, cuentas))
    return jsonify(busqueda_cuentas)


@app.route('/pagos/<int:client_id>/buscar', methods=['GET'])
def buscar(client_id):
    args = request.args
    servicio = args.get('servicio',type=str)
    empresa= args.get('empresa') 
    if servicio is None or empresa is None:
        return jsonify({'message': 'servicio o empresa no encontrados'})
    
    pago_cliente = None
    for pago in pagos:
        if pago['cliente_id'] == client_id and pago['servicio'] == servicio and pago['empresa']==empresa:
            pago_cliente = pago
            break
    
    if pago_cliente is None:
        return jsonify({'message': 'Pago no encontrado'})
    
    return pago_cliente

@app.route('/pagos/<int:id>/pagar', methods=['GET'])
def pagar(id):
    args = request.args
    clave = args.get('clave',type=str)
    cuenta_id = args.get('cuenta',type=str)
    if clave is None or cuenta_id is None:
        return jsonify({'message': 'clave o cuenta no encontrados'})
    
    busqueda_pagos = list(filter(lambda p: p['id'] == id, pagos))
    if len(busqueda_pagos) != 1:
        return jsonify({'message': 'Pago no encontrado'})
    pago = busqueda_pagos[0]

    busqueda_cuentas = list(filter(lambda c: c['id'] == cuenta_id, cuentas))
    if len(busqueda_cuentas) != 1:
        return jsonify({'message': 'Cuenta no encontrado'})
    cuenta = busqueda_cuentas[0]

    if clave != cuenta["clave_web"]:
        return jsonify({'message': 'Clave incorrecta'})

    return jsonify({'pago': pago})

if __name__=='__main__':
    app.run()

