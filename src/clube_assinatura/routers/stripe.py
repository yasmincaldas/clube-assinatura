import stripe
from clube_assinatura.settings import Settings


router = APIRouter(prefix="/webhooks", tags=["webhooks"])
settings = Settings()


@app.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.stripe_webhook_secret
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event['type'] == 'invoice.payment_succeeded':
        invoice = event['data']['object']
        handle_invoice_paid(invoice)

    return {"status": "success"}