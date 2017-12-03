"""views for the CRUD actions."""
from django.shortcuts import render

from .models import Price

def plot(request):
    """Example plot in django."""

    image_type = 'png'  # svg or png

    # https://scipy-cookbook.readthedocs.io/items/Matplotlib_Django.html
    import random
    import django
    import datetime
    import matplotlib
    import numpy as np
    from matplotlib.pyplot import figure
    from matplotlib.figure import Figure
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import matplotlib.cbook as cbook

    if image_type == 'svg':
        from matplotlib.backends.backend_svg import FigureCanvasSVG as FigureCanvas
        # todo: the svg output is kind of verbose
        # fix is here: https://stackoverflow.com/questions/34387893/output-matplotlib-figure-to-svg-with-text-as-text-not-curves
    elif image_type == 'png':
        from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

    years = mdates.YearLocator()  # every year
    months = mdates.MonthLocator()  # every month
    yearsFmt = mdates.DateFormatter('%Y')

    from matplotlib.figure import Figure
    # from matplotlib.dates import DateFormatter

    all_entries = Price.objects.all().order_by('time')

    dates = []
    prices = []

    for entry in all_entries:
        dates.append(datetime.datetime.fromtimestamp(entry.time))
        prices.append(entry.high)

    fig = figure()
    # Firs plot
    ax = fig.add_subplot(211)
    ax.plot(dates,prices)

    # Format the ticks
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.xaxis.set_minor_locator(months)

    # Second plot
    x = [1,2,3,4,5,6]
    y = [50,12,88,43,23,89]
    bx = fig.add_subplot(212)
    bx.plot(x,y)

    # Third plot
    x2 = [1, 2, 3, 4, 5, 6]
    y2 = [50, 12, 88, 43, 23, 89]
    bx = fig.add_subplot(21)
    bx.plot(x2, y2)


    canvas = FigureCanvas(fig)

    if image_type == 'svg':
        response = django.http.HttpResponse(content_type='image/svg+xml')
        canvas.print_svg(response)
    elif image_type == 'png':
        response = django.http.HttpResponse(content_type='image/png')
        canvas.print_png(response)

    return response


def coins(request):
    """Page to show coin plot."""
    return render(request, 'coins.html', {})
