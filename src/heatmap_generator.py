try:
    import folium
    from folium.plugins import HeatMap
except Exception as e:
    print(f"Lib not installed: %s" % e)

class HeatmapGenerator:
    def __init__(self, df):
        self.df = df

    def generate_heatmap(self):
        m = folium.Map(location=[-14.235004, -51.92528], zoom_start=4, tiles='cartodb dark_matter')

        heat_data = self.df['coordinates'].apply(lambda x: [float(i) for i in x.split(', ')]).tolist()

        HeatMap(heat_data).add_to(m)

        m.save('heatmap.html')
