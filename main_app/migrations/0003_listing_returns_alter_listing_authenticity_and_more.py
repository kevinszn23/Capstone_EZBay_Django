# Generated by Django 4.1.2 on 2022-10-11 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_listing_bio_listing_authenticity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='returns',
            field=models.CharField(default='This item is final sale and cannot be returned', max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='authenticity',
            field=models.TextField(default='This item is verified by professionally trained authenticators before delivery', max_length=500),
        ),
        migrations.AlterField(
            model_name='listing',
            name='condition',
            field=models.CharField(default='Pre-owned', max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='delivery',
            field=models.CharField(default='Estimated between Thu, Oct 20 and Tue, Oct 25 to 02171', max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='img',
            field=models.CharField(default='https://i.ebayimg.com/images/g/vToAAOSwNPti-wZp/s-l500.jpg', max_length=500),
        ),
        migrations.AlterField(
            model_name='listing',
            name='money_back',
            field=models.TextField(default='Get the item you ordered or get your money back.', max_length=500),
        ),
        migrations.AlterField(
            model_name='listing',
            name='name',
            field=models.CharField(default='Nike Stussy Spiridon Fossil', max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='payments',
            field=models.CharField(default='PayPal, Google Pay, Visa, Mastercard, American Express, Discover', max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.CharField(default='US $300.00', max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='seller_information',
            field=models.TextField(default='codingconnoseiur23 (999 ✭), 99.3% Positive feedback', max_length=500),
        ),
        migrations.AlterField(
            model_name='listing',
            name='shipping_details',
            field=models.CharField(default='US $13.00, Secure delivery with tracking, Located in: Jersey City, New Jersey, United States', max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='ships_from',
            field=models.CharField(default='Ships from United States', max_length=100),
        ),
    ]
