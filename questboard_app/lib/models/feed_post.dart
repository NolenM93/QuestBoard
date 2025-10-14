import 'package:hive/hive.dart';

part 'feed_post.g.dart';

@HiveType(typeId: 20)
enum PostType {
  @HiveField(0)
  questCompleted,
  @HiveField(1)
  achievementUnlocked,
  @HiveField(2)
  levelUp,
  @HiveField(3)
  announcement,
  @HiveField(4)
  lootDrop,
  @HiveField(5)
  milestone,
  @HiveField(6)
  teamUpdate,
}

@HiveType(typeId: 21)
class FeedPost extends HiveObject {
  @HiveField(0)
  final String id;

  @HiveField(1)
  final String authorId;

  @HiveField(2)
  final String teamId;

  @HiveField(3)
  final PostType type;

  @HiveField(4)
  final String content;

  @HiveField(5)
  final DateTime createdAt;

  @HiveField(6)
  final List<String> imageUrls;

  @HiveField(7)
  final Map<String, dynamic> metadata; // Quest/achievement IDs, etc.

  @HiveField(8)
  final List<String> reactions; // User IDs who reacted

  @HiveField(9)
  final List<FeedComment> comments;

  @HiveField(10)
  final bool isPinned;

  FeedPost({
    required this.id,
    required this.authorId,
    required this.teamId,
    required this.type,
    required this.content,
    required this.createdAt,
    this.imageUrls = const [],
    this.metadata = const {},
    this.reactions = const [],
    this.comments = const [],
    this.isPinned = false,
  });

  FeedPost copyWith({
    String? id,
    String? authorId,
    String? teamId,
    PostType? type,
    String? content,
    DateTime? createdAt,
    List<String>? imageUrls,
    Map<String, dynamic>? metadata,
    List<String>? reactions,
    List<FeedComment>? comments,
    bool? isPinned,
  }) {
    return FeedPost(
      id: id ?? this.id,
      authorId: authorId ?? this.authorId,
      teamId: teamId ?? this.teamId,
      type: type ?? this.type,
      content: content ?? this.content,
      createdAt: createdAt ?? this.createdAt,
      imageUrls: imageUrls ?? this.imageUrls,
      metadata: metadata ?? this.metadata,
      reactions: reactions ?? this.reactions,
      comments: comments ?? this.comments,
      isPinned: isPinned ?? this.isPinned,
    );
  }
}

@HiveType(typeId: 22)
class FeedComment extends HiveObject {
  @HiveField(0)
  final String id;

  @HiveField(1)
  final String authorId;

  @HiveField(2)
  final String content;

  @HiveField(3)
  final DateTime createdAt;

  @HiveField(4)
  final List<String> reactions;

  FeedComment({
    required this.id,
    required this.authorId,
    required this.content,
    required this.createdAt,
    this.reactions = const [],
  });
}
