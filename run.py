from application import create_app
import sys

print('Rainfall Service Started', file=sys.stdout)
app = create_app()
app.run(
     host='0.0.0.0',
     port='8080',
     debug='True'
)
