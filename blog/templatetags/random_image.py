from django import template
import requests
import random
from bs4 import BeautifulSoup
import logging
import os
from django.templatetags.static import static

register = template.Library()
logger = logging.getLogger(__name__)

FALLBACK_IMAGE_PATH = 'blog/th-1779141600.jpg'  # Path relative to your static files or media

@register.simple_tag
def get_random_unsplash_or_fallback():
    """Fetches a random image URL from Unsplash, or uses a fallback image if it fails."""
    try:
        unsplash_url = "https://unsplash.com/images"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(unsplash_url, headers=headers, timeout=5)  # Add a timeout
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        image_elements = soup.find_all('img', loading='lazy')

        if image_elements:
            image_urls = [img['src'] for img in image_elements if 'src' in img.attrs]
            if image_urls:
                random_url = random.choice(image_urls)
                logger.info(f"Successfully fetched random Unsplash image URL: {random_url}")
                return random_url
            else:
                logger.warning("No 'src' attributes found in Unsplash image elements.")
        else:
            logger.warning("No image elements with loading='lazy' found on Unsplash.")

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching Unsplash image: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred while fetching Unsplash image: {e}")

    # Fallback to the local image
    logger.info(f"Falling back to local image: {FALLBACK_IMAGE_PATH}")
    return static(FALLBACK_IMAGE_PATH)