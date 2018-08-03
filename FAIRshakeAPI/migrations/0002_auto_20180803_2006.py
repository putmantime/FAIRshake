# Generated by Django 2.0.7 on 2018-08-03 20:06

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import select2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('FAIRshakeAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='assessment',
            field=select2.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answers', to='FAIRshakeAPI.Assessment'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='metric',
            field=select2.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answers', to='FAIRshakeAPI.Metric'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='assessor',
            field=select2.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='project',
            field=select2.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='assessments', to='FAIRshakeAPI.Project'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='requestor',
            field=select2.fields.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='rubric',
            field=select2.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='assessments', to='FAIRshakeAPI.Rubric'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='target',
            field=select2.fields.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='assessments', to='FAIRshakeAPI.DigitalObject'),
        ),
        migrations.AlterField(
            model_name='digitalobject',
            name='authors',
            field=select2.fields.ManyToManyField(blank=True, sorted=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='digitalobject',
            name='rubrics',
            field=select2.fields.ManyToManyField(blank=True, related_name='digital_objects', sorted=False, to='FAIRshakeAPI.Rubric'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='authors',
            field=select2.fields.ManyToManyField(blank=True, sorted=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='authors',
            field=select2.fields.ManyToManyField(blank=True, sorted=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='digital_objects',
            field=select2.fields.ManyToManyField(blank=True, related_name='projects', sorted=False, to='FAIRshakeAPI.DigitalObject'),
        ),
        migrations.AlterField(
            model_name='rubric',
            name='authors',
            field=select2.fields.ManyToManyField(blank=True, sorted=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rubric',
            name='metrics',
            field=select2.fields.ManyToManyField(blank=True, related_name='rubrics', sorted=False, to='FAIRshakeAPI.Metric'),
        ),
    ]