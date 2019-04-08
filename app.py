from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
from waitress import serve
import waitress

app = Flask(__name__)

class Community:
  def __init__(self):
  	self.house = None
  	self.restaurant = None
  	self.transport = None
  	self.recreation = None

session = Community()

@app.route('/')
def welc():
	return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
	session.house = request.form['house']
	session.restaurant = request.form['restaurant']
	session.transport = request.form['transport']
	session.recreation = request.form['recreation']
	return '', 204

@app.route('/dashboard')
def dash():
	restaurantExplanation = reason(session.restaurant)
	return render_template('neighborhood.html', house=session.house, restaurant=session.restaurant, transport=session.transport, recreation=session.recreation,
		restaurantExplanation = reason(session.restaurant), transportExplanation = reason(session.transport), recreationExplanation = reason(session.recreation))

def reason(png):
	png = png.lower()
	if png == 'bakeryshop.png':
		return 'you are helping a baker that lives in your community pay their bills and feed their family.'
	elif png == 'barbershop.png':
		return 'you have a good relationship with the barber and the recurring patrons and you receieve free haircuts'
	elif png == 'bike1.png':
		return 'you are saving money by not paying for transportation and getting exercise that will benefit you in the long run'
	elif png == 'books.png':
		return 'you might stop by the book shop at least once a week to chat with the owner and you are reading more often and learning new skills'
	elif png == 'bus1.png':
		return 'you are able to talk to your neighbors on your commute and you save money by not having a car'
	elif png == 'cafe.png':
		return 'you are able to bring your own mug to the coffee shop to get fresh made coffee every day'
	elif png == 'florist.png':
		return 'you buy flowers for your loved ones more often'
	elif png == 'icecream.png':
		return 'you are supporting a local dairy farmer in the community'
	elif png == 'movies.png':
		return 'you can watch movies as often as you want and support local artists'
	elif png == 'pharm.png':
		return 'your pharmacist will know you by name and can provide knowledge about certain medications on a more regular basis'
	elif png == 'pizza.png':
		return 'you are supporting the local dairy farm where the cheese is purchased and have access to fresh dough when you want to make a pizza at home'
	elif png == 'train1.png':
		return 'you are paying for public transit which benefits the community and you can avoid rush hour traffic that may be prevalent on the street'
	elif png == 'walk1.png':
		return 'you are reducing your carbon footprint and getting exercise'

if __name__ == '__main__':
	waitress.serve(app, host='0.0.0.0', port=5000, url_scheme='https')
	#app.debug = False
	#app.run(host='0.0.0.0')