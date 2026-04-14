# x và y là các đối tượng dạng mảng
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import plotly.express as px

print("Creating and opening chart. Please check your browser...")
fig = px.scatter(x=[0, 1, 1, 2, 3, 4], y=[0, 1, 4, 16, 9, 16])

print("Creating and opening chart. Please check your browser...")
fig.show(renderer="browser")
print("Chart display command executed.")
