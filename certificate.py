from OpenSSL import crypto

with open('cert.pem', 'rb') as cert_file:
    cert_data = cert_file.read()
    certificate = crypto.load_certificate(crypto.FILETYPE_PEM, cert_data)

print("Certificate Details:")
print(f"Subject: {certificate.get_subject()}")
print(f"Issuer: {certificate.get_issuer()}")
print(f"Serial Number: {certificate.get_serial_number()}")
print(f"Version: {certificate.get_version()}")
print(f"Not Before: {certificate.get_notBefore()}")
print(f"Not After: {certificate.get_notAfter()}")
print(f"Fingerprint: {certificate.digest('sha256')}")

public_key = certificate.get_pubkey()
print("\nPublic Key Details:")
print(f"Type: {public_key.type()}")
print(f"Bits: {public_key.bits()}")
