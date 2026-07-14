tickets = {
    "INC-1001": {
        "status": "In Progress",
        "team": "Platform Engineering",
        "priority": "High"
    },
    "INC-1002": {
        "status": "Resolved",
        "team": "Database Team",
        "priority": "Medium"
    }
}


def get_ticket_status(ticket_id):

    ticket = tickets.get(ticket_id)

    if not ticket:
        return "Ticket not found"

    return (
        f"{ticket_id} status: {ticket['status']}. "
        f"Assigned team: {ticket['team']}. "
        f"Priority: {ticket['priority']}."
    )
