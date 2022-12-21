### clientes = /clientes/<int:id>

- curl http://localhost:5000/clientes | json_pp
- curl http://localhost:5000/clientes/1 | json_pp
- curl http://localhost:5000/clientes/2 | json_pp

### cuentas = /clientes/<int:id>/cuentas

- curl http://localhost:5000/clientes/1/cuentas | json_pp
- curl http://localhost:5000/clientes/2/cuentas | json_pp

### buscar pagos = /pagos/<int:cliente_id>/buscar?servicio=str&empresa=str

Respuesta - error falta 2 parametros
- curl http://localhost:5000/pagos/1/buscar | json_pp

Respuesta - error falta 1 parametros
- curl http://localhost:5000/pagos/1/buscar?servicio=netflix | json_pp

Respuesta - ok pago no encontrado
- curl http://localhost:5000/pagos/1/buscar?servicio=streaming&empresa=netflix | json_pp

Respuesta - ok pago
- curl http://localhost:5000/pagos/1/buscar?servicio=celular&empresa=movistar | json_pp

Respuesta - ok pago
- curl http://localhost:5000/pagos/2/buscar?servicio=streaming&empresa=netflix | json_pp

### pagar = /pagos/<int:id>/pagar?clave=str&cuenta=str

Respuesta - error falta 2 parametros
- curl http://localhost:5000/pagos/1000/pagar | json_pp

Respuesta - error falta 1 parametros
- curl http://localhost:5000/pagos/1000/pagar?clave=123 | json_pp

Respuesta - ok pago no encontrado
- curl http://localhost:5000/pagos/5000/pagar?clave=123&cuenta=123 | json_pp

Respuesta - ok pago encontrado, ok cuenta no encontrada
- curl http://localhost:5000/pagos/1000/pagar?clave=123&cuenta=123 | json_pp

Respuesta - ok pago, ok cuenta, error clave
- curl http://localhost:5000/pagos/1000/pagar?clave=123&cuenta=1941967786134 | json_pp

Respuesta - ok pago, ok cuenta, ok clave
- curl http://localhost:5000/pagos/1000/pagar?clave=192389&cuenta=1941967786134 | json_pp
- curl http://localhost:5000/pagos/1000/pagar?clave=145701&cuenta=1931853946025 | json_pp
- curl http://localhost:5000/pagos/1001/pagar?clave=145605&cuenta=1921153676312 | json_pp
