flask db init
flask db migrate -m "initial migrate"
flask db upgrade

### 1. User bloglar bomasi h3"You don't have any blogs"
### 2. User boshqa userlarni bloglarini korolmasin @access decorator yarating