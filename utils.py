import requests
import os

def download_file(url, save_path):
    """
    Download a file from a given URL and save it to a local path.
    :param url: The URL of the file to download.
    :param save_path: The local path where the file will be saved.
    """
    # Ensure the folder exists
    folder = os.path.dirname(save_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    try:
        response = requests.get(url.strip(), stream=True)  # Stream the file
        response.raise_for_status()  # Check for HTTP errors

        # Write the file in chunks to avoid memory issues
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):  # 8 KB chunks
                file.write(chunk)
        print(f"File successfully downloaded to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")