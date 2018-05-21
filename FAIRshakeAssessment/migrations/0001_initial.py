# Generated by Django 2.0.5 on 2018-05-21 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FAIRshakeHub', '0001_initial'),
        ('FAIRshakeRubric', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('S', 'Self assessment'), ('T', 'Test assessment'), ('A', 'Automated assessment'), ('U', 'User submitted assessment')], max_length=1, verbose_name='Type')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='FAIRshakeHub.Resource')),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='FAIRshakeRubric.Rubric')),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='Answer (json serialized)')),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='FAIRshakeAssessment.Assessment')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='FAIRshakeRubric.Question')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='assessmentresult',
            unique_together={('assessment', 'question')},
        ),
    ]
