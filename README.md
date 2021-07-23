# seed_cbc_py
KISA 128bit SEED CBC 암호화 복호화 Python 

## 참고
https://seed.kisa.or.kr/kisa/Board/17/detailView.do

https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/?highlight=seed#cryptography.hazmat.primitives.ciphers.algorithms.SEED

## 사용

s=SeedCBC('password12345678', 'iv34567890123456')

print(s.Encrypt('암호문자열'))

print(s.Decrypt('복호화 문자열(base64)'))

