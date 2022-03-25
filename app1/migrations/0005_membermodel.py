# Generated by Django 2.1.4 on 2019-02-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20190202_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberModel',
            fields=[
                ('member_name', models.CharField(max_length=50)),
                ('member_id', models.IntegerField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('mobile_num', models.IntegerField(max_length=10)),
                ('email_id', models.EmailField(max_length=200)),
                ('address', models.TextField()),
            ],
        ),
    ]
