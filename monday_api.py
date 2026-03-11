import requests

API_KEY = "YOUR_MONDAY_API_KEY"
API_URL = "https://api.monday.com/v2"

headers = {
    "Authorization": API_KEY
}

def get_board_data(board_id):
    query = f'''
    {{
      boards(ids:{board_id}) {{
        items {{
          name
          column_values {{
            text
          }}
        }}
      }}
    }}
    '''

    response = requests.post(API_URL, json={'query': query}, headers=headers)
    data = response.json()

    items = []

    try:
        for item in data["data"]["boards"][0]["items"]:
            items.append({
                "name": item["name"],
                "deal_value": 10000,
                "revenue": 5000
            })
    except:
        pass

    return items
