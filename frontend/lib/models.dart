// models.dart

import 'package:json_annotation/json_annotation.dart';

part 'models.g.dart';

@JsonSerializable()
class Order {
  int id;
  String address;
  String contactNumber;
  String note;
  DateTime createdDate;
  DateTime productDeliveryDate;
  int shopperId;
  int cartId;
  int userAccountId;
  double tip;

  Order({
    required this.id,
    required this.address,
    required this.contactNumber,
    required this.note,
    required this.createdDate,
    required this.productDeliveryDate,
    required this.shopperId,
    required this.cartId,
    required this.userAccountId,
    required this.tip,
  });

  factory Order.fromJson(Map<String, dynamic> json) => _$OrderFromJson(json);
  Map<String, dynamic> toJson() => _$OrderToJson(this);
}
@JsonSerializable()
class Account {
  final int id;
  // Add other properties

  Account({
    required this.id,
    // Initialize other properties as needed
  });

  factory Account.fromJson(Map<String, dynamic> json) {
    return Account(
      id: json['id'] as int,
      // Map other properties from JSON
    );
  }
}
@JsonSerializable()
class User {
  int id;
  String userName;
  String password;
  String email;
  bool isVerified;
  bool isActive;
  bool isSoftDeleted;
  // final Account? account; // Account is optional

  User({
    required this.id,
    required this.userName,
    required this.password,
    required this.email,
    required this.isVerified,
    required this.isActive,
    required this.isSoftDeleted,
    // this.account,
  });

  factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json);
  Map<String, dynamic> toJson() => _$UserToJson(this);
}
