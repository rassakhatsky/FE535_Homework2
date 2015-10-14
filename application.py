from flask import Flask, render_template_string, request, flash
from wtforms import RadioField, FloatField, IntegerField
from wtforms.validators import DataRequired
from flask.ext.wtf import Form
from  BlackFormula import Option

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

@application.route('/', methods=['GET', 'POST'])
def hi():
    form = Calculator()
    return render_template_string(template, title='FE535 - Homework 2', form=form)

if __name__ == '__main__':
    application.debug = False
    application.secret_key = SECRET_KEY
    application.run()
