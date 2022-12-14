# Generated by Django 4.0.4 on 2022-08-09 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=128, unique=True)),
                ('bank_add', models.TextField(max_length=256, unique=True)),
                ('bank_email', models.EmailField(max_length=254)),
                ('bank_phone', models.CharField(max_length=10)),
                ('Remarks', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name_plural': 'bank details',
            },
        ),
        migrations.CreateModel(
            name='DonationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_type', models.CharField(max_length=16, unique=True)),
                ('Remarks', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name_plural': 'donations type',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=40, unique=True)),
                ('Remarks', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name_plural': 'event types',
            },
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_type', models.CharField(max_length=16, unique=True)),
                ('Remarks', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('household', models.CharField(max_length=64, unique=True)),
                ('Remarks', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name_plural': 'households',
            },
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ministry', models.CharField(choices=[('AD', 'Adult'), ('YT', 'Youth'), ('YA', 'Young_Adults'), ('CH', 'Children'), ('OT', 'Other')], default='AD', max_length=2)),
                ('Remarks', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name_plural': 'ministries',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=32, unique=True)),
                ('Remarks', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name_plural': 'roles',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=50, verbose_name='project')),
                ('project_fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChurchM.fund', verbose_name='Fund committed')),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128)),
                ('middlename', models.CharField(max_length=128)),
                ('lastname', models.CharField(blank=True, max_length=128)),
                ('sex', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('email', models.CharField(blank=True, max_length=60)),
                ('house_address', models.TextField(blank=True, max_length=256)),
                ('remarks', models.CharField(blank=True, max_length=256)),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChurchM.household')),
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChurchM.ministry')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChurchM.role')),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateTimeField(auto_now_add=True)),
                ('event_time_start', models.TimeField()),
                ('event_end_time', models.TimeField()),
                ('Remarks', models.CharField(blank=True, max_length=256)),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChurchM.eventtype')),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='BibleReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bible_text', models.CharField(max_length=80)),
                ('Remarks', models.CharField(blank=True, max_length=256)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChurchM.event')),
            ],
            options={
                'verbose_name_plural': 'bible readings',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult_male', models.IntegerField(blank=True)),
                ('adult_female', models.IntegerField(blank=True)),
                ('youth_male', models.IntegerField(blank=True)),
                ('youth_female', models.IntegerField(blank=True)),
                ('young_adults_male', models.IntegerField(blank=True)),
                ('young_adults_female', models.IntegerField(blank=True)),
                ('children', models.IntegerField(blank=True)),
                ('total_male', models.IntegerField(default=0)),
                ('total_female', models.IntegerField(default=0)),
                ('total_attendance', models.IntegerField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChurchM.event')),
            ],
            options={
                'verbose_name_plural': 'attendance',
            },
        ),
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.PositiveIntegerField(unique=True)),
                ('account_sort_code', models.PositiveIntegerField()),
                ('account_balance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Remarks', models.CharField(blank=True, max_length=256)),
                ('bank_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ChurchM.bankdetails')),
            ],
            options={
                'verbose_name_plural': 'account details',
            },
        ),
    ]
