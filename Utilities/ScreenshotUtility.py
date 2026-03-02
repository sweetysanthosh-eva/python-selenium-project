import os

def capture_screenshot(item, file_path):
    """
    Captures and saves a screenshot using the driver found in 'item'.
    Returns the file path if successful, else None.
    """
    driver = None
    if hasattr(item, 'funcargs') and 'browserinstance' in item.funcargs:
        driver = item.funcargs['browserinstance']

    if driver:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure directory exists
        driver.save_screenshot(file_path)
        print(f"[Screenshot] Saved to: {file_path}")
        return file_path
    else:
        print("[Screenshot] Driver not found; skipping screenshot.")
        return None