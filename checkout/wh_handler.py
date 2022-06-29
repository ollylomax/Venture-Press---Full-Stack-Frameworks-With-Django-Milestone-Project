from django.http import HttpResponse


class main_handler:
    """Handler for stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def generic_handler(self, event):
        """
        Handler for a undefined webhook event
        """
        return HttpResponse(
            content=f'Undefined webhook: {event["type"]}',
            status=200)

    def pi_succeeded_handler(self, event):
        """
        Stripe payment_intent.succeeded webhook handler
        """
        return HttpResponse(
            content=f'Webhook: {event["type"]}',
            status=200)

    def pi_payment_failed_handler(self, event):
        """
        Stripe payment_intent.payment_failed webhook handler
        """
        return HttpResponse(
            content=f'Webhook: {event["type"]}',
            status=200)