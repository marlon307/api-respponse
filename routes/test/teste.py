from fastapi import APIRouter
import mercadopago
import os

router = APIRouter(tags=["TESTE"])
testeeee = {
    "id": 1311088498,
    "date_created": "2022-12-31T09: 52: 32.081-04: 00",
    "date_approved": None,
    "date_last_updated": "2022-12-31T09: 52: 32.081-04: 00",
    "date_of_expiration": "2023-01-01T09: 52: 31.732-04: 00",
    "money_release_date": None,
    "money_release_status": None,
    "operation_type": "regular_payment",
    "issuer_id": None,
    "payment_method_id": "pix",
    "payment_type_id": "bank_transfer",
    "payment_method": {"id": "pix", "type": "bank_transfer"},
    "status": "pending",
    "status_detail": "pending_waiting_transfer",
    "currency_id": "BRL",
    "description": "Pedido #145",
    "live_mode": False,
    "sponsor_id": None,
    "authorization_code": None,
    "money_release_schema": None,
    "taxes_amount": 0,
    "counter_currency": None,
    "brand_id": None,
    "shipping_amount": 0,
    "build_version": "2.125.0",
    "pos_id": None,
    "store_id": None,
    "integrator_id": None,
    "platform_id": None,
    "corporation_id": None,
    "collector_id": 118098077,
    "payer": {
        "first_name": None,
        "last_name": None,
        "email": "test_user_80507629@testuser.com",
        "identification": {"number": "32659430", "type": "DNI"},
        "phone": {"area_code": None, "number": None, "extension": None},
        "type": None,
        "entity_type": None,
        "id": "1201321128",
    },
    "marketplace_owner": None,
    "metadata": {},
    "additional_info": {
        "available_balance": None,
        "nsu_processadora": None,
        "authentication_code": None,
    },
    "order": {},
    "external_reference": None,
    "transaction_amount": 234,
    "transaction_amount_refunded": 0,
    "coupon_amount": 0,
    "differential_pricing_id": None,
    "financing_group": None,
    "deduction_schema": None,
    "callback_url": None,
    "installments": 1,
    "transaction_details": {
        "payment_method_reference_id": None,
        "net_received_amount": 0,
        "total_paid_amount": 234,
        "overpaid_amount": 0,
        "external_resource_url": None,
        "installment_amount": 0,
        "financial_institution": None,
        "payable_deferral_period": None,
        "acquirer_reference": None,
        "bank_transfer_id": None,
        "transaction_id": None,
    },
    "fee_details": [],
    "charges_details": [],
    "captured": True,
    "binary_mode": False,
    "call_for_authorize_id": None,
    "statement_descriptor": None,
    "card": {},
    "notification_url": None,
    "refunds": [],
    "processing_mode": "aggregator",
    "merchant_account_id": None,
    "merchant_number": None,
    "acquirer_reconciliation": [],
    "point_of_interaction": {
        "type": "OPENPLATFORM",
        "business_info": {"unit": "online_payments", "sub_unit": "sdk"},
        "location": {"state_id": None, "source": None},
        "application_data": {"name": None, "version": None},
        "transaction_data": {
            "qr_code": "00020126580014br.gov.bcb.pix0136b76aa9c2-2ec4-4110-954e-ebfe34f05b615204000053039865406234.005802BR5910Sultrax1086006recife62230519mpqrinter131108849863043090",
            "bank_transfer_id": None,
            "transaction_id": None,
            "e2e_id": None,
            "financial_institution": None,
            "ticket_url": "https: //www.mercadopago.com.br/sandbox/payments/1311088498/ticket?caller_id=1201321128&hash=5075e943-6484-4b09-bd1b-64ef4ceb1793",
            "bank_info": {
                "payer": {
                    "account_id": None,
                    "id": None,
                    "long_name": None,
                    "external_account_id": None,
                },
                "collector": {
                    "account_id": None,
                    "long_name": None,
                    "account_holder_name": "zBCfpF dcGeyDOq lplNs",
                    "transfer_account_id": None,
                },
                "is_same_bank_account_owner": None,
                "origin_bank_id": None,
                "origin_wallet_id": None,
            },
            "qr_code_base64": "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",
        },
    },
}


@router.post("/teste")
def rota_para_teste_rapido(data: dict):

    payment = testeeee
    # process_payment(data_json["method_pay"], order[0])
    order = {"number_order": 232}
    new_dict = {
        "number_order": order["number_order"],
        "date_of_expiration": payment["date_of_expiration"],
        "qr_code": payment["point_of_interaction"]["transaction_data"]["qr_code"],
        "qr_code_base64": payment["point_of_interaction"]["transaction_data"][
            "qr_code_base64"
        ],
    }
    return new_dict
    # sdk = mercadopago.SDK(os.getenv("MP_ACCESS_TOKEN"))

    # payment_data = {
    #     "transaction_amount": 100,
    #     "description": "Título do produto",
    #     "payment_method_id": "pix",
    #     "payer": {
    #         "email": "test@test.com",
    #         "first_name": "Test",
    #         "last_name": "User",
    #         "identification": {
    #             "type": "CPF",
    #             "number": "19119119100",
    #         },
    #         "address": {
    #             "zip_code": "06233-200",
    #             "street_name": "Av. das Nações Unidas",
    #             "street_number": "3003",
    #             "neighborhood": "Bonfim",
    #             "city": "Osasco",
    #             "federal_unit": "SP",
    #         },
    #     },
    # }
    # token = sdk.card_token()
    # print(str(token))

    # payment_data = {
    #     "transaction_amount": 150,
    #     "token": "visa",
    #     "description": "Título do produto",
    #     "installments": 1,
    #     "payment_method_id": "visa",
    #     "payer": {
    #         "email": "email@email.com",
    #         "identification": {
    #             "type": "CPF",
    #             "number": "19119119100",
    #         },
    #     },
    # }

    # payment_response = sdk.payment().create(payment_data)
    # payment = payment_response["response"]
