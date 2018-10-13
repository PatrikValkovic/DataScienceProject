from flask import Flask, render_template, flash, request
from wtforms import Form, validators, StringField
from TwitterGet import get_from_twitter
from ProcessTweets import process_tweets
from Config import config

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    query = StringField('Query:', validators=[validators.required()])
 
 
@app.route("/", methods=['GET', 'POST'])
def webapp():
    form = ReusableForm(request.form)
    # words = [
    #     'trump charity president 2018 warren test million denying native right saudi ties ',
    #     'king rogue using jamal arabia says prompting speculate minutes donald long ',
    #     'suggests mouth replied question secdef stay james ',
    # ]
    words = []



    if request.method == 'POST':
        query = request.form['query']
        tweetsno = request.form['tweetsno']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        radius = request.form['radius']
        worldwide = 'worldwide' in request.form
        #datefrom=request.form['datefrom']
        #dateto=request.form['dateto']

        if form.validate():
            processed = makeSearch(query,
                                   int(tweetsno),
                                   float(latitude) if not worldwide else None,
                                   float(longitude) if not worldwide else None,
                                   float(radius))
            words = processed[0]
            flash('Analyzed ' + str(processed[1]) + ' tweets', 'result')
        else:
            flash('All the form fields are required.', 'error')
 
    return render_template('webapp.html', form=form, words=words, MAP_KEY=config['Google']['map_key'])

def makeSearch(query : str, tweetsno, latitude, longitude, radius):
    tweets = list(get_from_twitter(query.split(' '), 'en', tweetsno, longitude, latitude, int(radius)))
    count = len(tweets)
    return (process_tweets(tweets), count)
 
if __name__ == "__main__":
    app.run()