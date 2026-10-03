import requests
from bs4 import BeautifulSoup

# Funtion to read from Google Doc url
def print_secret_message(url):
    response = requests.get(url)
    response.raise_for_status()


    # parse data
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if not table:
        return

    # Get coordinates and data
    grid_data = {}
    max_x = 0
    max_y = 0
    rows = table.find_all("tr")
    for row in rows[1:]:  # Skip the header row
        cells = row.find_all(["td", "th"])
        if len(cells) < 3:
            continue

        # Typically the columns are: x-coordinate, Unicode character, y-coordinate
        # Or: x-coordinate, y-coordinate, Unicode character
        # We parse ints safely to determine column mapping
        col0 = cells[0].get_text(strip=True)
        col1 = cells[1].get_text(strip=True)
        col2 = cells[2].get_text(strip=True)

        try:
            x = int(col0)
            char = col1
            y = int(col2)
        except ValueError:
            # Fallback if the table schema has character in col2 and y in col1
            try:
                x = int(col0)
                y = int(col1)
                char = col2
            except ValueError:
                continue

        grid_data[(x, y)] = char
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    # Note: Standard Cartesian coordinates place (0,0) at the bottom-left.
    # If the letters appear upside-down, change range(max_y, -1, -1) to range(max_y + 1).
    for y in range(max_y, -1, -1):
        line = [grid_data.get((x, y), " ") for x in range(max_x + 1)]
        print("".join(line))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        doc_url = sys.argv[1]
    else:
        doc_url = input("Enter Google Doc URL: ").strip()
    if doc_url:
        print_secret_message(doc_url)

