class Property:
    def __init__(self, square_feet="", bedrooms="", bathrooms="", **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

    def dispaly(self):
        print("#" * 20)
        print("Property Deatils")
        print()
        print(f"Square Feet : {self.square_feet}")
        print(f"Bedrooms : {self.bedrooms}")
        print(f"Bathrooms : {self.bathrooms}")
        print()

    @staticmethod
    def prompt_init():
        return dict(
            square_feet=input("Enter square feet : "),
            bedrooms=input("Enter bedrooms : "),
            bathrooms=input("Enter bathrooms : "),
        )
