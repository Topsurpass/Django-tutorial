import uuid
from django.db import models
from app.Users.models import User
from app.Property.models import Property
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField( validators=[
            MinValueValidator(1, message="Rating must be between 1 and 5"),
            MaxValueValidator(5, message="Rating must be between 1 and 5")
        ])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.review_id} - {self.rating}"
