import json
from decimal import Decimal

from flask import jsonify

def handle(req):
    
    fact = 1
    data = json.loads(req)
    n = data.get("number")
    
    for i in range(1, n+1):
        fact = Decimal(fact * i)

    return jsonify(result=fact)
