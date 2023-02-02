class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


object_1 = BlogPost('Maikl', 'laiks', 500)
object_2 = BlogPost('Nik', 'laiks', 500)

object_2.number_of_likes = 600

print(object_1.number_of_likes)
print(object_2.number_of_likes)

