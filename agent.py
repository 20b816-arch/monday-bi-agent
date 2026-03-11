from monday_api import get_board_data

def ask_agent(question):
    actions = []
    
    question = question.lower()

    if "deal" in question or "pipeline" in question:
        actions.append("Fetching Deals board from Monday.com API")
        data = get_board_data("DEALS_BOARD_ID")

        actions.append("Analyzing deals data")
        total_value = sum(item.get("deal_value", 0) for item in data)

        answer = f"Total pipeline deal value is: ${total_value}"
        return answer, actions

    elif "work" in question or "revenue" in question:
        actions.append("Fetching Work Orders board from Monday.com API")
        data = get_board_data("WORK_BOARD_ID")

        actions.append("Calculating total revenue")
        revenue = sum(item.get("revenue", 0) for item in data)

        answer = f"Total revenue from work orders: ${revenue}"
        return answer, actions

    else:
        return "I could not understand the question.", ["No matching analysis rule"]
