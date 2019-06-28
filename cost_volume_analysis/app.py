from flask import Flask, request, render_template
from .model import DB, Widget, upload_widgets, products, add_widget

def create_app():
    """Create and configure instance of flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)


    @app.route('/')
    def root():
        widgs = Widget.query.all()
        return render_template('base.html', title = 'Home', widgets = widgs)

    @app.route('/refresh')
    def refresh():
      """Pull fresh data from dict"""
      DB.drop_all()
      DB.create_all()
      upload_widgets(products)
      DB.session.commit()
      return 'Data refreshed'

    @app.route('/product', methods = ['POST'])
    @app.route('/product/<name>', methods = ['GET'])
    def product(name = None, message = ''):
        product_name = name or request.values['widget_name']
        fixed_costs = fixed_costs or request.values['widget_fixed_costs']
        variable_costs = variable_costs or request.values['widget_variable_costs']
        price_point = price_point or request.values['widget_price_point']
        if request.method == 'POST':
            add_widget(name, fixed_costs, variable_costs, price_point)
            message = "{} successfully added!".format(product_name)
        return render_template('product.html',
                               title = product_name,
                               fixed_costs = fixed_costs,
                               variable_costs = variable_costs,
                               price_point = price_point)


    return app

# link to notbook for cva
"""https://colab.research.google.com/drive/1bK6oaYlRxzKEy1yoGhGmPlcIQI7A_LXJ#scrollTo=7cPePPxa_o80"""
