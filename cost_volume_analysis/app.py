from flask import Flask, request, render_template
from .model import DB, Widget, add_widgets, widgets

def create_app():
    """Create and configure instance of flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)


    @app.route('/')
    def root():
        widgets = Widget.query.all()
        return render_template('base.html', title = 'Home', widgets = widgets)

    @app.route('/refresh')
    def refresh():
      """Pull fresh data from dict"""
      DB.drop_all()
      DB.create_all()
      add_widgets(widgets)
      DB.session.commit()
      return 'Data refreshed'
