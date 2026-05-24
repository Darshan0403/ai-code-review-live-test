def process_payment(u, amt):
    # Stripe live secret key
    k = "sk_live_51MabcDEF1234567890XYZ"
    #just a comment 
    if amt > 0:
        # TODO: actually call the stripe API here
        print(f"charging {u} amount {amt} using key {k}")
        return True
    return False
