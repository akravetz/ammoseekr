from datetime import datetime

from pydantic import BaseModel, Field


class AmmoSale(BaseModel):
    retailer_name: str
    description: str
    brand_name: str
    caliber: str
    grains: int = Field(default=0, ge=0)
    price: float = Field(default=0.0, ge=0.0)
    rounds: int = Field(default=1, ge=1)
    price_per_round: float = Field(default=0.0, ge=0.0)
    rating: float = Field(default=0.0, ge=0.0)
    count_reviews: int = Field(default=0, ge=0)
    scraped_at: datetime
