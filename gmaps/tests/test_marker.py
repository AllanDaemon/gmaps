
import unittest
import pytest

import numpy as np

from ..marker import _marker_layer_options, _symbol_layer_options


class MarkerLayer(unittest.TestCase):

    def setUp(self):
        self.locations = [(-5.0, 5.0), (10.0, 10.0)]

    def test_hover_text_atomic(self):
        marker_options = _marker_layer_options(
            self.locations, hover_text="test-text", label="")
        for options in marker_options:
            assert options["hover_text"] == "test-text"

    def test_hover_text_lists(self):
        marker_options = _marker_layer_options(
            self.locations, hover_text=["t1", "t2"], label="")
        hover_texts = [options["hover_text"] for options in marker_options]
        assert tuple(hover_texts) == ("t1", "t2")

    def test_locations_array(self):
        marker_options = _marker_layer_options(
            np.array(self.locations), hover_text="", label="")
        locations = [options["location"] for options in marker_options]
        assert locations == self.locations

    def test_locations_pandas_df(self):
        pd = pytest.importorskip("pandas")
        df = pd.DataFrame.from_records(
            self.locations, columns=["latitude", "longitude"])
        marker_options = _marker_layer_options(
            df, hover_text="", label="")
        locations = [options["location"] for options in marker_options]
        assert locations == self.locations


class SymbolLayer(unittest.TestCase):

    def setUp(self):
        self.locations = [(-5.0, 5.0), (10.0, 10.0)]
        self.kwargs = {
            "hover_text": "", "fill_color": "red", "scale": 5,
            "fill_opacity": 1.0, "stroke_opacity": 1.0
        }

    def test_stroke_color_atomic_text(self):
        symbol_options = _symbol_layer_options(
            self.locations, stroke_color="red", **self.kwargs)
        for options in symbol_options:
            assert options["stroke_color"] == "red"

    def test_stroke_color_atomic_tuple(self):
        color = (10, 10, 10, 0.5)
        symbol_options = _symbol_layer_options(
            self.locations, stroke_color=color, **self.kwargs)
        for options in symbol_options:
            assert options["stroke_color"] == color

    def test_stroke_color_list_text(self):
        symbol_options = _symbol_layer_options(
            self.locations, stroke_color=["red", "green"], **self.kwargs)
        opts = [options["stroke_color"] for options in symbol_options]
        assert tuple(opts) == ("red", "green")

    def test_stroke_color_list_tuples(self):
        c1 = (10, 10, 10, 0.5)
        c2 = (20, 20, 20, 0.5)
        symbol_options = _symbol_layer_options(
            self.locations, stroke_color=[c1, c2], **self.kwargs)
        opts = [options["stroke_color"] for options in symbol_options]
        assert tuple(opts) == (c1, c2)
