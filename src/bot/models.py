from pydantic import BaseModel


class Card(BaseModel):
    id: int
    name: str
    brand: str
    brandId: int
    rating: int
    priceU: int

    def display(self):
        return f"ID: {self.id}\nName: {self.name}\nBrand: {self.brand}\nBrand ID: {self.brandId}\nRating: {self.rating}\npriceU: {self.priceU}"
