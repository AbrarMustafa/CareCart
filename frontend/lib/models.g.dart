// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'models.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Order _$OrderFromJson(Map<String, dynamic> json) => Order(
      id: (json['id'] as num).toInt(),
      address: json['address'] as String,
      contactNumber: json['contactNumber'] as String,
      note: json['note'] as String,
      createdDate: DateTime.parse(json['createdDate'] as String),
      productDeliveryDate:
          DateTime.parse(json['productDeliveryDate'] as String),
      shopperId: (json['shopperId'] as num).toInt(),
      cartId: (json['cartId'] as num).toInt(),
      userAccountId: (json['userAccountId'] as num).toInt(),
      tip: (json['tip'] as num).toDouble(),
    );

Map<String, dynamic> _$OrderToJson(Order instance) => <String, dynamic>{
      'id': instance.id,
      'address': instance.address,
      'contactNumber': instance.contactNumber,
      'note': instance.note,
      'createdDate': instance.createdDate.toIso8601String(),
      'productDeliveryDate': instance.productDeliveryDate.toIso8601String(),
      'shopperId': instance.shopperId,
      'cartId': instance.cartId,
      'userAccountId': instance.userAccountId,
      'tip': instance.tip,
    };

User _$UserFromJson(Map<String, dynamic> json) => User(
      id: (json['id'] as num).toInt(),
      userName: json['userName'] as String,
      password: json['password'] as String,
      email: json['email'] as String,
      isVerified: json['isVerified'] as bool,
      isActive: json['isActive'] as bool,
      isSoftDeleted: json['isSoftDeleted'] as bool,
    );

Map<String, dynamic> _$UserToJson(User instance) => <String, dynamic>{
      'id': instance.id,
      'userName': instance.userName,
      'password': instance.password,
      'email': instance.email,
      'isVerified': instance.isVerified,
      'isActive': instance.isActive,
      'isSoftDeleted': instance.isSoftDeleted,
    };
