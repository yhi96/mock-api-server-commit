import json

with open('tests/config.json', 'r') as file:
    config = json.load(file)

use_https = config["use_https"]
cert_path = config["https_cert"] if use_https else None

# URL за HTTP или HTTPS в зависимост от конфигурацията
url = "https://localhost:8443/" if use_https else "http://localhost:8080/"

# Изключваме проверката за сертификата, когато е HTTPS
verify = False if use_https else True

print(f"Config loaded: use_https={use_https}, cert_path={cert_path}, url={url}, verify={verify}")