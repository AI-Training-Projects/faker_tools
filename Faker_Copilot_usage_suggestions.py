★ IntelliCode API Usage Examples
Thoughts?  Take our Survey!
Derived from 41 examples found on GitHub
Real World Examples of faker.Faker.name()
Grouped by signature:

name()

★ IntelliCode API Usage Examples
Thoughts?  Take our Survey!
Derived from 41 examples found on GitHub
Real World Examples of faker.Faker.name()
Grouped by signature:

name()




Page 1 of 9

 
def populate(self, number=20):

        names = []
        for _ in range(0, number):
            n = fake.name()
            names.append(n)

        return names
 PacktPublishing/Mastering-Python-Design-Patterns-S...
 
def test_create_me_unauthorized(client):
    new_thought = {
        'username': fake.name(),
        'text': fake.text(240),
    }
    response = client.post('/api/me/thoughts/', data=new_thought)
    assert http.client.UNAUTHORIZED == response.status_code
 PacktPublishing/Hands-On-Docker-for-Microservices-...
 
def make_data(self, user_count):
        f = faker.Faker()
        users = []

        for i in range(user_count):
            user, addr = self.make_user(f.name(), f.address())
            users.append(user)

        self.session.add_all(users)
        self.session.commit()
 orf/datatables/test_basic.py
 
★ IntelliCode API Usage Examples
Thoughts?  Take our Survey!
Derived from 41 examples found on GitHub
Real World Examples of faker.Faker.name()
Grouped by signature:

name()




Page 2 of 9

 
def generate_quote_field():
    quote = f'<p>{fake.sentence()}</p>'
    attribution = fake.name()
    attribution_info = f'<p>{fake.sentence()} <a href="{fake.url(schemes=["https"])}">{fake.sentence()}</a></p>'

    return generate_field('single_quote', {
        'quote': quote,
        'attribution': attribution,
        'attribution_info': attribution_info,
    })
 mozilla/foundation.mozilla.org/streamfield_provide...
 
def generate_users(n):
    users = list()
    for i in range(n):
        user = User()
        user.username = faker.name()
        user.password = "password"
        users.append(user)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            log.error("Fail to add user %s: %s" % (str(user), e))
            db.session.rollback()
    return users
 PacktPublishing/Mastering-Flask-Web-Development-Se...
 
def generate_users(n):
    users = list()
    for i in range(n):
        user = User()
        user.username = faker.name()
        user.password = "password"
        try:
            db.session.add(user)
            db.session.commit()
            users.append(user)
        except Exception as e:
            log.error("Fail to add user %s: %s" % (str(user), e))
            db.session.rollback()
    return users
 PacktPublishing/Mastering-Flask-Web-Development-Se...
 
Page 3 of 9

 
def obj(data=None, object_id=True):
        # type: (Optional[dict], Optional[bool, str, int]) -> dict

        fake = Faker()

        data = {} if data is None else data

        data["name"] = fake.name()

        if isinstance(object_id, bool):
            if object_id:
                data["objectID"] = fake.md5()
        elif isinstance(object_id, (str, int)):
            data["objectID"] = object_id

        return data
 algolia/algoliasearch-client-python/factory.py
 
def create_fake_users(n):
    """Generate fake users."""
    faker = Faker()
    for i in range(n):
        user = User(name=faker.name(),
                    age=random.randint(20, 80),
                    address=faker.address().replace('\n', ', '),
                    phone=faker.phone_number(),
                    email=faker.email())
        db.session.add(user)
    db.session.commit()
    print(f'Added {n} fake users to the database.')
 miguelgrinberg/flask-tables/create_fake_users.py
 
def test_create_user(client):
    new_user = {
        'username': fake.name(),
        'password': fake.password(length=15, special_chars=True),
    }
    response = client.post('/admin/users/', data=new_user)
    result = response.json

    assert http.client.CREATED == response.status_code

    expected = {
        'id': ANY,
        'username': new_user['username'],
        'creation': '2019-05-07T13:47:34',
    }
    assert result == expected
 PacktPublishing/Hands-On-Docker-for-Microservices-...★ IntelliCode API Usage Examples


Page 3 of 9

 
def obj(data=None, object_id=True):
        # type: (Optional[dict], Optional[bool, str, int]) -> dict

        fake = Faker()

        data = {} if data is None else data

        data["name"] = fake.name()

        if isinstance(object_id, bool):
            if object_id:
                data["objectID"] = fake.md5()
        elif isinstance(object_id, (str, int)):
            data["objectID"] = object_id

        return data
 algolia/algoliasearch-client-python/factory.py
 
def create_fake_users(n):
    """Generate fake users."""
    faker = Faker()
    for i in range(n):
        user = User(name=faker.name(),
                    age=random.randint(20, 80),
                    address=faker.address().replace('\n', ', '),
                    phone=faker.phone_number(),
                    email=faker.email())
        db.session.add(user)
    db.session.commit()
    print(f'Added {n} fake users to the database.')
 miguelgrinberg/flask-tables/create_fake_users.py
 
def test_create_user(client):
    new_user = {
        'username': fake.name(),
        'password': fake.password(length=15, special_chars=True),
    }
    response = client.post('/admin/users/', data=new_user)
    result = response.json

    assert http.client.CREATED == response.status_code

    expected = {
        'id': ANY,
        'username': new_user['username'],
        'creation': '2019-05-07T13:47:34',
    }
    assert result == expected
 PacktPublishing/Hands-On-Docker-for-Microservices-...
 
 
 ★ IntelliCode API Usage Examples
Thoughts?  Take our Survey!
Derived from 41 examples found on GitHub
Real World Examples of faker.Faker.name()
Grouped by signature:

name()




Page 4 of 9

 
def populate(session):
    """Create 3 adresses and 50 users."""
    users = []
    f = faker.Faker(seed=1)
    addresses = [Address(description=d) for d in ["Street", "Avenue", "Road"]]
    session.add_all(addresses)

    for i, addr in zip(range(0, 50), itertools.cycle(addresses)):
        user = User(
            name=f.name(),
            address=addr,
            birthday=datetime(1970, 1, 2) + timedelta(days=10 * i),
        )
        users.append(user)

    session.add_all(users)
    session.commit()
 Pegase745/sqlalchemy-datatables/conftest.py
 
def test_login(client):
    USERNAME = fake.name()
    PASSWORD = fake.password(length=15, special_chars=True)
    new_user = {
        'username': USERNAME,
        'password': PASSWORD,
    }
    response = client.post('/admin/users/', data=new_user)
    assert http.client.CREATED == response.status_code

    response = client.post('/api/login/', data=new_user)
    result = response.json
    assert http.client.OK == response.status_code

    expected = {
        'Authorized': ANY,
    }
    assert result == expected
 PacktPublishing/Hands-On-Docker-for-Microservices-...
 
def users(count=100):
    fake = Faker()
    i = 0
    while i < count:
        u = User(email=fake.email(),
                 username=fake.user_name(),
                 password='password',
                 confirmed=True,
                 name=fake.name(),
                 location=fake.city(),
                 about_me=fake.text(),
                 member_since=fake.past_date())
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()
 miguelgrinberg/flasky/fake.py
 
 ★ IntelliCode API Usage Examples
Thoughts?  Take our Survey!
Derived from 41 examples found on GitHub
Real World Examples of faker.Faker.name()
Grouped by signature:

name()




Page 5 of 9

 
def handle(self, *args, **options):
        from faker import Faker
        fake = Faker()
        transaction = Transactions.objects.create(sender=fake.name(), receiver=fake.name(), amount=fake.numerify())

        transactions = Transactions.objects.latest('id')
        transactions.added_to_block = True
        transactions.save()
        transactions.__dict__.pop("added_to_block", 0)
        transactions.__dict__.pop("_state", 0)
        peer = Peer.objects.order_by('-id')[0]
        peer.mine_block('second',  str(transactions.__dict__))
        peer.synchronize('second')
 sayonetech/django-blockchain/create_transaction.py
 
def test_rancher_parse_members_from_project():
    names = [fake.name(), fake.name()]
    members = uut.parse_members_from_project(
        {
            "id": "p2",
            "members": [
                {
                    "type": "projectMember",
                    "externalId": f"cn={names[0]},ou=People,dc=example,dc=com",
                    "role": "owner",
                },
                {
                    "type": "projectMember",
                    "externalId": f"cn={names[1]},ou=People,dc=example,dc=com",
                    "role": "owner",
                },
            ],
        }
    )
    assert members == names
 kiwicom/the-zoo/test_rancher.py
 
def test_create_me_thought(client):
    new_thought = {
        'username': fake.name(),
        'text': fake.text(240),
    }
    header = token_validation.generate_token_header(fake.name(),
                                                    PRIVATE_KEY)
    headers = {
        'Authorization': header,
    }
    response = client.post('/api/me/thoughts/', data=new_thought,
                           headers=headers)
    result = response.json

    assert http.client.CREATED == response.status_code

    expected = {
        'id': ANY,
        'username': ANY,
        'text': new_thought['text'],
        'timestamp': '2019-05-07T13:47:34',
    }
    assert result == expected
 PacktPublishing/Hands-On-Docker-for-Microservices-...
 
 
 ★ IntelliCode API Usage Examples
Thoughts?  Take our Survey!
Derived from 41 examples found on GitHub
Real World Examples of faker.Faker.name()
Grouped by signature:

name()




Page 6 of 9

 
def _generate_feed(atom=False):
    link = fake.url()
    feed = {
        "title": fake.sentence(),
        "link": link,
        "description": fake.sentence(),
    }
    optional = {
        "language": fake.locale(),
        "author_email": fake.email(),
        "author_name": fake.name(),
        "author_link": fake.url(),
        "subtitle": fake.sentence(),
        "categories": fake.pylist(nb_elements=5, value_types=[fake.word]),
        "feed_url": fake.url(),
        "feed_copyright": fake.sentence(),
        "id": link if atom else fake.uuid4(),
        "ttl": fake.pyint(),
    }
    feed.update([(k, v) for (k, v) in optional.items() if fake.pybool()])
    return feed
 recursecenter/blaggregator/utils.py
 
def run_fake_cards(table_name):
    fake = Faker()
    dynamo = boto3.resource('dynamodb')
    pci_table = dynamo.Table(table_name)

    for i in range(0, 50):
        name = fake.name()
        try:
            pci_table.put_item(Item = {
                'card_number': fake.credit_card_number(card_type=None),
                'full_name': name,
                'cvv': fake.credit_card_security_code(card_type=None),
                'expiration': fake.credit_card_expire(start = "now", end = "+5y", date_format="%m/%y")
            })
            print(good("Successfully generated card number for {}".format(name)))
            sleep(1)
        except Exception as e:
            print(bad(str(e)))
 we45/DVFaaS-Damn-Vulnerable-Functions-as-a-Service...
 
def _generate_item(atom=False):
    link = fake.url()
    item = {
        "title": fake.sentence(),
        "link": link,
        "description": fake.sentence(),
    }
    optional = {
        "content": fake.paragraph(),
        "author_email": fake.email(),
        "author_name": fake.name(),
        "author_link": fake.url(),
        "pubdate": fake.date_time(),
        "updateddate": fake.date_time(),
        "unique_id": link if atom else fake.uuid4(),
        "categories": fake.pylist(nb_elements=5, value_types=[fake.word]),
        "item_copyright": fake.sentence(),
        "ttl": fake.pyint(),
    }
    item.update([(k, v) for (k, v) in optional.items() if fake.pybool()])
    return item
 recursecenter/blaggregator/utils.py
 
 
 ★ IntelliCode API Usage Examples
Thoughts?  Take our Survey!
Derived from 41 examples found on GitHub
Real World Examples of faker.Faker.name()
Grouped by signature:

name()




Page 7 of 9

 
def test_create_circle(self):
        """
        should be able to create a circle and return 201
        """
        user = make_user()

        auth_token = user.auth_token.key

        circle_name = fake.name()
        circle_color = fake.hex_color()

        headers = {'HTTP_AUTHORIZATION': 'Token %s' % auth_token}

        data = {
            'name': circle_name,
            'color': circle_color
        }

        url = self._get_url()

        response = self.client.put(url, data, **headers, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Circle.objects.filter(name=circle_name, color=circle_color, creator_id=user.pk).count() == 1)
 OkunaOrg/okuna-api/test_views.py
 
def get_response(self):
        return {
            "id": str(self.iid) if self.iid is not None else str(fake.pyint()),
            "shortId": f"{fake.word()}-{fake.pyint()}",
            "title": fake.sentence(),
            "culprit": fake.word(),
            "assignedTo": {
                "type": "user",
                "email": fake.email(),
                "name": fake.name(),
                "id": str(fake.pyint()),
            },
            "permalink": fake.url(),
            "count": sum(stat[1] for stat in self.issue_stats),
            "userCount": fake.pyint(),
            "firstSeen": fake.iso8601() + "Z",
            "lastSeen": fake.iso8601() + "Z",
            "stats": {"14d": self.issue_stats},
        }
 kiwicom/the-zoo/test_sentry_stats.py
 
def test_create_list(self):
        """
        should be able to create a list and return 201
        """
        user = make_user()

        auth_token = user.auth_token.key

        list_emoji = mixer.blend(Emoji)

        list_name = fake.name()
        emoji_id = list_emoji.pk

        headers = {'HTTP_AUTHORIZATION': 'Token %s' % auth_token}

        data = {
            'name': list_name,
            'emoji_id': emoji_id
        }

        url = self._get_url()

        response = self.client.put(url, data, **headers, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(List.objects.filter(name=list_name, emoji_id=emoji_id, creator_id=user.pk).count() == 1)
 OkunaOrg/okuna-api/test_views.py
 
 
 ★ IntelliCode API Usage Examples
Thoughts?  Take our Survey!
Derived from 41 examples found on GitHub
Real World Examples of faker.Faker.name()
Grouped by signature:

name()




Page 8 of 9

 
def test_cannot_update_world_circle(self):
        """
        should not be able to update own world circle and return 400
        """
        user = make_user()
        auth_token = user.auth_token.key

        headers = {'HTTP_AUTHORIZATION': 'Token %s' % auth_token}

        circle_id = Circle.get_world_circle_id()

        new_circle_name = fake.name()
        new_circle_color = fake.hex_color()

        data = {
            'name': new_circle_name,
            'color': new_circle_color
        }

        url = self._get_url(circle_id)
        response = self.client.patch(url, data, **headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(Circle.objects.filter(name=new_circle_name, id=circle_id, color=new_circle_color).count() == 0)
 OkunaOrg/okuna-api/test_views.py
 
def test_cannot_update_connections_circle(self):
        """
        should not be able to update own connections circle and return 400
        """
        user = make_user()
        auth_token = user.auth_token.key

        headers = {'HTTP_AUTHORIZATION': 'Token %s' % auth_token}

        circle_id = user.connections_circle_id

        new_circle_name = fake.name()
        new_circle_color = fake.hex_color()

        data = {
            'name': new_circle_name,
            'color': new_circle_color
        }

        url = self._get_url(circle_id)
        response = self.client.patch(url, data, **headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(Circle.objects.filter(name=new_circle_name, id=circle_id, color=new_circle_color).count() == 0)
 OkunaOrg/okuna-api/test_views.py
 
def create_demo_fixtures():
    fake = Faker()
    name = fake.name()

    # have username be demo-username, so demos-users are easy to tell
    username = 'demo-{name}'.format(name=name)
    username = slugify(username)

    # since these are demo accounts, just set the username/pass the same
    # so this is a really weird bug since you'd wonder why this would be a get_or_create
    # but faker doesn't always generate fake names in celery instances ...
    user, _ = User.objects.get_or_create(username=username)

    # create a log of this person as a demo user, otherwise we would never be able to tell if someone is a demo or not!
    _, created = DemoUserLog.objects.get_or_create(user=user)
    if not created:
        return

    fixtures_builder = DemoHistoricalDataBuilder(user, periods_back=180)
    fixtures_builder.create_historical_fixtures()
 jeffshek/betterself/tasks.py
 
 
 ★ IntelliCode API Usage Examples
Thoughts?  Take our Survey!
Derived from 41 examples found on GitHub
Real World Examples of faker.Faker.name()
Grouped by signature:

name()




Page 9 of 9

 
def generate_dear_internet_letter_field():
    author_name = fake.name()
    author_description = ''.join(
        (
            '<p>',
            f'<a href="{fake.url(schemes=["https"])}" target="_blank">{author_name}</a>',
            f' is {" ".join(fake.words(nb=15))}. {fake.sentence()}',
            '</p>',
        )
    )

    letter = f'<p>{fake.paragraph(nb_sentences=10, variable_nb_sentences=True)}</p>'

    attributes = {
        'author_name': author_name,
        'author_description': author_description,
        'letter': letter,
    }

    if random() > 0.5:
        attributes['author_photo'] = choice(Image.objects.all()).id

    if random() > 0.5:
        attributes['image'] = choice(Image.objects.all()).id

    if random() > 0.5:
        attributes['video_url'] = fake.url(schemes=["https"])

    return generate_field('letter', attributes)
 mozilla/foundation.mozilla.org/streamfield_provide...
 
 