from django.contrib.auth.models import User
from api.models import UserProfile,Transactions
from rest_framework.serializers import ModelSerializer



class UserProfileSerializer(ModelSerializer):
    class Meta:
        model=UserProfile
        fields=["account_number",
                "phone",
                "mpin",
                "ac_type",
                "balance",
                "pan"]
class UserSerializer(ModelSerializer):
    profile=UserProfileSerializer(required=True)
    class Meta:
        model=User
        fields=["username","email","password","first_name","profile"]

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')

        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')

        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.account_number = profile_data.get('account_number', profile.account_number)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.pan = profile_data.get('pan', profile.pan)
        profile.mpin = profile_data.get('country', profile.mpin)
        profile.ac_type= profile_data.get('city', profile.ac_type)
        profile.balance= profile_data.get('zip', profile.balance)
        profile.save()

        return instance
class TransactionSerializer(ModelSerializer):
    class Meta:
        model=Transactions
        fields=["to_acno","amount","description","payment_mode"]

    def create(self,validated_data):
        transaction=Transactions(**validated_data,account=self.context["user"])
        userprofile=UserProfile.objects.get(id=self.context["user"])
        userprofile.balance-=validated_data.get("amount")
        userprofile.save()
        userprofile = UserProfile.objects.get(id=validated_data.get("to_acno"))
        userprofile.balance += validated_data.get("amount")
        userprofile.save()

        transaction.save()
        return transaction
