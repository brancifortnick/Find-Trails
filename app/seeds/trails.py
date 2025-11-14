from app.models import db, Trail
from sqlalchemy import text


# Adds trails for all 50 US states based on Good_Trails data
def seed_trails():
    trails_data = [
        # States 1-10
        {'name': 'Delta Marsh Walk', 'description': "A serene hike through Alabama's winding bayous, where cypress trees tower over still waters and herons skim across the surface.", 'length': 8, 'difficulty': 3, 'elevation_gain': 420, 'state_id': 1, 'cross_state': False},
        {'name': 'Denali Tundra Loop', 'description': "Alaska's rugged tundra tests hikers with unmarked paths, sudden elevation, and moose sightings that feel all too close.", 'length': 12, 'difficulty': 7, 'elevation_gain': 2850, 'state_id': 2, 'cross_state': False},
        {'name': 'Canyon Cradle Trail', 'description': "Twisting through Arizona's deep red slot canyons, this trail is a sun-baked journey into ancient stone corridors.", 'length': 9, 'difficulty': 5, 'elevation_gain': 1640, 'state_id': 3, 'cross_state': False},
        {'name': 'Ozark Highland Passage', 'description': "This steep, forest-lined path through Arkansas is one of the wildest stretches of the Ozarks. Waterfalls await.", 'length': 11, 'difficulty': 6, 'elevation_gain': 1920, 'state_id': 4, 'cross_state': False},
        {'name': 'Sequoia Crest Trek', 'description': "Massive trees, misty mountain passes, and jaw-dropping views make this one of California's crown jewels.", 'length': 16, 'difficulty': 6, 'elevation_gain': 3640, 'state_id': 5, 'cross_state': False},
        {'name': 'Rocky Divide Trail', 'description': 'Above tree line and full of alpine drama, this Colorado climb will leave you breathless—literally and figuratively.', 'length': 13, 'difficulty': 8, 'elevation_gain': 3180, 'state_id': 6, 'cross_state': False},
        {'name': 'Pine Grove Ramble', 'description': "Connecticut's gentle forests offer a welcoming escape for new hikers and nature lovers alike.", 'length': 5, 'difficulty': 2, 'elevation_gain': 280, 'state_id': 7, 'cross_state': False},
        {'name': 'Cape Henlopen Dunes Trail', 'description': "Rolling dunes and salty breezes define this coastal hike in Delaware. Don't forget your sunscreen.", 'length': 4, 'difficulty': 1, 'elevation_gain': 120, 'state_id': 8, 'cross_state': False},
        {'name': 'Everglades Edge Walk', 'description': "Boardwalks and swamp trails let you safely glimpse Florida's wildest side—gators and all.", 'length': 7, 'difficulty': 3, 'elevation_gain': 180, 'state_id': 9, 'cross_state': False},
        {'name': 'Blue Ridge Summit Trail', 'description': "Georgia's slice of the Blue Ridge Mountains is full of switchbacks, meadows, and sweeping southern skies.", 'length': 9, 'difficulty': 5, 'elevation_gain': 1820, 'state_id': 10, 'cross_state': True},
        # States 11-20
        {'name': 'Volcanic Crater Rim Trail', 'description': 'Lava fields and blackened craters shape this surreal trek in Hawaii Volcanoes National Park. Bring layers—the weather flips fast.', 'length': 6, 'difficulty': 4, 'elevation_gain': 980, 'state_id': 11, 'cross_state': False},
        {'name': 'Sawtooth Traverse', 'description': "Idaho's jagged peaks make for technical climbs and icy lakes nestled between stone spires. Rugged and remote.", 'length': 15, 'difficulty': 7, 'elevation_gain': 2940, 'state_id': 12, 'cross_state': False},
        {'name': 'Shawnee Wilderness Trail', 'description': "Illinois' hidden forest gem meanders past sandstone cliffs and seasonal waterfalls. Quiet, wild, and full of surprises.", 'length': 10, 'difficulty': 4, 'elevation_gain': 840, 'state_id': 13, 'cross_state': False},
        {'name': 'Hoosier Highlands Path', 'description': "A rolling hike through Indiana's forested southern hills. Steep hollows meet breezy ridgelines.", 'length': 8, 'difficulty': 3, 'elevation_gain': 620, 'state_id': 14, 'cross_state': False},
        {'name': 'Loess Hills Ridge', 'description': "Iowa's unique windblown hills create a rolling landscape. Rare geology meets prairie skies.", 'length': 9, 'difficulty': 4, 'elevation_gain': 740, 'state_id': 15, 'cross_state': False},
        {'name': 'Flint Hills Prairie Trail', 'description': 'Open skies and endless grasses define this Kansas trail. An unbroken sea of green stretches to every horizon.', 'length': 14, 'difficulty': 3, 'elevation_gain': 520, 'state_id': 16, 'cross_state': False},
        {'name': 'Red River Gorge Crest', 'description': 'Natural rock bridges and cliffside trails define this favorite Kentucky hike through Daniel Boone National Forest.', 'length': 9, 'difficulty': 5, 'elevation_gain': 1460, 'state_id': 17, 'cross_state': False},
        {'name': 'Cajun Swamp Trek', 'description': "Moss-laced bayous and alligator trails wind through Louisiana's Atchafalaya Basin. Bring bug spray and steady boots.", 'length': 7, 'difficulty': 4, 'elevation_gain': 240, 'state_id': 18, 'cross_state': False},
        {'name': 'Acadia Ridge Trail', 'description': "Maine's granite peaks meet cold Atlantic air in this stunning oceanside trek through Acadia National Park.", 'length': 11, 'difficulty': 6, 'elevation_gain': 2120, 'state_id': 19, 'cross_state': False},
        {'name': 'Appalachian Foothills Walk', 'description': "Maryland's mountainous west offers an intro to the Appalachian Trail, complete with river valleys and mountain laurel.", 'length': 6, 'difficulty': 3, 'elevation_gain': 780, 'state_id': 20, 'cross_state': True},
        # States 21-30
        {'name': 'Mount Greylock Ascent', 'description': 'The highest point in Massachusetts reveals panoramic rewards at the summit, especially during fall foliage.', 'length': 9, 'difficulty': 5, 'elevation_gain': 1650, 'state_id': 21, 'cross_state': False},
        {'name': 'Porcupine Mountain Loop', 'description': 'A deep forest trail in Michigan with crashing waterfalls, wild blueberries, and views over Lake Superior.', 'length': 13, 'difficulty': 6, 'elevation_gain': 2280, 'state_id': 22, 'cross_state': False},
        {'name': 'North Shore Ridge Trail', 'description': "Minnesota's rocky highlands and coldwater lakes make this hike both scenic and invigorating.", 'length': 10, 'difficulty': 5, 'elevation_gain': 1540, 'state_id': 23, 'cross_state': False},
        {'name': 'Natchez Trace Backwoods Trail', 'description': 'This Mississippi trail delves deep into pine groves and historic Native American footpaths.', 'length': 7, 'difficulty': 4, 'elevation_gain': 680, 'state_id': 24, 'cross_state': False},
        {'name': 'Ozark Overlook Trail', 'description': "Missouri's rolling hills and limestone bluffs offer rewarding views for a moderate forest trek.", 'length': 8, 'difficulty': 5, 'elevation_gain': 1120, 'state_id': 25, 'cross_state': False},
        {'name': 'Big Sky Highlands Trail', 'description': 'Windswept peaks and glacier-fed lakes make this Montana route unforgettable. Expect solitude—and grizzlies.', 'length': 15, 'difficulty': 7, 'elevation_gain': 3050, 'state_id': 26, 'cross_state': False},
        {'name': 'Sandhills Prairie Path', 'description': "Nebraska's grass dunes stretch for miles in this surprisingly serene and scenic walk under vast skies.", 'length': 10, 'difficulty': 2, 'elevation_gain': 380, 'state_id': 27, 'cross_state': False},
        {'name': 'Valley of Fire Summit Route', 'description': "Crimson peaks and slot canyons define this otherworldly desert scramble in Nevada's oldest state park.", 'length': 6, 'difficulty': 6, 'elevation_gain': 1580, 'state_id': 28, 'cross_state': False},
        {'name': 'White Mountains Ridge Trail', 'description': "New Hampshire's granite ridges test your endurance, especially with unpredictable weather blowing through.", 'length': 12, 'difficulty': 7, 'elevation_gain': 2750, 'state_id': 29, 'cross_state': False},
        {'name': 'Pinelands Deepwoods Loop', 'description': "New Jersey's Pine Barrens are thick, sandy, and full of mystery—perfect for a quiet, immersive hike.", 'length': 8, 'difficulty': 3, 'elevation_gain': 420, 'state_id': 30, 'cross_state': False},
        # States 31-40
        {'name': 'Bandelier Mesa Traverse', 'description': "Ancient cliff dwellings and volcanic terrain define this stunning hike through northern New Mexico's mesa country.", 'length': 10, 'difficulty': 5, 'elevation_gain': 1340, 'state_id': 31, 'cross_state': False},
        {'name': 'Adirondack High Peaks', 'description': "New York's wilderness challenges with rocky scrambles and alpine lakes tucked between towering summits.", 'length': 14, 'difficulty': 7, 'elevation_gain': 2890, 'state_id': 32, 'cross_state': False},
        {'name': 'Outer Banks Coastal Walk', 'description': "North Carolina's windswept dunes and lighthouse views make this a unique coastal adventure.", 'length': 8, 'difficulty': 2, 'elevation_gain': 150, 'state_id': 33, 'cross_state': False},
        {'name': 'Badlands Butte Trail', 'description': "North Dakota's stark beauty unfolds across eroded peaks and bison-dotted grasslands.", 'length': 7, 'difficulty': 4, 'elevation_gain': 820, 'state_id': 34, 'cross_state': False},
        {'name': 'Hocking Hills Gorge', 'description': "Ohio's sandstone caves and waterfalls create a magical forest trek through deep hollows.", 'length': 9, 'difficulty': 4, 'elevation_gain': 760, 'state_id': 35, 'cross_state': False},
        {'name': 'Wichita Mountain Ridge', 'description': "Oklahoma's ancient granite domes rise above prairie and lakes in this rugged southern climb.", 'length': 8, 'difficulty': 5, 'elevation_gain': 1180, 'state_id': 36, 'cross_state': False},
        {'name': 'Columbia Gorge Passage', 'description': "Oregon's waterfalls cascade through moss-draped forests in one of the Pacific Northwest's most iconic hikes.", 'length': 12, 'difficulty': 6, 'elevation_gain': 2340, 'state_id': 37, 'cross_state': False},
        {'name': 'Allegheny Ridge Trail', 'description': "Pennsylvania's rolling highlands wind past historic sites and hardwood forests in the heart of Appalachia.", 'length': 10, 'difficulty': 5, 'elevation_gain': 1420, 'state_id': 38, 'cross_state': False},
        {'name': 'Newport Cliff Walk', 'description': "Rhode Island's mansion-lined coast offers a unique blend of natural beauty and Gilded Age grandeur.", 'length': 3, 'difficulty': 1, 'elevation_gain': 80, 'state_id': 39, 'cross_state': False},
        {'name': 'Congaree Swamp Boardwalk', 'description': "South Carolina's old-growth forest floats you through towering cypresses and still, dark waters.", 'length': 6, 'difficulty': 2, 'elevation_gain': 50, 'state_id': 40, 'cross_state': False},
        # States 41-50
        {'name': 'Black Hills Summit', 'description': "South Dakota's granite spires pierce the sky in this challenging mountain trek near Mount Rushmore.", 'length': 11, 'difficulty': 6, 'elevation_gain': 2150, 'state_id': 41, 'cross_state': False},
        {'name': 'Smoky Mountain Crest', 'description': "Tennessee's misty peaks host ancient forests and panoramic vistas along the Appalachian spine.", 'length': 13, 'difficulty': 7, 'elevation_gain': 2680, 'state_id': 42, 'cross_state': False},
        {'name': 'Big Bend Canyon Trail', 'description': "Texas's desert wilderness carves through limestone cliffs above the Rio Grande's dramatic bends.", 'length': 11, 'difficulty': 6, 'elevation_gain': 1840, 'state_id': 43, 'cross_state': False},
        {'name': 'Zion Narrows Wade', 'description': "Utah's slot canyon river hike immerses you in towering red walls and flowing waters.", 'length': 9, 'difficulty': 6, 'elevation_gain': 720, 'state_id': 44, 'cross_state': False},
        {'name': 'Long Trail Summit', 'description': "Vermont's ridge walk showcases fall colors and mountain views across the Green Mountains.", 'length': 10, 'difficulty': 5, 'elevation_gain': 1580, 'state_id': 45, 'cross_state': False},
        {'name': 'Shenandoah Skyline', 'description': "Virginia's Blue Ridge vistas unfold along meadows and forests in this classic Appalachian trail.", 'length': 12, 'difficulty': 5, 'elevation_gain': 1920, 'state_id': 46, 'cross_state': False},
        {'name': 'Olympic Rainforest Loop', 'description': "Washington's temperate rainforest drips with moss and ferns beneath towering evergreens.", 'length': 14, 'difficulty': 6, 'elevation_gain': 2180, 'state_id': 47, 'cross_state': False},
        {'name': 'New River Gorge Trail', 'description': "West Virginia's ancient river canyon drops dramatically through whitewater and Appalachian forests.", 'length': 8, 'difficulty': 5, 'elevation_gain': 1380, 'state_id': 48, 'cross_state': False},
        {'name': 'Ice Age Trail Segment', 'description': "Wisconsin's glacial landscape winds through kettle lakes and prairie remnants from the last ice age.", 'length': 11, 'difficulty': 4, 'elevation_gain': 920, 'state_id': 49, 'cross_state': False},
        {'name': 'Grand Teton Climb', 'description': "Wyoming's iconic peaks tower above alpine meadows in one of America's most dramatic mountain landscapes.", 'length': 16, 'difficulty': 8, 'elevation_gain': 4120, 'state_id': 50, 'cross_state': False},
    ]

    for trail_data in trails_data:
        trail = Trail(**trail_data)
        db.session.add(trail)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the trails table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_trails():
    db.session.execute(text('TRUNCATE trails RESTART IDENTITY CASCADE;'))
    db.session.commit()
