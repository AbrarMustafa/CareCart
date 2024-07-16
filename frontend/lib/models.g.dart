// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'models.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Order _$OrderFromJson(Map<String, dynamic> json) => Order(
      id: (json['id'] as num).toInt(),
      address: json['address'] as String,
      contactNumber: json['contact_number'] as String,
      note: json['note'] as String,
      createdDate: DateTime.parse(json['created_date'] as String),
      productDeliveryDate:
          DateTime.parse(json['product_delivery_date'] as String),
      shopperId: (json['shopper_id'] as num).toInt(),
      cartId: (json['cart_id'] as num).toInt(),
      userAccountId: (json['user_account_id'] as num).toInt(),
      tip: (json['tip'] as num).toDouble(),
    );

Map<String, dynamic> _$OrderToJson(Order instance) => <String, dynamic>{
      'id': instance.id,
      'address': instance.address,
      'contact_number': instance.contactNumber,
      'note': instance.note,
      'created_date': instance.createdDate.toIso8601String(),
      'product_delivery_date': instance.productDeliveryDate.toIso8601String(),
      'shopper_id': instance.shopperId,
      'cart_id': instance.cartId,
      'user_account_id': instance.userAccountId,
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
