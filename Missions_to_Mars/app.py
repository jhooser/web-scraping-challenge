
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")
@app.route("/")
def index():
     mars_data= mongo.db.listings.find_one()
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scraper():

    # Run the scrape function
    mars_data = scrape.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, costa_data, upsert=True)

    # Redirect back to home page
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)
