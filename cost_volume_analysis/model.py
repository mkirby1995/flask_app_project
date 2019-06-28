from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Widget(DB.Model):
    name = DB.Column(DB.String(100), primary_key = True)
    fixed_costs = DB.Column(DB.Integer)
    variable_costs = DB.Column(DB.Integer)
    price_point = DB.Column(DB.Integer)

    def __repr__(self):
      return "{}".format(self.name)


products = [
    # Name, fixed_costs, variable_costs, price_point
    ('Book', 5000.00, 4.50, 25.00),
    ('Truck', 10000000.00, 25000.00, 60000.00),
    ('Cup', 200.00, 0.50, 2.50),
    ('Burger', 25000.00, 3.50, 5.50),
]


def upload_widgets(widget_list):
    for _ in range(len(widget_list)):
        product = Widget(
            name = widget_list[_][0],
            fixed_costs = widget_list[_][1],
            variable_costs = widget_list[_][2],
            price_point = widget_list[_][3])
        DB.session.add(product)
        DB.session.commit()


def add_widget(name, fixed_costs, variable_costs, price_point):
    product = Widget(
        name = name,
        fixed_costs = fixed_costs,
        variable_costs = variable_costs,
        price_point = price_point)
    DB.session.add(product)
    DB.session.commit()
