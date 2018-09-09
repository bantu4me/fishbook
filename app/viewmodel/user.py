from app.model.user import User


class PersonView:
    def __init__(self, user: User):
        self.nickname = user.nickname
        send_receive = str(user.send_counter) + '/' + str(user.receive_counter)
        self.send_receive = send_receive
        self.beans = user.beans
        self.email = user.email
