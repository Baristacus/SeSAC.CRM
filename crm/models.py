from crm import db


class User(db.Model):
    Id = db.Column(db.Text, primary_key=True)
    Name = db.Column(db.Text, nullable=False)
    Gender = db.Column(db.Text, nullable=False)
    Birthday = db.Column(db.Text, nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Address = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<User {self.Name}>"


class Store(db.Model):
    Id = db.Column(db.Text, primary_key=True)
    Name = db.Column(db.Text, nullable=False)
    Type = db.Column(db.Text, nullable=False)
    Address = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Store {self.Name}>"


class Item(db.Model):
    Id = db.Column(db.Text, primary_key=True)
    Type = db.Column(db.Text, nullable=False)
    Name = db.Column(db.Text, nullable=False)
    UnitPrice = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Item {self.Name}>"


class Order(db.Model):
    Id = db.Column(db.Text, primary_key=True)
    OrderAt = db.Column(db.Text, nullable=False)
    StoreId = db.Column(db.Text, nullable=False)
    UserId = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Order {self.Id}>"


class OrderItem(db.Model):
    __tablename__ = "OrderItem"
    Id = db.Column(db.Text, primary_key=True)
    OrderId = db.Column(db.Text, nullable=False)
    ItemId = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<OrderItem {self.Id}>"
