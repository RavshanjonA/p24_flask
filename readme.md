flask db init
flask db migrate -m "initial migrate"
flask db upgrade

### 1. login qilgan paytda 3marta xato parol kirita olsin 3tadan kopayib ketsin bloklasin, Admin emailini chiqaring.
### 2. togri login parol bilan kiritilsa ham is_active bolmasa you account is blocked degan xabar chiqarisin.