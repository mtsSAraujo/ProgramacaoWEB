import json
import uuid  # Usar UUID para gerar IDs únicos
from datetime import datetime
import os

# Define os canais e transações
channels = [
    "com.picpay",
    "business.app",
    "goldengate.admin.web",
    "goldengate.portal.industrial",
    "picpay.ib.web"
]

# Define os produtos
products = [
    "student_loan"
]

# Gera as transações
def generate_transactions(product_code):
    return [f"{product_code}_{str(i).zfill(3)}" for i in range(1, 101)]

# Gera as integrações para cada produto e canal
def generate_integrations(product_code):
    integrations = []
    transactions = generate_transactions(product_code)
    
    for channel in channels:
        for transaction in transactions:
            integration = {
                "_id": {"$oid": uuid.uuid4().hex[:24]},  # Usando UUID para gerar IDs únicos
                "channel": channel,
                "product": product_code,
                "transaction": transaction,
                "active": True,
                "params": {},
                "workflowAnalyze": "wf-analyze-transaction",
                "workflowAuthenticate": "wf-authenticate-transaction",
                "authenticationMethods": [
                    "SMS", "EMAIL", "TOKEN_PICPAY", "WHATSAPP"
                ],
                "signatureFields": ["user.userId"],
                "authenticationChallengeRules": [
                    "rule-challenge-all-methods",
                    "rule-challenge-3-methods",
                    "rule-challenge-sms-email",
                    "rule-challenge-whatsapp",
                    "rule-challenge-token",
                    "rule-challenge-sms",
                    "rule-challenge-email"
                ],
                "versioningDetails": {
                    "version": 2,
                    "status": "UPDATED",
                    "mode": "RELEASED",
                    "user": "system2@picpay.com",
                    "createdAt": {"$date": datetime.now().isoformat() + "Z"}
                }
            }
            integrations.append(integration)
    
    return integrations

# Define o caminho base
base_path = r"C:\Users\mateus.araujo\Downloads\integrationsTeste"

# Certifica-se que o caminho existe
if not os.path.exists(base_path):
    os.makedirs(base_path)

# Gera 10 JSONs diferentes para cada produto
for product in products:
    integrations = generate_integrations(product)
    file_path = os.path.join(base_path, f"{product}_integrations_corrected_version2.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(integrations, f, indent=2, ensure_ascii=False)

file_path