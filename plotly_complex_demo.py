import sys
import io
import plotly.express as px

# Ensure UTF-8 for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

print("Loading dataset and creating an animated complex chart...")

# Loading the Gapminder dataset provided by Plotly Express
df = px.data.gapminder()

# Creating a bubble chart with animations over the years
fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    animation_frame="year",
    animation_group="country",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=55,
    range_x=[100, 100000],
    range_y=[25, 90],
    title="Evolution of Global Health and Wealth (Gapminder Dataset)",
    labels={
        "gdpPercap": "GDP per Capita (USD, log scale)",
        "lifeExp": "Life Expectancy (Years)",
        "pop": "Population",
        "continent": "Continent",
    },
    template="plotly_dark",
)

# Export to HTML file for download
output_file = "plotly_chart.html"
fig.write_html(output_file, include_plotlyjs="cdn")
print(f"✓ Chart exported to: {output_file}")
print("You can download this file from the workflow artifacts on GitHub.")
