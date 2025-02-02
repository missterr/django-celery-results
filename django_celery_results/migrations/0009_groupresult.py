# Generated by Django 3.2 on 2021-04-19 14:55
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_results', '0008_chordcounter'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupResult',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('group_id', models.CharField(
                    help_text='Celery ID for the Group that was run',
                    max_length=getattr(
                        settings,
                        'DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH',
                        255
                    ),
                    unique=True,
                    verbose_name='Group ID')),
                ('date_created', models.DateTimeField(
                    auto_now_add=True,
                    help_text='Datetime field when the group result '
                              'was created in UTC',
                    verbose_name='Created DateTime')),
                ('date_done', models.DateTimeField(
                    auto_now=True,
                    help_text='Datetime field when the group was '
                              'completed in UTC',
                    verbose_name='Completed DateTime')),
                ('content_type', models.CharField(
                    help_text='Content type of the result data',
                    max_length=128,
                    verbose_name='Result Content Type')),
                ('content_encoding', models.CharField(
                    help_text='The encoding used to save the task '
                              'result data',
                    max_length=64,
                    verbose_name='Result Encoding')),
                ('result', models.TextField(
                    default=None,
                    editable=False,
                    help_text='The data returned by the task.  Use '
                              'content_encoding and content_type '
                              'fields to read.',
                    null=True,
                    verbose_name='Result Data')),
            ],
            options={
                'verbose_name': 'group result',
                'verbose_name_plural': 'group results',
                'ordering': ['-date_done'],
            },
        ),
        migrations.AlterField(
            model_name='chordcounter',
            name='group_id',
            field=models.CharField(
                help_text='Celery ID for the Chord header group',
                max_length=getattr(
                    settings,
                    'DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH',
                    255
                ),
                unique=True,
                verbose_name='Group ID'),
        ),
        migrations.AlterField(
            model_name='taskresult',
            name='date_created',
            field=models.DateTimeField(
                auto_now_add=True,
                help_text='Datetime field when the task result '
                          'was created in UTC',
                verbose_name='Created DateTime'),
        ),
        migrations.AlterField(
            model_name='taskresult',
            name='date_done',
            field=models.DateTimeField(
                auto_now=True,
                help_text='Datetime field when the task was completed in UTC',
                verbose_name='Completed DateTime'),
        ),
        migrations.AlterField(
            model_name='taskresult',
            name='status',
            field=models.CharField(
                choices=[
                    ('FAILURE', 'FAILURE'),
                    ('PENDING', 'PENDING'),
                    ('RECEIVED', 'RECEIVED'),
                    ('RETRY', 'RETRY'),
                    ('REVOKED', 'REVOKED'),
                    ('STARTED', 'STARTED'),
                    ('SUCCESS', 'SUCCESS')],
                default='PENDING',
                help_text='Current state of the task being run',
                max_length=50,
                verbose_name='Task State'),
        ),
        migrations.AlterField(
            model_name='taskresult',
            name='task_id',
            field=models.CharField(
                help_text='Celery ID for the Task that was run',
                max_length=getattr(
                    settings,
                    'DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH',
                    255
                ),
                unique=True,
                verbose_name='Task ID'),
        ),
        migrations.AlterField(
            model_name='taskresult',
            name='task_name',
            field=models.CharField(
                help_text='Name of the Task which was run',
                max_length=255,
                null=True,
                verbose_name='Task Name'),
        ),
        migrations.AlterField(
            model_name='taskresult',
            name='worker',
            field=models.CharField(
                default=None,
                help_text='Worker that executes the task',
                max_length=100,
                null=True,
                verbose_name='Worker'),
        ),
        migrations.AddIndex(
            model_name='chordcounter',
            index=models.Index(
                fields=['group_id'],
                name='django_cele_group_i_299b0d_idx'),
        ),
        migrations.AddIndex(
            model_name='taskresult',
            index=models.Index(
                fields=['task_id'],
                name='django_cele_task_id_7f8fca_idx'),
        ),
        migrations.AddIndex(
            model_name='taskresult',
            index=models.Index(
                fields=['task_name'],
                name='django_cele_task_na_08aec9_idx'),
        ),
        migrations.AddIndex(
            model_name='taskresult',
            index=models.Index(
                fields=['status'],
                name='django_cele_status_9b6201_idx'),
        ),
        migrations.AddIndex(
            model_name='taskresult',
            index=models.Index(
                fields=['worker'],
                name='django_cele_worker_d54dd8_idx'),
        ),
        migrations.AddIndex(
            model_name='taskresult',
            index=models.Index(
                fields=['date_created'],
                name='django_cele_date_cr_f04a50_idx'),
        ),
        migrations.AddIndex(
            model_name='taskresult',
            index=models.Index(
                fields=['date_done'],
                name='django_cele_date_do_f59aad_idx'),
        ),
        migrations.AddIndex(
            model_name='groupresult',
            index=models.Index(
                fields=['group_id'],
                name='django_cele_group_i_3cddec_idx'),
        ),
        migrations.AddIndex(
            model_name='groupresult',
            index=models.Index(
                fields=['date_created'],
                name='django_cele_date_cr_bd6c1d_idx'),
        ),
        migrations.AddIndex(
            model_name='groupresult',
            index=models.Index(
                fields=['date_done'],
                name='django_cele_date_do_caae0e_idx'),
        ),
    ]
