from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    PROFILE_MIN_AGE = 12
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField()

    age = models.IntegerField(
        validators=(
            MinValueValidator(PROFILE_MIN_AGE),
        ),
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Game(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15

    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD_CARD_GAME = 'Board/Card Game'
    OTHER = 'Other'

    CATEGORIES = [(x, x) for x in [ACTION, ADVENTURE, PUZZLE, STRATEGY, SPORTS, BOARD_CARD_GAME, OTHER]]

    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5.0

    LVL_MIN_VALUE = 1

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=CATEGORIES,
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(RATING_MIN_VALUE),
            MaxValueValidator(RATING_MAX_VALUE),
        ),
    )

    max_level = models.IntegerField(
        validators=(
            MinValueValidator(LVL_MIN_VALUE),
        ),
        null=True,
        blank=True,
    )

    image = models.URLField()

    summary = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
