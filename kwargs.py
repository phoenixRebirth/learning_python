class File:
    def __init__(self, owner, path):
        self.path = path
        self.owner = owner

    def open(self):
        print("file "+self.path+" bien ouvert!")

class Advertisement(File):

    def open(self, **kwargs):
        File.open(self)

# class SecretFile(File):
#
#     def open(self, staff):
#         if staff == self.owner:
#             File.open(self)
#         else:
#             print("interdit")

class SecretFile(File):

    def open(self, **kwargs):
        if kwargs.get('staff', None) == self.owner:
            File.open(self)
        else:
            print(kwargs)
            print("interdit")


# if kwargs.get('staff', None) == self.owner:

staff1 = "roger"
staff2 = "marguerite"
adv_file = Advertisement(staff2, "adv.txt")
secret_file = SecretFile(staff1, "secret.txt")

# adv_file.open()
# secret_file.open(staff2)
list_files = [adv_file, secret_file]
for elt in list_files:
    elt.open(staff=staff2)

# staff=staff2
