class DataframeFormatter:
    def format_dataframe(self, input_file):
        # Assuming `coordinates` is a string in list or tuple format '[x, y]'
        input_file['coordinates'] = input_file['coordinates'].apply(lambda coord: self.format_coordinates(coord))
        return input_file

    def format_coordinates(self, coordinates):
        # Here you implement the logic to format the coordinates as desired
        coordinates = coordinates.strip("[]'()")
        return coordinates
