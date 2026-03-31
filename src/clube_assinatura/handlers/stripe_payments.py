async def handle_payment_succeeded(self, invoice):
    if not invoice.get("subscription"):
        return  
            