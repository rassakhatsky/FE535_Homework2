from flask import Flask, render_template_string, request, flash
from wtforms import RadioField, FloatField, IntegerField
from wtforms.validators import DataRequired
from flask.ext.wtf import Form
#from  BlackFormula import Option

application = Flask(__name__)

SECRET_KEY = 'blablbablablbalablbasecretkeyissosecret'

template = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>FE535 - Homework 2</title>
    <style type="text/css">
        .bs-example {
            margin: 20px;
        }
    </style>

    {% if title %}
        <title>{{ title }} - FE535</title>
    {% else %}
    {% endif %}
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul class=flashes>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    {% block body %}{% endblock %}

</head>
<body>
<div>FE535: <a href="/">Homework 2</a> |
    <a href="/blackformula">Black Formula calculator (example 1)</a> |
    <a href="/volatility">Implied volatility calculator (example 2)</a> |
</div>
<hr>
<h1>Implied volatility calculator</h1>

<form action="" method="post" name="calculator">
    {{ form.hidden_tag() }}
    <p>
        Days in Year:
        {% for subfield in form.daysYear %}
            <tr>
                <td>{{ subfield }}</td>
                <td>{{ subfield.label }}</td>
            </tr>
        {% endfor %}
    </p>

    <p>
        Option type:
        {% for subfield in form.optionType %}
            <tr>
                <td>{{ subfield }}</td>
                <td>{{ subfield.label }}</td>
            </tr>
        {% endfor %}
    </p>
    <p>{{ form.spotPrice.label }}: {{ form.spotPrice(size=10) }}</p>

    <p>{{ form.strikePrice.label }}: {{ form.strikePrice(size=10) }}</p>

    <p>{{ form.timeDays.label }}: {{ form.timeDays(size=10) }}</p>

    <p>{{ form.rate.label }}: {{ form.rate(size=10) }}</p>

    <p>{{ form.dividendYeld.label }}: {{ form.dividendYeld(size=10) }}</p>
    <br><br>

    <p>
        Target Action:
        {% for subfield in form.target %}
            <br>
            <tr>
                <td>{{ subfield }}</td>
                <td>{{ subfield.label }}</td>
            </tr>
        {% endfor %}

    </p>
    <p>{{ form.volatility.label }}: {{ form.volatility(size=10) }}</p>

    <p>{{ form.price.label }}: {{ form.price(size=10) }}</p>

    <p><input type="submit" value="Calculate"></p>
</form>
</body>
</html>
<head>
</head>

<script>
    function clear() {
        document.getElementById("myForm").reset();
    }
</script>'''


class Calculator(Form):
    optionType = RadioField('Option Type', choices=[('put', 'Put'), ('call', 'Call')], validators=[DataRequired()],
                            default='put')
    daysYear = RadioField('Days in Year', choices=[(365, 365), (360, 360), (252, 252)], default=360,
                          validators=[DataRequired()])

    spotPrice = FloatField('Spot Price, $', validators=[DataRequired()], default=1000.0)
    strikePrice = FloatField('Strike Price, $', validators=[DataRequired()], default=1000.0)
    timeDays = IntegerField('Maturity, days', validators=[DataRequired()], default=30)
    rate = FloatField('Rate, %', validators=[DataRequired()], default=0.0)
    dividendYeld = FloatField('Dividend Yeld, %', validators=[DataRequired()], default=0.0)

    target = RadioField('Target action',
                        choices=[('volatility', 'Calculate Volatility, %'), ('price', 'Calculate Option Price, $')],
                        validators=[DataRequired()], default='price')

    volatility = FloatField('Volatility, %')
    price = FloatField('Option Price, $')

@application.route('/hi', methods=['GET', 'POST'])
def hi():
    form = Calculator()
    return render_template_string(template, title='FE535 - Homework 2', form=form)
'''
@application.route('/', methods=['GET', 'POST'])
@application.route('/volatility', methods=['GET', 'POST'])
@application.route('/blackformula', methods=['GET', 'POST'])
def calculator():
    form = Calculator()
    if str(request.url_rule) == '/blackformula':
        form.optionType.data = 'put'
        form.optionType.object_data = 'put'
        form.optionType.raw_data = ['put']
        form.spotPrice.data = 1314.49
        form.spotPrice.object_data = 1314.49
        form.spotPrice.raw_data = [str(1314.49)]
        form.strikePrice.data = 1314.49
        form.strikePrice.object_data = 1314.49
        form.strikePrice.raw_data = [str(1314.49)]
        form.daysYear.data = str(360)
        form.daysYear.object_data = 360
        form.daysYear.raw_data = [str(360)]
        form.timeDays.data = 180
        form.timeDays.object_data = 180
        form.timeDays.raw_data = [str(180)]
        form.volatility.data = 20.252
        form.volatility.object_data = 20.252
        form.volatility.raw_data = [str(20.252)]
        form.rate.data = 0.78525
        form.rate.object_data = 0.78525
        form.rate.raw_data = [str(0.78525)]
        form.dividendYeld.data = 2.211
        form.dividendYeld.object_data = 2.211
        form.dividendYeld.raw_data = [str(2.211)]
        form.price.data = None
        form.price.object_data = None
        form.price.raw_data = [str('')]
        form.target.data = 'price'
        form.target.object_data = 'price'
        form.target.raw_data = [str('price')]

    if str(request.url_rule) == '/volatility':
        form.optionType.data = 'call'
        form.optionType.object_data = 'call'
        form.optionType.raw_data = ['call']
        form.spotPrice.data = 1314.25
        form.spotPrice.object_data = 1314.25
        form.spotPrice.raw_data = [str(1314.25)]
        form.strikePrice.data = 1314.25
        form.strikePrice.object_data = 1314.25
        form.strikePrice.raw_data = [str(1314.25)]
        form.daysYear.data = str(360)
        form.daysYear.object_data = 360
        form.daysYear.raw_data = [str(360)]
        form.timeDays.data = 30
        form.timeDays.object_data = 30
        form.timeDays.raw_data = [str(30)]
        form.volatility.data = None
        form.volatility.object_data = None
        form.volatility.raw_data = [str('')]
        form.rate.data = 0.261
        form.rate.object_data = 0.261
        form.rate.raw_data = [str(0.261)]
        form.dividendYeld.data = 2.886
        form.dividendYeld.object_data = 2.886
        form.dividendYeld.raw_data = [str(2.886)]
        form.price.data = 23.47
        form.price.object_data = 23.47
        form.price.raw_data = [str(23.47)]
        form.target.data = 'volatility'
        form.target.object_data = 'volatility'
        form.target.raw_data = [str('volatility')]

    if request.method == 'POST':
        optionType = form.optionType.data
        daysYear = int(form.daysYear.data)
        spotPrice = form.spotPrice.data
        strikePrice = form.strikePrice.data
        timeDays = form.timeDays.data
        rate = form.rate.data
        dividendYeld = form.dividendYeld.data
        volatility = form.volatility.data
        price = form.price.data
        target = form.target.data

        if not volatility is None and target == 'price':  # calc price
            option = Option(option=optionType, spotPrice=spotPrice, strikePrice=strikePrice, timeDays=timeDays,
                            rate=rate / 100.0, dividendYeld=dividendYeld / 100.0, volatility=volatility / 100.0,
                            daysYear=daysYear)
            price = option.calculatePrice()

            form.price.data = price
            form.price.object_data = price
            form.price.raw_data = [str(price)]

        elif not price is None and target == 'volatility':  # calc vol
            option = Option(option=optionType, spotPrice=spotPrice, strikePrice=strikePrice, timeDays=timeDays,
                            rate=rate / 100.0, dividendYeld=dividendYeld / 100.0, volatility=200 / 100.0,
                            daysYear=daysYear)
            volatility = option.imp_vol(price)

            form.volatility.data = volatility
            form.volatility.object_data = volatility
            form.volatility.raw_data = [str(volatility)]
        else:
            flash('Volatility or Option Price has to be set')
    return render_template_string(template, title='FE535 - Homework 2', form=form)

'''
if __name__ == '__main__':
    application.debug = False
    application.secret_key = SECRET_KEY
    application.run()
