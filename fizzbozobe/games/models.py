from django.db import models

# Create your models here.
class Game(models.Model):
    ## Entity representing a game in the system

    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255,
        default="",
        help_text="Name of the game",
        blank=False,
    )

    author = models.CharField(
        max_length=255,
        default="",
        help_text="Author of the game",
        blank=False,
    )

    min_number = models.IntegerField(
        help_text="Minimum number in the game range",
    )

    max_number = models.IntegerField(
        help_text="Maximum number in the game range",
    )

    rules_count = models.IntegerField(
        help_text="Number of rules associated with the game",
    )

    created_at = modes.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the game was created",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        help_text="Timestamp when the game was last updated",
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Timestamp when the game was deleted",
    )

    #Navigation properties would be represented via related_name in Django ORM

    class Meta:
        db_table = "games"
        verbose_name = "Game"
        verbose_name_plural = "Games"
    
    def __str__(self):
        # Returns a string representation of the object.
        return self.name
    
class GameSession(models.Model):
    player_name = models.CharField(
        max_length=255,
        default="",
        help_text="Name of the player",
        blank=False,
    )

    duration_seconds = models.IntegerField(
        help_text="Duration of the game session in seconds",
    )

    started_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the game session started",
    )

    ended_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Timestamp when the game session ended",
    )

    number_used = models.JSONField(
        default=list,
        help_text="List of numbers used in the game session",
    )

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="game_sessions",
        help_text="The game associated with this session",
    )

    


# namespace fizzbozo_be.Entities
# {
#     public class GameSession
#     {
#         public Guid Id { get; set; }
#         public string PlayerName { get; set; } = string.Empty;
#         public int DurationSeconds { get; set; }
#         public DateTime StartedAt { get; set; }
#         public DateTime EndedAt { get; set; }
#         public List<int> NumbersUsed { get; set; } = new();

#         // Foreign key
#         public int GameId { get; set; }
#         public Game Game { get; set; }

#         //Navigation Properties
#         public ICollection<GameQuestion> GameQuestions { get; set; }
#         public Result Result { get; set; }
#     }
# }

    # {
    #     public int Id { get; set; }
    #     public string Name { get; set; } = string.Empty;
    #     public string Author { get; set; } = string.Empty;
    #     public int MinNumber { get; set; }
    #     public int MaxNumber { get; set; }
    #     public int RulesCount { get; set; }
    #     public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    #     public DateTime? UpdatedAt { get; set; }
    #     public DateTime? DeletedAt { get; set; }

    #     // Navigation properties
    #     public ICollection<Rule> Rules { get; set; } 
    #     public ICollection<GameSession> GameSessions { get; set; }
    # }

#     namespace fizzbozo_be.Entities
# {
#     public class GameQuestion
#     {
#         public int Id { get; set; }
#         public int Number { get; set; }
#         public string ExpectedAnswer { get; set; } = string.Empty;
#         public string PlayerAnswer { get; set; } = string.Empty;
#         public bool IsCorrect {  get; set; }
#         public DateTime AnsweredAt { get; set; } = DateTime.UtcNow;

#         // Foreign key
#         public Guid SessionId { get; set; }
#         public GameSession GameSession { get; set; }
#     }
# }
