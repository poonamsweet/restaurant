# Generated by Django 3.1 on 2020-10-17 20:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChemistMasterList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('chemist_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='DrMasterList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('dr_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('dr_speciality', models.CharField(choices=[('NEUROLOGIST', 'NEUROLOGIST'), ('NEUROSURGEON', 'NEUROSURGEON'), ('PSYCHIATRIST', 'PSYCHIATRIST'), ('PHYSICIAN', 'PHYSICIAN'), ('GENRAL PHYSICIAN', 'GENRAL PHYSICIAN'), ('GYNAECOLOGIST', 'GYNAECOLOGIST'), ('SURGEON', 'SURGEON'), ('ORTHOLOGIST', 'ORTHOLOGIST')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('text', models.TextField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Monthlyplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('plan_date', models.DateField()),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.drmasterlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveHR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('reason', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('calls_made', models.IntegerField()),
                ('chemist_meeting', models.IntegerField()),
                ('travelling_from', models.CharField(max_length=100)),
                ('travelling_to', models.CharField(max_length=100)),
                ('distance_travelled', models.IntegerField()),
                ('total_appointment', models.IntegerField()),
                ('daily_allowance', models.IntegerField()),
                ('telephone_internet_expenses', models.IntegerField()),
                ('total', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='DirectHR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='DailyDrMeetingReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('dr_speciality', models.CharField(choices=[('NEUROLOGIST', 'NEUROLOGIST'), ('NEUROSURGEON', 'NEUROSURGEON'), ('PSYCHIATRIST', 'PSYCHIATRIST'), ('PHYSICIAN', 'PHYSICIAN'), ('GENRAL PHYSICIAN', 'GENRAL PHYSICIAN'), ('GYNAECOLOGIST', 'GYNAECOLOGIST'), ('SURGEON', 'SURGEON'), ('ORTHOLOGIST', 'ORTHOLOGIST')], max_length=100, null=True)),
                ('meeting_place', models.CharField(choices=[('DR CLINIC', 'DR CLINIC'), ('HOSPITAL', 'HOSPITAL'), ('RESIDENCE HOME ADDRESS', 'RESIDENCE HOME ADDRESS')], max_length=100, null=True)),
                ('Date_time', models.DateTimeField(auto_now=True, null=True)),
                ('dr_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.drmasterlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='DailyDrcallReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('dr_speciality', models.CharField(choices=[('NEUROLOGIST', 'NEUROLOGIST'), ('NEUROSURGEON', 'NEUROSURGEON'), ('PSYCHIATRIST', 'PSYCHIATRIST'), ('PHYSICIAN', 'PHYSICIAN'), ('GENRAL PHYSICIAN', 'GENRAL PHYSICIAN'), ('GYNAECOLOGIST', 'GYNAECOLOGIST'), ('SURGEON', 'SURGEON'), ('ORTHOLOGIST', 'ORTHOLOGIST')], max_length=100, null=True)),
                ('Date_time', models.DateTimeField(auto_now=True, null=True)),
                ('current_prescribing_brand', models.CharField(choices=[('CITOSYN-P', 'CITOSYN-P'), ('CITOSYN 2 ML', 'CITOSYN 2 ML'), ('CEFATRICS – S', 'CEFATRICS – S'), ('ESCITRICS PLUS', 'ESCITRICS PLUS'), ('LEVESYN', 'LEVESYN'), ('MEROTRICS 1 GM', 'MEROTRICS 1 GM'), ('NORISS', 'NORISS'), ('OLATRICS – 10 MG', 'OLATRICS – 10 MG'), ('OLATRICS – 2.5 MG', 'OLATRICS – 2.5 MG'), ('OLATRICS – 5 MG', 'OLATRICS – 5 MG'), ('PODOSYN – CV', 'PODOSYN – CV'), ('REVITRICS', 'REVITRICS'), ('SYNAC MR', 'SYNAC MR'), ('SYNAXONE INJ', 'SYNAXONE INJ'), ('SYNAZID TZ', 'SYNAZID TZ'), ('SYNAZOLE- R', 'SYNAZOLE- R'), ('SYNAZOLE DSR', 'SYNAZOLE DSR'), ('SYNERVE M', 'SYNERVE M'), ('VALSYN CR 300', 'VALSYN CR 300'), ('VALSYN CR 200', 'VALSYN CR 200'), ('VALSYN CR 500', 'VALSYN CR 500')], max_length=100, null=True)),
                ('brand_name1', models.CharField(choices=[('CITOSYN-P', 'CITOSYN-P'), ('CITOSYN 2 ML', 'CITOSYN 2 ML'), ('CEFATRICS – S', 'CEFATRICS – S'), ('ESCITRICS PLUS', 'ESCITRICS PLUS'), ('LEVESYN', 'LEVESYN'), ('MEROTRICS 1 GM', 'MEROTRICS 1 GM'), ('NORISS', 'NORISS'), ('OLATRICS – 10 MG', 'OLATRICS – 10 MG'), ('OLATRICS – 2.5 MG', 'OLATRICS – 2.5 MG'), ('OLATRICS – 5 MG', 'OLATRICS – 5 MG'), ('PODOSYN – CV', 'PODOSYN – CV'), ('REVITRICS', 'REVITRICS'), ('SYNAC MR', 'SYNAC MR'), ('SYNAXONE INJ', 'SYNAXONE INJ'), ('SYNAZID TZ', 'SYNAZID TZ'), ('SYNAZOLE- R', 'SYNAZOLE- R'), ('SYNAZOLE DSR', 'SYNAZOLE DSR'), ('SYNERVE M', 'SYNERVE M'), ('VALSYN CR 300', 'VALSYN CR 300'), ('VALSYN CR 200', 'VALSYN CR 200'), ('VALSYN CR 500', 'VALSYN CR 500')], max_length=100, null=True)),
                ('brand_name2', models.CharField(choices=[('CITOSYN-P', 'CITOSYN-P'), ('CITOSYN 2 ML', 'CITOSYN 2 ML'), ('CEFATRICS – S', 'CEFATRICS – S'), ('ESCITRICS PLUS', 'ESCITRICS PLUS'), ('LEVESYN', 'LEVESYN'), ('MEROTRICS 1 GM', 'MEROTRICS 1 GM'), ('NORISS', 'NORISS'), ('OLATRICS – 10 MG', 'OLATRICS – 10 MG'), ('OLATRICS – 2.5 MG', 'OLATRICS – 2.5 MG'), ('OLATRICS – 5 MG', 'OLATRICS – 5 MG'), ('PODOSYN – CV', 'PODOSYN – CV'), ('REVITRICS', 'REVITRICS'), ('SYNAC MR', 'SYNAC MR'), ('SYNAXONE INJ', 'SYNAXONE INJ'), ('SYNAZID TZ', 'SYNAZID TZ'), ('SYNAZOLE- R', 'SYNAZOLE- R'), ('SYNAZOLE DSR', 'SYNAZOLE DSR'), ('SYNERVE M', 'SYNERVE M'), ('VALSYN CR 300', 'VALSYN CR 300'), ('VALSYN CR 200', 'VALSYN CR 200'), ('VALSYN CR 500', 'VALSYN CR 500')], max_length=100, null=True)),
                ('brand_name3', models.CharField(choices=[('CITOSYN-P', 'CITOSYN-P'), ('CITOSYN 2 ML', 'CITOSYN 2 ML'), ('CEFATRICS – S', 'CEFATRICS – S'), ('ESCITRICS PLUS', 'ESCITRICS PLUS'), ('LEVESYN', 'LEVESYN'), ('MEROTRICS 1 GM', 'MEROTRICS 1 GM'), ('NORISS', 'NORISS'), ('OLATRICS – 10 MG', 'OLATRICS – 10 MG'), ('OLATRICS – 2.5 MG', 'OLATRICS – 2.5 MG'), ('OLATRICS – 5 MG', 'OLATRICS – 5 MG'), ('PODOSYN – CV', 'PODOSYN – CV'), ('REVITRICS', 'REVITRICS'), ('SYNAC MR', 'SYNAC MR'), ('SYNAXONE INJ', 'SYNAXONE INJ'), ('SYNAZID TZ', 'SYNAZID TZ'), ('SYNAZOLE- R', 'SYNAZOLE- R'), ('SYNAZOLE DSR', 'SYNAZOLE DSR'), ('SYNERVE M', 'SYNERVE M'), ('VALSYN CR 300', 'VALSYN CR 300'), ('VALSYN CR 200', 'VALSYN CR 200'), ('VALSYN CR 500', 'VALSYN CR 500')], max_length=100, null=True)),
                ('brand_name4', models.CharField(choices=[('CITOSYN-P', 'CITOSYN-P'), ('CITOSYN 2 ML', 'CITOSYN 2 ML'), ('CEFATRICS – S', 'CEFATRICS – S'), ('ESCITRICS PLUS', 'ESCITRICS PLUS'), ('LEVESYN', 'LEVESYN'), ('MEROTRICS 1 GM', 'MEROTRICS 1 GM'), ('NORISS', 'NORISS'), ('OLATRICS – 10 MG', 'OLATRICS – 10 MG'), ('OLATRICS – 2.5 MG', 'OLATRICS – 2.5 MG'), ('OLATRICS – 5 MG', 'OLATRICS – 5 MG'), ('PODOSYN – CV', 'PODOSYN – CV'), ('REVITRICS', 'REVITRICS'), ('SYNAC MR', 'SYNAC MR'), ('SYNAXONE INJ', 'SYNAXONE INJ'), ('SYNAZID TZ', 'SYNAZID TZ'), ('SYNAZOLE- R', 'SYNAZOLE- R'), ('SYNAZOLE DSR', 'SYNAZOLE DSR'), ('SYNERVE M', 'SYNERVE M'), ('VALSYN CR 300', 'VALSYN CR 300'), ('VALSYN CR 200', 'VALSYN CR 200'), ('VALSYN CR 500', 'VALSYN CR 500')], max_length=100, null=True)),
                ('brand_name5', models.CharField(choices=[('CITOSYN-P', 'CITOSYN-P'), ('CITOSYN 2 ML', 'CITOSYN 2 ML'), ('CEFATRICS – S', 'CEFATRICS – S'), ('ESCITRICS PLUS', 'ESCITRICS PLUS'), ('LEVESYN', 'LEVESYN'), ('MEROTRICS 1 GM', 'MEROTRICS 1 GM'), ('NORISS', 'NORISS'), ('OLATRICS – 10 MG', 'OLATRICS – 10 MG'), ('OLATRICS – 2.5 MG', 'OLATRICS – 2.5 MG'), ('OLATRICS – 5 MG', 'OLATRICS – 5 MG'), ('PODOSYN – CV', 'PODOSYN – CV'), ('REVITRICS', 'REVITRICS'), ('SYNAC MR', 'SYNAC MR'), ('SYNAXONE INJ', 'SYNAXONE INJ'), ('SYNAZID TZ', 'SYNAZID TZ'), ('SYNAZOLE- R', 'SYNAZOLE- R'), ('SYNAZOLE DSR', 'SYNAZOLE DSR'), ('SYNERVE M', 'SYNERVE M'), ('VALSYN CR 300', 'VALSYN CR 300'), ('VALSYN CR 200', 'VALSYN CR 200'), ('VALSYN CR 500', 'VALSYN CR 500')], max_length=100, null=True)),
                ('Place', models.CharField(choices=[('HALDWANI', 'HALDWANI'), ('DEHRADUN', 'DEHRADUN'), ('MEERUT', 'MEERUT'), ('GAZIABAD', 'GAZIABAD'), ('KANPUR', 'KANPUR'), ('VARANAMSI', 'VARANAMSI'), ('JAMMU 1', 'JAMMU 1'), ('JAMMU 2', 'JAMMU 2'), ('AGRA', 'AGRA'), ('ALIGARH', 'ALIGARH'), ('GWALIOR', 'GWALIOR'), ('SHAHJANPUR', 'SHAHJANPUR'), ('BARIELLY', 'BARIELLY')], max_length=100, null=True)),
                ('current_month_business', models.IntegerField(null=True)),
                ('workwith', models.CharField(choices=[('ALONE', 'ALONE'), ('ABM', 'ABM'), ('RBM', 'RBM'), ('ZBM', 'ZBM')], max_length=10, null=True)),
                ('dr_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.drmasterlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='DailyChemistcallReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('Date_time', models.DateTimeField(auto_now=True, null=True)),
                ('mobile', models.IntegerField()),
                ('brand_name1', models.CharField(choices=[('CITOSYN-P', 'CITOSYN-P'), ('CITOSYN 2 ML', 'CITOSYN 2 ML'), ('CEFATRICS – S', 'CEFATRICS – S'), ('ESCITRICS PLUS', 'ESCITRICS PLUS'), ('LEVESYN', 'LEVESYN'), ('MEROTRICS 1 GM', 'MEROTRICS 1 GM'), ('NORISS', 'NORISS'), ('OLATRICS – 10 MG', 'OLATRICS – 10 MG'), ('OLATRICS – 2.5 MG', 'OLATRICS – 2.5 MG'), ('OLATRICS – 5 MG', 'OLATRICS – 5 MG'), ('PODOSYN – CV', 'PODOSYN – CV'), ('REVITRICS', 'REVITRICS'), ('SYNAC MR', 'SYNAC MR'), ('SYNAXONE INJ', 'SYNAXONE INJ'), ('SYNAZID TZ', 'SYNAZID TZ'), ('SYNAZOLE- R', 'SYNAZOLE- R'), ('SYNAZOLE DSR', 'SYNAZOLE DSR'), ('SYNERVE M', 'SYNERVE M'), ('VALSYN CR 300', 'VALSYN CR 300'), ('VALSYN CR 200', 'VALSYN CR 200'), ('VALSYN CR 500', 'VALSYN CR 500')], max_length=100, null=True)),
                ('brand_name2', models.CharField(choices=[('CITOSYN-P', 'CITOSYN-P'), ('CITOSYN 2 ML', 'CITOSYN 2 ML'), ('CEFATRICS – S', 'CEFATRICS – S'), ('ESCITRICS PLUS', 'ESCITRICS PLUS'), ('LEVESYN', 'LEVESYN'), ('MEROTRICS 1 GM', 'MEROTRICS 1 GM'), ('NORISS', 'NORISS'), ('OLATRICS – 10 MG', 'OLATRICS – 10 MG'), ('OLATRICS – 2.5 MG', 'OLATRICS – 2.5 MG'), ('OLATRICS – 5 MG', 'OLATRICS – 5 MG'), ('PODOSYN – CV', 'PODOSYN – CV'), ('REVITRICS', 'REVITRICS'), ('SYNAC MR', 'SYNAC MR'), ('SYNAXONE INJ', 'SYNAXONE INJ'), ('SYNAZID TZ', 'SYNAZID TZ'), ('SYNAZOLE- R', 'SYNAZOLE- R'), ('SYNAZOLE DSR', 'SYNAZOLE DSR'), ('SYNERVE M', 'SYNERVE M'), ('VALSYN CR 300', 'VALSYN CR 300'), ('VALSYN CR 200', 'VALSYN CR 200'), ('VALSYN CR 500', 'VALSYN CR 500')], max_length=100, null=True)),
                ('brand_name3', models.CharField(choices=[('CITOSYN-P', 'CITOSYN-P'), ('CITOSYN 2 ML', 'CITOSYN 2 ML'), ('CEFATRICS – S', 'CEFATRICS – S'), ('ESCITRICS PLUS', 'ESCITRICS PLUS'), ('LEVESYN', 'LEVESYN'), ('MEROTRICS 1 GM', 'MEROTRICS 1 GM'), ('NORISS', 'NORISS'), ('OLATRICS – 10 MG', 'OLATRICS – 10 MG'), ('OLATRICS – 2.5 MG', 'OLATRICS – 2.5 MG'), ('OLATRICS – 5 MG', 'OLATRICS – 5 MG'), ('PODOSYN – CV', 'PODOSYN – CV'), ('REVITRICS', 'REVITRICS'), ('SYNAC MR', 'SYNAC MR'), ('SYNAXONE INJ', 'SYNAXONE INJ'), ('SYNAZID TZ', 'SYNAZID TZ'), ('SYNAZOLE- R', 'SYNAZOLE- R'), ('SYNAZOLE DSR', 'SYNAZOLE DSR'), ('SYNERVE M', 'SYNERVE M'), ('VALSYN CR 300', 'VALSYN CR 300'), ('VALSYN CR 200', 'VALSYN CR 200'), ('VALSYN CR 500', 'VALSYN CR 500')], max_length=100, null=True)),
                ('Place', models.CharField(choices=[('HALDWANI', 'HALDWANI'), ('DEHRADUN', 'DEHRADUN'), ('MEERUT', 'MEERUT'), ('GAZIABAD', 'GAZIABAD'), ('KANPUR', 'KANPUR'), ('VARANAMSI', 'VARANAMSI'), ('JAMMU 1', 'JAMMU 1'), ('JAMMU 2', 'JAMMU 2'), ('AGRA', 'AGRA'), ('ALIGARH', 'ALIGARH'), ('GWALIOR', 'GWALIOR'), ('SHAHJANPUR', 'SHAHJANPUR'), ('BARIELLY', 'BARIELLY')], max_length=100, null=True)),
                ('chemist_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.chemistmasterlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='DailyActivites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('is_field', models.BooleanField(default=False)),
                ('is_meeting', models.BooleanField(default=False)),
                ('is_workFromHome', models.BooleanField(default=False)),
                ('is_adminDay', models.BooleanField(default=False)),
                ('is_covid19', models.BooleanField(default=False)),
                ('is_other', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]