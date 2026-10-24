import os
from abc import ABC, abstractmethod

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from a .env file
load_dotenv()


class APIBase(ABC):
    """Base class for AI listing providers."""

    def __init__(self, api_key: str, base_url: str, model: str):
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    @abstractmethod
    def generate_listing(self, product_specs, estimated_price_, comparables):
        """Generate a product listing using the provided data."""
        raise NotImplementedError


class AIListing(APIBase):
    """Concrete implementation for generating refurbished product listings."""

    def __init__(self):
        api_key = os.getenv("AI_API_KEY")
        base_url = os.getenv("AI_BASE_URL")
        model = os.getenv("AI_MODEL")

        if not api_key:
            raise ValueError("AI_API_KEY is missing from .env file.")
        if not base_url:
            raise ValueError("AI_BASE_URL is missing from .env file.")
        if not model:
            raise ValueError("AI_MODEL is missing from .env file.")

        super().__init__(api_key=api_key, base_url=base_url, model=model)

    def generate_listing(self, product_specs, estimated_price_, comparables):
        prompt = """
        Write an accurate listing for a refurbished product intended for a website.
        Rules:
        - Only use specifications provided.
        - Never invent any other details about the product.
        - Describe the estimated price as an estimate based on comparables, not a guarantee.
        - Keep the tone professional and informative, as if a potential customer may read the listing.
        """

        user_prompt = f"""
        Create a product listing with the following details:
        Product Specifications: {product_specs}
        Estimated Price: {estimated_price_}
        Comparables: {comparables}

        Follow the rules above and ensure the listing is clear, concise, and informative.
        Write a bullet list of the product specifications and a short paragraph about the estimated price and comparables.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=800,
            temperature=0.7,
        )

        if not response.choices or not response.choices[0].message.content:
            raise ValueError("The AI returned no response.")

        return response.choices[0].message.content