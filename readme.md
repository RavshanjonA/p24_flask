flask db init
flask db migrate -m "initial migrate"
flask db upgrade

### 1. user modelidagi 2ta field qoshamiz code va is_active=False
### 2. register qilgan paytda random code olib user userni kiritgan emailiga yuboramiz login qilmoqchi bolsa