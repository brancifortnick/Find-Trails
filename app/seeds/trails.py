from app.models import db, Trail


def seed_trails():
    """Seed trails for all 50 US states based on Good_Trails data"""
    trails_data = [
        {'name': 'Delta Marsh Walk', 'description': "A serene hike through Alabama's winding bayous, where cypress trees tower over still waters and herons skim across the surface.", 'length': 8, 'difficulty': 3, 'state_id': 1, 'cross_state': False},
        {'name': 'Denali Tundra Loop', 'description': "Alaska's rugged tundra tests hikers with unmarked paths, sudden elevation, and moose sightings that feel all too close.", 'length': 12, 'difficulty': 7, 'state_id': 2, 'cross_state': False},
        {'name': 'Canyon Cradle Trail', 'description': "Twisting through Arizona's deep red slot canyons, this trail is a sun-baked journey into ancient stone corridors.", 'length': 9, 'difficulty': 5, 'state_id': 3, 'cross_state': False},
        {'name': 'Ozark River Bend', 'description': "Arkansas's flowing waters and wooded valleys create a peaceful, low-impact path ideal for beginners.", 'length': 6, 'difficulty': 2, 'state_id': 4, 'cross_state': False},
        {'name': 'Sierra Summit Trail', 'description': "Scaling California's towering peaks, this challenging trek rewards with views of alpine lakes and endless skies.", 'length': 14, 'difficulty': 8, 'state_id': 5, 'cross_state': False},
        {'name': 'Rocky Divide Trail', 'description': 'Above tree line and full of alpine drama, this Colorado climb will leave you breathless—literally and figuratively.', 'length': 13, 'difficulty': 8, 'state_id': 6, 'cross_state': False},
        {'name': 'Pine Grove Ramble', 'description': "Connecticut's gentle forests offer a welcoming escape for new hikers and nature lovers alike.", 'length': 5, 'difficulty': 2, 'state_id': 7, 'cross_state': False},
        {'name': 'Cape Henlopen Dunes Trail', 'description': "Rolling dunes and salty breezes define this coastal hike in Delaware. Don't forget your sunscreen.", 'length': 4, 'difficulty': 1, 'state_id': 8, 'cross_state': False},
        {'name': 'Everglades Edge Walk', 'description': "Boardwalks and swamp trails let you safely glimpse Florida's wildest side—gators and all.", 'length': 7, 'difficulty': 3, 'state_id': 9, 'cross_state': False},
        {'name': 'Blue Ridge Summit Trail', 'description': "Georgia's slice of the Blue Ridge Mountains is full of switchbacks, meadows, and sweeping southern skies.", 'length': 9, 'difficulty': 5, 'state_id': 10, 'cross_state': True},
        {'name': 'Volcanic Crater Rim Trail', 'description': 'Lava fields and blackened craters shape this surreal trek in Hawaii Volcanoes National Park. Bring layers—the weather flips fast.', 'length': 6, 'difficulty': 4, 'state_id': 11, 'cross_state': False},
        {'name': 'Sawtooth Traverse', 'description': "Idaho's jagged peaks make for technical climbs and icy lakes nestled between stone spires. Rugged and remote.", 'length': 15, 'difficulty': 7, 'state_id': 12, 'cross_state': False},
        {'name': 'Shawnee Wilderness Trail', 'description': "Illinois' hidden forest gem meanders past sandstone cliffs and seasonal waterfalls. Quiet, wild, and full of surprises.", 'length': 10, 'difficulty': 4, 'state_id': 13, 'cross_state': False},
        {'name': 'Hoosier Highlands Path', 'description': "A rolling hike through Indiana's forested southern hills. Steep hollows meet breezy ridgelines.", 'length': 8, 'difficulty': 3, 'state_id': 14, 'cross_state': False},
        {'name': 'Flint Hills Prairie Trail', 'description': 'Open skies and endless grasses define this Kansas trail. An unbroken sea of green stretches to every horizon.', 'length': 14, 'difficulty': 3, 'state_id': 15, 'cross_state': False},
        {'name': 'Red River Gorge Crest', 'description': 'Natural rock bridges and cliffside trails define this favorite Kentucky hike through Daniel Boone National Forest.', 'length': 9, 'difficulty': 5, 'state_id': 16, 'cross_state': False},
        {'name': 'Cajun Swamp Trek', 'description': "Moss-laced bayous and alligator trails wind through Louisiana's Atchafalaya Basin. Bring bug spray and steady boots.", 'length': 7, 'difficulty': 4, 'state_id': 17, 'cross_state': False},
        {'name': 'Acadia Ridge Trail', 'description': "Maine's granite peaks meet cold Atlantic air in this stunning oceanside trek through Acadia National Park.", 'length': 11, 'difficulty': 6, 'state_id': 18, 'cross_state': False},
        {'name': 'Appalachian Foothills Walk', 'description': "Maryland's mountainous west offers an intro to the Appalachian Trail, complete with river valleys and mountain laurel.", 'length': 6, 'difficulty': 3, 'state_id': 19, 'cross_state': True},
        {'name': 'Mount Greylock Ascent', 'description': 'The highest point in Massachusetts reveals panoramic rewards at the summit, especially during fall foliage.', 'length': 9, 'difficulty': 5, 'state_id': 20, 'cross_state': False},
        {'name': 'Porcupine Mountain Loop', 'description': 'A deep forest trail in Michigan with crashing waterfalls, wild blueberries, and views over Lake Superior.', 'length': 13, 'difficulty': 6, 'state_id': 21, 'cross_state': False},
        {'name': 'North Shore Ridge Trail', 'description': "Minnesota's rocky highlands and coldwater lakes make this hike both scenic and invigorating.", 'length': 10, 'difficulty': 5, 'state_id': 22, 'cross_state': False},
        {'name': 'Natchez Trace Backwoods Trail', 'description': 'This Mississippi trail delves deep into pine groves and historic Native American footpaths.', 'length': 7, 'difficulty': 4, 'state_id': 23, 'cross_state': False},
        {'name': 'Ozark Overlook Trail', 'description': "Missouri's rolling hills and limestone bluffs offer rewarding views for a moderate forest trek.", 'length': 8, 'difficulty': 5, 'state_id': 24, 'cross_state': False},
        {'name': 'Big Sky Highlands Trail', 'description': 'Windswept peaks and glacier-fed lakes make this Montana route unforgettable. Expect solitude—and grizzlies.', 'length': 15, 'difficulty': 7, 'state_id': 25, 'cross_state': False},
        {'name': 'Sandhills Prairie Path', 'description': "Nebraska's grass dunes stretch for miles in this surprisingly serene and scenic walk under vast skies.", 'length': 10, 'difficulty': 2, 'state_id': 26, 'cross_state': False},
        {'name': 'Valley of Fire Summit Route', 'description': "Crimson peaks and slot canyons define this otherworldly desert scramble in Nevada's oldest state park.", 'length': 6, 'difficulty': 6, 'state_id': 27, 'cross_state': False},
        {'name': 'White Mountains Ridge Trail', 'description': "New Hampshire's granite ridges test your endurance, especially with unpredictable weather blowing through.", 'length': 12, 'difficulty': 7, 'state_id': 28, 'cross_state': False},
        {'name': 'Pinelands Deepwoods Loop', 'description': "New Jersey's Pine Barrens are thick, sandy, and full of mystery—perfect for a quiet, immersive hike.", 'length': 8, 'difficulty': 3, 'state_id': 29, 'cross_state': False},
        {'name': 'Bandelier Mesa Traverse', 'description': "Ancient cliff dwellings and volcanic terrain define this stunning hike through northern New Mexico's mesa country.", 'length': 10, 'difficulty': 5, 'state_id': 30, 'cross_state': False},
    ]

    for trail_data in trails_data:
        trail = Trail(**trail_data)
        db.session.add(trail)

    db.session.commit()


def undo_trails():
    db.session.execute('TRUNCATE trails RESTART IDENTITY CASCADE;')
    db.session.commit()
