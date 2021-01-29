from flask import Flask, render_template, url_for, request, redirect, jsonify
# from flask_restful import Api, Resource
# from paypalsdk import PayPalClient
# from paypalcheckoutsdk.orders import OrdersCaptureRequest
import csv
import requests
app = Flask(__name__)
print(app)

# creating the server route to the checkout page with PayPal smart button (index.html)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

# write to csv not used, has potential use as a databse if needed.

# def write_to_csv(data):
# 	with open('database.csv', newline='', mode='a') as database:
# 		status = data["status"]
# 		order_ID = data["id"]
# 		description = data["purchase_units"][0]["description"]
# 		address_line1 = data["purchase_units"][0]["shipping"]["address"]["address_line_1"]
# 		address_line2 = data["purchase_units"][0]["shipping"]["address"]["admin_area_2"]
# 		city = data["purchase_units"][0]["shipping"]["address"]["admin_area_1"]
# 		postcode = data["purchase_units"][0]["shipping"]["address"]["postal_code"]
# 		country = data["purchase_units"][0]["shipping"]["address"]["country_code"]
# 		csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
# 		csv_writer.writerow([status, order_ID, description, address_line1, address_line2, city, postcode, country])


@app.route('/approve/<string:orderID>', )
def captureorder123(orderID):
	r = requests.get("https://api-m.sandbox.paypal.com/v2/checkout/orders/" + orderID, headers={'Authorization': 'bearer A21AAIdebjLo7Y3abykgNXWST6cEhoVQ53MOTdCUJjMVCirPQ2lfC8LVCRinyK8WB6av0ZCOgaitdMvqDe8ziTMME7qhug6jA'})
	res = r.json()
	# write to csv not used, potentially has use as a database
	# write_to_csv(res) 
	sale_id = res["id"]
	description = res["purchase_units"][0]["description"]
	address_line1 = res["purchase_units"][0]["shipping"]["address"]["address_line_1"]
	address_line2 = res["purchase_units"][0]["shipping"]["address"]["admin_area_2"]
	city = res["purchase_units"][0]["shipping"]["address"]["admin_area_1"]
	postcode = res["purchase_units"][0]["shipping"]["address"]["postal_code"]
	country = res["purchase_units"][0]["shipping"]["address"]["country_code"]
	return render_template('paymentcomplete.html', order_id=sale_id, desc=description, add1=address_line1, add2 = address_line2, add3 = city, pcode=postcode, country1=country)


@app.route('/approved/<string:order_id>', )
def captureorder1(orderID):
	return redirect('/paymentcomplete.html/orderID', )
