from django.contrib.auth.hashers import make_password
from datetime import datetime
from .models import User, Images, Projects, Orders, Team, Telegram

def create_sample_data():
    # Create Users
    for i in range(1, 11):
        User.objects.create_user(
            username=f'user{i}',
            full_name=f'User {i}',
            position=f'Position {i}',
            skills=f'Skill {i}',
            password=make_password(f'password{i}'),
            status='FREE',
            contacts=f'Contact {i}',
            education=f'Education {i}',
            accepted=True if i % 2 == 0 else False
        )

    # Create Images
    for i in range(1, 11):
        Images.objects.create(image=f'image{i}.jpg')

    # Create Projects
    for i in range(1, 11):
        project = Projects.objects.create(
            type=f'Project type {i}',
            name=f'Project {i}',
            contacts=f'Contacts {i}',
            desc=f'Description {i}',
            desc_to_workers=f'Description to workers {i}',
            price=1000 * i,
            status='STARTED' if i % 2 == 0 else 'INPROGRESS',
            paid_money=500 * i,
        )
        project.images.add(Images.objects.get(pk=i))

    # Create Orders
    for i in range(1, 11):
        Orders.objects.create(
            order_name=f'Order {i}',
            desc=f'Description {i}',
            contacts=f'Contacts {i}',
            major=f'Major {i}',
            address=f'Address {i}',
            organisation=f'Organisation {i}'
        )

    # Create Teams
    for i in range(1, 11):
        team_lead = User.objects.get(username=f'user{i}')
        project = Projects.objects.get(name=f'Project {i}')
        team = Team.objects.create(
            team_lead=team_lead,
            project_id=project,
            summa=10000 * i,
            paid_money=5000 * i,
            telegram_group=f'Telegram Group {i}'
        )
        for j in range(1, 6):
            team.workers_id.add(User.objects.get(username=f'user{j}'))

    # Create Telegram
    Telegram.objects.create(
        apiToken='YourApiToken',
        chatID='YourChatID'
    )

# Call the function to create sample data when needed
create_sample_data()
