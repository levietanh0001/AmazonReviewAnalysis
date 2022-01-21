from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import render
from django.http import HttpResponse
from bokeh.plotting import figure
from bokeh.embed import components
from sqlalchemy import create_engine
import pandas as pd
 

def home(request):
    # db = 'canned_coffee_5star_processed'
    # user = 'root'
    # passwd = ''
    # host =  'localhost'
    # port = 3306
    # engine = create_engine(f'mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}')
    # df = pd.read_sql('SELECT * FROM starbucks_frappuccino_5star', con=engine)
    #create a plot
    plot = figure(plot_width=400, plot_height=400)

    # add a circle renderer with a size, color, and alpha

    # plot.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

    script, div = components(plot)

    return render(request, 'base.html', {'script': script, 'div': div})