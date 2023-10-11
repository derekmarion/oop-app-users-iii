# Import and create your users here
import sys
sys.path.append('./users')
from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser

user1 = FreeUser("Jimmy", "jimmy@gimmy.com", "as;lkdjfao92wi3")
user1.add_post = "This is a blog post"
user1.add_post = "Here's another"
user1.add_post = "Third"

print(user1.get_posts)

user2 = PremiumUser("Jimmy", "jimmy@gimmy.com", "as;lkdjfao92wi3")
user2.add_post = "This is a blog post"
user2.add_post = "Here's another"
user2.add_post = "Third"

print(user2.get_posts)