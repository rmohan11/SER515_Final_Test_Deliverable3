# Generated by Django 2.1.1 on 2018-10-14 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookingInfo',
            fields=[
                ('booking_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.TextField(blank=True, null=True)),
                ('seats', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'booking_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('passport', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customer_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FlightDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateField(unique=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('available_bseats', models.IntegerField()),
                ('available_eseats', models.IntegerField()),
            ],
            options={
                'db_table': 'flight_details',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FlightInfo',
            fields=[
                ('flight_id', models.IntegerField(primary_key=True, serialize=False)),
                ('source', models.TextField()),
                ('destination', models.TextField()),
                ('departure', models.TimeField()),
                ('arrival', models.TimeField()),
                ('duration_hrs', models.FloatField(blank=True, null=True)),
                ('business_seats', models.IntegerField()),
                ('economy_seats', models.IntegerField()),
            ],
            options={
                'db_table': 'flight_info',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='flightdetails',
            name='flight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bookings.FlightInfo'),
        ),
        migrations.AddField(
            model_name='bookinginfo',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bookings.CustomerInfo'),
        ),
        migrations.AddField(
            model_name='bookinginfo',
            name='departure_date',
            field=models.ForeignKey(blank=True, db_column='departure_date', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bookings.FlightDetails'),
        ),
        migrations.AddField(
            model_name='bookinginfo',
            name='flight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bookings.FlightInfo'),
        ),
    ]
