from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Widget(DB.Model):
    name = DB.Column(DB.String(100), primary_key = True)
    fixed_costs = DB.Column(DB.Integer)
    variable_costs = DB.Column(DB.Integer)
    price_point = DB.Column(DB.Integer)

    def __repr__(self):
      return "<Product {}>".format(self.name)


products = [
    ('sample widget_1', 1.00, 0.50, 2.50),
    ('sample widget_2', 1.00, 0.50, 2.50),
    ('sample widget_3', 1.00, 0.50, 2.50),
    ('sample widget_4', 1.00, 0.50, 2.50),
]


def add_widgets(widget_list):
    for _ in range(len(widget_list)):
        product = Widget(
            name = widget_list[_][0],
            fixed_costs = widget_list[_][1],
            variable_costs = widget_list[_][2],
            price_point = widget_list[_][3])
        DB.session.add(product)
