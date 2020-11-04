from petdacorgo import db
from petdacorgo.models import User, Pet
from datetime import datetime

db.create_all()

Katrina = User(
    username='Katrina',
    email='kat.kopio@gmail.com',
    password='password',
    contact_num = "09171234567"
)

db.session.add(Katrina)

Piccolo = Pet(
    petname = "Piccolo",
    fullname = "Piccolo",
    profile_picture = "piccolo.jpg",
    birthday = datetime(2014,10,20),
    weight = "10 lbs",
    info = "Piccolo is a chubby and fluffy cat. She loves food, especially wet food. If you feed her, she may even love you a bit more than airconditioned rooms. She doesn't like loud noises (they startle her), or having her belly poked (even if she shows it off all the time)",
    photo1 = "piccolo_g1.jpg", 
    photo2 = "piccolo_g2.jpg", 
    photo3 = "piccolo_g3.jpg",
    photo4 = "piccolo_g4.jpg",
    photo5 = "piccolo_g5.jpg",
    pet_type = "cat",
    owner = Katrina
)

Oreo = Pet(
    petname = "Oreo",
    fullname = "Oreo McFurry",
    profile_picture = "oreo.jpg",
    birthday = datetime(2010,4,24),
    weight = "6 lbs",
    info = "Old man Oreo enjoys sleeping. In fact, he'll fall asleep almost anywhere! However, his favorite sleeping spot? Your hair. Beware, because Oreo loves to drool. Note as well, that he favors men, over women",
    photo1 = "oreo_g1.jpg", 
    photo2 = "oreo_g2.jpg", 
    photo3 = "oreo_g3.jpg",
    photo4 = "oreo_g4.JPG",
    photo5 = "oreo_g5.jpg",
    pet_type = "cat",
    owner = Katrina
)

Zula = Pet(
    petname = "Zula",
    fullname = "Zula",
    profile_picture = "zula.jpg",
    birthday = datetime(2016,11,27),
    weight = "11 lbs",
    info = "Zula is often described by her friends as a big plush stuffed toy. This is because Zula barely moves. Her routine consists of waking up, staying in bed, not moving until meal time, then heading back to bed. Don't be fooled by her calm demeanour. This cat is dramatic, and throws tantrums when she is being ignored. She also hates Truffles.",
    photo1 = "zula_g1.jpg", 
    photo2 = "zula_g2.jpg", 
    photo3 = "zula_g3.jpg",
    photo4 = "zula_g4.jpg",
    photo5 = "zula_g5.jpg",
    pet_type = "cat",
    owner = Katrina
)

Truffles = Pet(
    petname = "Truffles",
    fullname = "Truffles",
    profile_picture = "truffles.jpg",
    birthday = datetime(2019,6,26),
    weight = "5 lbs",
    info = "Truffles is the baby of the bunch. She is happy as long as she's with you (she does love her belly rubs and snuggles though). Her bestfriend is Piccolo, but they only chat when the topic is food. She doesn't like Zula very much, or getting bullied, or getting bullied by Zula.",
    photo1 = "truffles_g1.jpg", 
    photo2 = "truffles_g2.jpg", 
    photo3 = "truffles_g3.jpg",
    photo4 = "truffles_g4.jpg", 
    photo5 = "truffles_g5.jpg",
    pet_type = "cat",
    owner = Katrina
)

Edgrr = Pet(
    petname = "Edgrr",
    fullname = "Edgrr Felixmenio",
    profile_picture = "edgrr.jpg",
    birthday = datetime(2013,1,8),
    weight = "20 lbs",
    info = "Edgrr is a misunderstood dog. Though he looks like he's constantly judging you, that's actually just his RJF (resting judging face). He like browsing memes with you, especially if they're about him or other Shibes.",
    photo1 = "edgrr_g1.png", 
    photo2 = "edgrr_g2.jpeg", 
    photo3 = "edgrr_g3.jpg",
    photo4 = "edgrr_g4.jpg", 
    photo5 = "edgrr_g5.jpg",
    pet_type = "dog",
    owner = Katrina
)

Hugo = Pet(
    petname = "Hugo",
    fullname = "Hugo",
    profile_picture = "hugo.jpg",
    birthday = datetime(2011,2,6),
    weight = "25 lbs",
    info = "Don't be fooled by Hugo's fearsome face: all he wants is some belly rubs and bacon treats. He enjoys plopping on the floor, and people watching. He gets very jealous though when you hang out with other dogs.",
    photo1 = "hugo_g1.jpg", 
    photo2 = "hugo_g2.jpg", 
    photo3 = "hugo_g3.jpg",
    photo4 = "hugo_g4.jpg", 
    photo5 = "hugo_g5.jpg",
    pet_type = "dog",
    owner = Katrina
)

Coco = Pet(
    petname = "Coco",
    fullname = "Coco",
    profile_picture = "coco.jpg",
    birthday = datetime(2013,7,20),
    weight = "20 lbs",
    info = "The smartest among his brothers, Coco loves ear scratches, belly rubs and hugs. He loves Hugo the most in the world, and running around with him. He tries to get along with Perry, but they just end up hating each other.",
    photo1 = "coco_g1.jpg", 
    photo2 = "coco_g2.jpeg", 
    photo3 = "coco_g3.JPG",
    photo4 = "coco_g4.JPG", 
    photo5 = "coco_g5.JPG",
    pet_type = "dog",
    owner = Katrina
)

Perry = Pet(
    petname = "Perry",
    fullname = "Perry",
    profile_picture = "perry.jpg",
    birthday = datetime(2018,12,15),
    weight = "17 lbs",
    info = "Perry loves attention. Take him to the mall, and he just soaks up all the coos and squeals from his fans. He likes to sploot on the floor, imitating a bread loaf, and loves it when you pet him. Don't believe his kind demeanour though: he hates Coco and Hugo. He just feels like he shouldn't have to share your love, I guess.",
    photo1 = "perry_g1.jpg", 
    photo2 = "perry_g2.jpg", 
    photo3 = "perry_g3.jpg",
    photo4 = "perry_g4.jpg", 
    photo5 = "perry_g5.jpg",
    pet_type = "dog",
    owner = Katrina
)

pets = [Piccolo, Oreo, Zula, Truffles, Hugo, Coco, Perry, Edgrr]
for pet in pets:
    db.session.add(pet)

db.session.commit()