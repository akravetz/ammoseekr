import re
from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field, HttpUrl, model_validator


class AmmoListing(BaseModel):
    retailer_name: str
    description: str
    brand_name: str
    caliber: str
    grains: Optional[int] = Field(default=0, ge=0)
    price: float = Field(default=0.0, ge=0.0)
    rounds: int = Field(default=1, ge=1)
    price_per_round: float = Field(default=0.0, ge=0.0)
    rating: float = Field(default=0.0, ge=0.0)
    count_reviews: int = Field(default=0, ge=0)
    scraped_at: datetime
    url: HttpUrl

    @model_validator(mode="before")
    @classmethod
    def process_data(cls, data: Any) -> Any:
        """
        This function takes the messy, hierarchical json data returns by the ammoseek website
        and munges it into the appropriate format required by our pydantic model
        """
        # Extract and clean the price
        # returned from ammoseek as "$XX.YY"
        price_str = data.get("price", "")
        price = float(re.sub(r"[^\d.]", "", price_str))

        # either integer or "?"
        grains = data.get("grains", "?")
        if grains == "?":
            grains = None

        # Extract nested ratings values from DT_RowData
        dt_row_data = data.get("DT_RowData", {})
        rating = float(dt_row_data.get("rating", 0))
        count_reviews = dt_row_data.get("numratings", 0)

        # Calculate rounds and price_per_round
        rounds = data.get("count", 1)
        price_per_round = price / rounds if rounds > 0 else 0.0

        # Add the current timestamp for scraped_at
        scraped_at = datetime.now()

        # relative URL to the deal
        relative_url_id = data.get("DT_RowId", "")

        # Return the values to be assigned to the model
        return {
            "retailer_name": data.get("retailer", ""),
            "description": data.get("descr", ""),
            "brand_name": data.get("mfg", ""),
            "caliber": data.get("caliber", ""),
            "grains": grains,
            "price": price,
            "rounds": rounds,
            "price_per_round": price_per_round,
            "rating": rating,
            "count_reviews": count_reviews,
            "url": f"https://www.ammoseek.com/go.to/{relative_url_id}/a",
            "scraped_at": scraped_at,
        }
