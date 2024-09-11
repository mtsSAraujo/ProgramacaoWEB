import json
from bson import ObjectId  # Certifique-se de que o pymongo está instalado
from datetime import datetime

# Define os canais e transações
channels = [
    "com.picpay",
    "business.app",
    "goldengate.admin.web",
    "goldengate.portal.industrial",
    "picpay.ib.web"
]

transactions = [f"loan_{str(i).zfill(3)}" for i in range(1, 101)]

integrations = []

# Gera as integrações
for channel in channels:
    for transaction in transactions:
        integration = {
            "_id": {"$oid": str(ObjectId())},  # Gera um novo ObjectId único
            "channel": channel,
            "product": "loan",
            "transaction": transaction,
            "active": True,
            "params": {},
            "workflowAnalyze": "wf-analyze-transaction",
            "workflowAuthenticate": "wf-authenticate-transaction",
            "authenticationMethods": [
                "SMS",
                "EMAIL",
                "TOKEN_PICPAY",
                "WHATSAPP"
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
                "version": 1,
                "status": "CREATED",
                "mode": "RELEASED",
                "user": "system@picpay.com",
                "createdAt": {"$date": datetime.now().isoformat() + "Z"}
            }
        }
        integrations.append(integration)

# Exporta para um arquivo JSON
with open("integrations.json", "w", encoding="utf-8") as f:
    json.dump(integrations, f, indent=2, ensure_ascii=False)
