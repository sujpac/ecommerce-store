# Generated by Django 2.2.19 on 2021-03-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a test description. Lorem ipsum dolor sit amet         consectetur adipisicing elit. Et dolor suscipit libero eos atque         quia ipsa sint voluptatibus! Beatae sit assumenda asperiores iure at         maxime atque repellendus maiores quia sapiente.'),
        ),
    ]