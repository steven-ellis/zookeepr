from zkpylons.tests.model import *

class TestPaymentReceivedTable(TableTest):
    table = model.billing.tables.payment_received
    samples = [dict(InvoiceID=1000,
                    AuthNum='5260',
                    Amount=69000,
                    RefundKey='KJdW+tSk95x+d54+gHB0',
                    MerchantID='Test',
                    Status='Accepted',
                    Settlement=1110,
                    ErrorString='a',
                    CardName='b',
                    RequestedPage='ReceiptPage',
                    CardType='MASTERCARD',
                    MAC='0cf459a485261747bb565ec47ec434ee6fdba0fe',
                    CardNumber='51000...0008',
                    PaymentID=200,
                    TransID='SimProxy 54021549',
                    ORIGINAL_AMOUNT=69000,
                    Surcharge=0),
               dict(InvoiceID=1001,
                    AuthNum='5261',
                    Amount=69001,
                    RefundKey='KJdW+tSk95x+d54+gHB1',
                    MerchantID='Test1',
                    Status='Denied',
                    Settlement=1111,
                    ErrorString='x',
                    CardName='y',
                    RequestedPage='ReceiptPage1',
                    CardType='VISA',
                    MAC='0cf459a485261747bb565ec47ec434ee6fdbasdf',
                    CardNumber='51000...0009',
                    PaymentID=201,
                    TransID='SimProxy 54021550',
                    ORIGINAL_AMOUNT=69001,
                    Surcharge=1),
               ]