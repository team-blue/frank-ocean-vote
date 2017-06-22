from flask import Flask, render_template, request
import os
import webbrowser

app = Flask(__name__)
 
# frank_ocean_songs = {"Nikes" : 0, "Ivy" : 0, "Pink+White" : 0, "Be Yourself" : 0, "Solo" : 0}
poll_data = {
   'question' : 'Which Frank Ocean Song do you like best?',
   'fields'   : ['Nikes', 'Ivy', 'Pink+White', 'Be Yourself', 'Solo']
}

filename = 'data.txt'


@app.route('/')
def root():
    return render_template('poll.html', data=poll_data)

@app.route('/poll')
def poll():
    vote = request.args.get('field')
 
    out = open(filename, 'a')
    out.write( vote + '\n' )
    out.close()
 
    return render_template('thankyou.html', data=poll_data)



@app.route('/results')
def show_results():
    votes = {}
    for f in poll_data['fields']:
        votes[f] = 0
 
    f  = open(filename, 'r')
    for line in f:
        vote = line.rstrip("\n")
        votes[vote] += 1
 
    return render_template('results.html', data=poll_data, votes=votes)


if __name__ == "__main__":
    app.run(debug=True)





