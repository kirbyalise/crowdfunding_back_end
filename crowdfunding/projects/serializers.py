from rest_framework import serializers
from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'
        extra_kwargs = {'anonymous': {'write_only': True}}
    
    def to_representation(self, instance):
        # if instance.anonymous == True:
        #     return {
        #         "id": instance.id,
        #         "amount": instance.amount,
        #         "comment": instance.comment,
        #         "project": instance.project.id
        #     }
        # return super().to_representation(instance)
        
        json_rep = super().to_representation(instance)
        if instance.anonymous == True:
            del json_rep["supporter"]
        return json_rep

        
# -------

class PledgeDetailSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
        def update(self, instance, validated_data):
            instance.amount = validated_data.get('amount', instance.amount)
            instance.comment = validated_data.get('comment', instance.comment)
            instance.anonymous = validated_data.get('anonymous', instance.anonymous)
            instance.project = validated_data.get('project', instance.project)
            instance.save()
            return instance


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    total_raised = serializers.SerializerMethodField()  # Add this to calculate total raised

    class Meta:
        model = apps.get_model('projects.Project')
        fields = '__all__'  # Include total_raised in the fields

    def get_total_raised(self, obj):
        # Calculate the sum of all pledges related to this project
        return sum(pledge.amount for pledge in obj.pledges.all())


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    
    class Meta(ProjectSerializer.Meta):
        fields = '__all__'  # Include all fields, including total_raised and pledges
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance