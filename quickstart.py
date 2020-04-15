""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import random

# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# login credentials


comments = [
    u'What an amazing shot @{}! :heart_eyes: What do '
    u'you think of my recent shot?',
    u'What an amazing shot! :heart_eyes: I think '
    u'you might also like mine. :wink:',
    u'Wonderful!! :heart_eyes: Would be awesome if '
    u'you would checkout my photos as well!',
    u'Wonderful!! :heart_eyes: I would be honored '
    u'if you would checkout my images and tell me '
    u'what you think. :wink:',
    u'This is awesome!! :heart_eyes: Any feedback '
    u'for my photos? :wink:',
    u'This is awesome !! :heart_eyes:  maybe you will '
    u'like my photos, too? :wink:',
    u'I really like the way you captured this. I '
    u'bet you like my photos, too :wink:',
    u'I really like the way you captured this. If '
    u'you have time, check out my photos, too. I '
    u'bet you will like them. :wink:',
    u'Great capture!! :smiley: Any feedback for my '
    u'recent shot? :wink:',
    u'Great capture!! :smiley: :thumbsup: What do '
    u'you think of my recent photo?',
    u'Great capture!! :smiley: :thumbsup: What camera and lense did you use?',
    u'Great capture!! :smiley: :thumbsup: i think you will also like my pictures :wink:',
]

dont_likes = ['sex', 'nude', 'naked', 'beef', 'pork', 'seafood',
              'egg', 'chicken', 'cheese', 'sausage', 'lobster',
              'fisch', 'schwein', 'lamm', 'rind', 'kuh', 'meeresfrüchte',
              'schaf', 'ziege', 'hummer', 'yoghurt', 'joghurt', 'dairy',
              'meal', 'food', 'eat', 'pancake', 'cake', 'dessert',
              'protein', 'essen', 'mahl', 'breakfast', 'lunch',
              'dinner', 'turkey', 'truthahn', 'plate', 'bacon',
              'sushi', 'burger', 'salmon', 'shrimp', 'steak',
              'schnitzel', 'goat', 'oxtail', 'mayo', 'fur', 'leather',
              'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy',
              'breakfast', 'dinner', 'lunch']

hashtags = ['travelcommunity', 'passionpassport',
            'backpackerlife', 'travelguide', 'travelbloggers',
            'travelblog', 'letsgoeverywhere',
            'travelislife', 'stayandwander', 'beautifuldestinations',
            'moodygrams', 'travelingram', 'hiking', 'nature',
            'ourplanetdaily', 'travelyoga', 'travelgram', 'sunsetporn',
            'igtravel', 'instapassport', 'travelling', 'instatraveling',
            'mytravelgram', 'skyporn', 'traveler', 'sunrise',
            'sunsetlovers', 'travelblog', 'nsfw',
            'sunset_pics', 'visiting', 'ilovetravel',
            'photographyoftheday', 'sunsetphotography',
            'explorenature', 'landscapeporn', 'exploring_shotz',
            'landscapehunter', 'colors_of_day',
            'earthfocus', 'ig_shotz', 'ig_nature', 'discoverearth',
            'thegreatoutdoors']
random.shuffle(hashtags)
my_hashtags = hashtags[:10]

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_do_like(enabled=True, percentage=100)
    session.set_do_comment(enabled=True, percentage=25)
    session.set_comments(comments)
    session.set_user_interact(amount=6, randomize=False, percentage=100)

    session.set_skip_users(skip_private=True,
                           private_percentage=100,
                           skip_no_profile_pic=True,
                           no_profile_pic_percentage=100,
                           skip_business=False,
                           skip_non_business=False,
                           business_percentage=10,
                           skip_business_categories=[],
                           dont_skip_business_categories=[])

    session.set_delimit_liking(enabled=True, max_likes=350, min_likes=None)
    session.set_delimit_commenting(enabled=True, max_comments=32, min_comments=None)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=-1.25,
                                    delimit_by_numbers=True,
                                    max_followers=5000,
                                    max_following=None,
                                    min_followers=10,
                                    min_following=20,
                                    min_posts=1,
                                    max_posts=3000)

    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                                 peak_likes_hourly=47,
                                 peak_likes_daily=585,
                                 peak_comments_hourly=21,
                                 peak_comments_daily=182,
                                 peak_follows_hourly=48,
                                 peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4700)

    # activity
    session.set_dont_like(dont_likes)
    session.like_by_tags(my_hashtags, amount=50, interact=True)

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='travel', engagement_mode='no_comments')

