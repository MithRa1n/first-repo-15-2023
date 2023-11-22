class Movie:
    """
    Movie object
    """
    
    def __init__(self,name,duration,imdb_reviews):
        """
        Initialization
        """
        self.__name = name
        self.__duration = duration
        self.__imdb_reviews = imdb_reviews
        self.some_int = 15
        self.some_str = "Hi"
    def set_name(self, name):
        self.__name = name
    def set_duration(self,duration):
        self.__duration = duration
    def set_imbd_reviews(self,imdb_reviews):
        self.get_name()
        self.__imdb_reviews = imdb_reviews
    def get_name(self):
        return self.__name
    def get_duration(self):
        return self.__duration
    def get_imbd_reviews(self):
        return self.__imdb_reviews
    def __str__(self):
        """
        Return values of Film object as a string
        """
        return f"{self.__name} lasts for {self.__duration} minutes with {self.__imdb_reviews} reviews on it."
    def __repr__(self):
        return f"{self.__name} {self.__duration} {self.__imdb_reviews}"
    def __del__(self):
        print(f"{self.__name} - deleted")
if __name__ == "__main__":
    movie1 = Movie("Interstellar", 169, 8.6)
    movie2 = Movie("The Shawshank Redemption", 142, 9.3)
    movie3 = Movie("Star Wars: Episode IV - A New Hope", 121, 8.6)
    print(movie1.get_name())
    print(repr(movie1), (movie1), "\n")
    print(movie2.get_name())
    print(repr(movie2), (movie2), "\n")
    print(movie3.get_name())
    print(repr(movie3), (movie3), "\n")