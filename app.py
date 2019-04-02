from flask import Flask, render_template, request, redirect, url_for, logging, session, flash

from devices import Devices

app = Flask(__name__)
app.debug=True

devices = Devices()


# Home route
@app.route('/')
def home():
    return render_template('home.html')

# About Route/Page
@app.route('/about')
def about():
    return render_template('about.html')



# Dashboard Route
@app.route('/dashboard')
def dashboard():
    print("Dashboard")
    # Retriving data from database will go here
    # First will have to get the data from the database and then send to the view
    return render_template('dashboard.html', devices=devices)

# Device Control Route
@app.route('/device/<string:id>/<string:action>/')
def device_control(id, action):
    for index in range(len(devices)):
        if devices[index]['id'] == int(id):
            # Update status
            devices[index]['status'] = action
            # Turn on/off the device
            #Change the pin
            #### Your Devices Pin controls code will go here.###
            print(devices[index]['pin'])
            flash('Successful!! ' + devices[index]['name'] + ' updated', 'success')
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.secret_key = 'verySecret#123'
    app.run()
