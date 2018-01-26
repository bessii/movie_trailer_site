#!/usr/bin/python
# -*- coding: utf-8 -*-


class Movie:

    """ This class provides a way to store movie related information.
    It contains the __init__ method which represents the constructor of
    the class and it serves as a blueprint to create different movie objects"""
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(
         self,
         movie_title,
         movie_storyline,
         poster_image,
         trailer_youtube,
         ):

            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube
