from django.shortcuts import render
from .models import Project
import pandas as pd
from plotly.offline import plot
import plotly.express as px


def index(request):
    qs = Project.objects.all()
    projects_data = [
        {
            'Project': x.name,
            'Start': x.start_date,
            'Finish': x.end_date,
            'Manager': x.manager
        } for x in qs
    ]
    df = pd.DataFrame(projects_data)
    fig = px.timeline(
        df, x_start="Start", 
        x_end="Finish",
        y="Project",
        color="Manager",
    )
    fig.update_yaxes(autorange='reversed')
    gantt_plot = plot(fig, output_type='div')
    context = {'plot_div': gantt_plot}

    return render(request, 'core/index.html', context)



