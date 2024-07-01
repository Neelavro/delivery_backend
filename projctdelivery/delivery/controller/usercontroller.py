from delivery.models import User


def createUser():
    u1 = User(name = 'test', email = 'test@gmail.com', password= '1234')

    u1.save()

def getUser(uid):
    u1 = User.objects.get(id = uid)
    #print(u1.name)
    u1.save()
    print(u1.name)

getUser(3)